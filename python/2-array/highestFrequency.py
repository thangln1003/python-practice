

from collections import Counter
import heapq

def migratoryBirds(arr) -> int:
    count = Counter(arr)
    result = heapq.nlargest(1, count.keys(), key=count.get)

    return result[0] if result else None

if __name__ == "__main__":
    arr = [1, 4, 4, 4, 5, 3]

    print("Result: ", end=" ")
    print(migratoryBirds(arr))
