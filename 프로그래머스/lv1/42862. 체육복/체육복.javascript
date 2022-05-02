function solution(n, lost_b, reserve_b) {
    //번호 하나 차이만 나야 빌려줄 수 있음
    //자신도 잃어버렸으면 못 빌려줌, 아님 빌려줘도 똑같음

    
    lost_b.sort()
    reserve_b.sort()
    
    lost = lost_b.filter(x=>!reserve_b.includes(x))
    reserve = reserve_b.filter(x=>!lost_b.includes(x))
    
    var answer = n-lost.length
    //다 볼 필요 없음
    
    for(let i =0;i<lost.length;i++){   
        
        let front = lost[i]-1
        let back = lost[i]+1
        
        for (let j =0; j<reserve.length;j++){
            
            if (reserve[j] == front || reserve[j] ==back ){
                answer+=1
                reserve[j]=(-1)
                break
            }
        }
    }
    return answer;
}