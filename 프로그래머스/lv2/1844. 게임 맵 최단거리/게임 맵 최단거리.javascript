function solution(maps) {
    var answer = 0;
    let n = maps.length-1 //0
    let m = maps[0].length-1 //1
    
    // 도달하지 못하는 경우  
    // if (maps[n-1][m] ==0 &&maps[n][m-1] ==0) return -1
    
    let visited = [...Array(n+1)].map(()=>new Array(m+1).fill(0))
    
    let queue = [];
    queue.push([0,0])
    visited[0][0] += 1
    
    let dx = [1,-1,0,0]
    let dy = [0,0,1,-1]
        
    while (queue.length != 0){
    
        let [x,y] = queue.shift()

        if (x == n && y == m) {
            break
        }
        
        for (let i=0;i<4;i++){
            let nx = x+ dx[i]
            let ny = y+ dy[i] 
            
            if (nx>-1 && ny>-1 && nx<=n && ny<=m){
                
                if (visited[nx][ny]==0 && maps[nx][ny]==1){
                    
                    queue.push([nx,ny])
                    visited[nx][ny] = visited[x][y]+1
                    
                    
                }  
            }

        }


    }
    return visited[n][m] == 0 ? -1 : visited[n][m];
}