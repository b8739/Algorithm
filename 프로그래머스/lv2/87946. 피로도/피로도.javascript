function solution(k, dungeons) {
    var answer = 0;
    let visited = new Array(dungeons.length).fill(false)
    // dfs
    
    function dfs(index,energy,been){
        //에너지가 고갈되어도 멈추는 예외사항이 필요
        for (let i=0;i<dungeons.length;i++){
            if (!visited[i] && energy>=dungeons[i][0] && energy>=dungeons[i][1]){
                visited[i] = true
                dfs(i+1,energy-dungeons[i][1],been+1)
                visited[i] = false
             }
        }   

        answer = Math.max(answer,been)
        return answer
    }
    
    answer = dfs(-1,k,0)
    console.log(answer)
    return answer

}