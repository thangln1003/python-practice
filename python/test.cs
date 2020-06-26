public class Solution {
    public int FindJudge(int N, int[][] trust) {
        var graph = new bool[N, N];
        for(var i = 0; i < trust.Length; ++i){
            graph[trust[i][0] - 1, trust[i][1] - 1] = true;
        }
        
        for(var i = 0; i < N; i++){
            bool isJudge = true;
            for(var j = 0; j < N; j++){
                if(i != j){
                    if(graph[i, j] || !graph[j,i]){
                        isJudge = false;
                    break;
                }
            }
        }

        if(isJudge)
            return i + 1;
        }
        return -1;
    }
}