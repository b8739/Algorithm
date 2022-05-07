function solution(n, computers) {
    var answer = 0;
    let visited = [...Array(n)].fill(false)
    
    const dfs = (x) => {
        visited[x]=true
        
        for (let i=0;i<computers[x].length;i++){
            if (!visited[i] && computers[x][i]!=0){
                dfs(i)   
            }
        }
    }
    
    for (let i =0;i<n;i++){
        if (!visited[i]) 
        {
            dfs(i,0)
            answer+=1

        }
    }
    return answer;
}