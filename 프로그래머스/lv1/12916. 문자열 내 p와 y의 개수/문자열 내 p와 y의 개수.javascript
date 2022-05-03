function solution(s){
    var answer = true;
    
    if (s.length === 0) return answer
    
    s = s.toLowerCase()
    
    p_cnt = 0
    y_cnt = 0
    
    for (let i of s){
        if (i == 'p') p_cnt+=1
        else if (i == 'y') y_cnt+=1
    }
    console.log(s)
    if (p_cnt!=y_cnt) answer=false;

    return answer;
}