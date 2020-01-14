# Queen's Attack II
# https://www.hackerrank.com/challenges/queens-attack-2/problem

# TODO: Approach 1

def queenAttack(n, k, r_q, c_q, obstacles) -> int:
    totalCount = 0

    # Right
    rRObstacle = -1
    cRObstacle = -1
    # Bottom
    rBObstacle = -1
    cBObstacle = -1
    # Left
    rLObstacle = -1
    cLObstacle = -1
    # Top
    rTObstacle = -1
    cTObstacle = -1
    # Bottom Left
    rBLObstacle = -1
    cBLObstacle = -1
    # Bottom Right
    rBRObstacle = -1
    cBRObstacle = -1

    for row in range(len(obstacles)):
        rObstacle = obstacles[row][0]
        cObstacle = obstacles[row][1]
        
        # Right
        if (cObstacle < cRObstacle or rRObstacle == -1) and cObstacle > c_q and rObstacle == r_q:
            rRObstacle = rObstacle
            cRObstacle = cObstacle
        # Bottom
        if (rObstacle < rBObstacle or rBObstacle == -1) and rObstacle < r_q and cObstacle == c_q:
            rBObstacle = rObstacle
            cBObstacle = cObstacle
        # Left
        if (cObstacle > cLObstacle or cLObstacle == -1) and cObstacle < c_q and rObstacle == r_q:
            rLObstacle = rObstacle
            cLObstacle = cObstacle
        # Top
        if (rObstacle < rTObstacle or rTObstacle == -1) and rObstacle > r_q and cObstacle == c_q:
            rTObstacle = rObstacle
            cTObstacle = cObstacle
        # Bottom Left
        # if (rObstacle > rBLObstacle or rBLObstacle == -1) and rObstacle < r_q and cObstacle < c_q:
        #     rBLObstacle = rObstacle
        #     cBLObstacle = cObstacle
        # Bottom Right
        # if (rObstacle > rBRObstacle or rBRObstacle == -1) and rObstacle < r_q and cObstacle > c_q:
        #     rBRObstacle = rObstacle
        #     cBRObstacle = cObstacle

    # Right
    totalCount += cRObstacle - c_q - 1 if cRObstacle != -1 else n - c_q
    # Bottom
    totalCount +=  r_q - rBObstacle - 1 if rBObstacle != -1 else n - r_q
    # Left
    totalCount += c_q - cLObstacle - 1 if cLObstacle != -1 else c_q - 1
    # Top
    totalCount += rTObstacle - r_q - 1 if rTObstacle != -1 else n - r_q
    # Bottom Left
    # totalCount += c_q - cBLObstacle - 1 if rBLObstacle != -1 else min(c_q - 1, r_q - 1)
    # Bottom Right
    # totalCount += cBRObstacle - c_q - 1 if cBRObstacle != -1 else min(n - c_q, r_q - 1)
    # Top Left
    # Top Right
    
    return totalCount


if __name__ == "__main__":
    n = 5   # Size of the matrix
    k = 3   # Number of obstacles

    r_q, c_q = 4, 3  # Geolocation of Queen

    obstacles = [
        [2, 3],
        [4, 2],
        [5, 5]
    ]

    result = queenAttack(n, k, r_q, c_q, obstacles)
    print(result)
    
