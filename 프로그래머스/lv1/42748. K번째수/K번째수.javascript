function solution(array, commands) {
    var answer = [];
    for (const c of commands){
        let [i,j,k] = [c[0]-1,c[1],c[2]-1]
        
        answer.push(array.slice(i,j).sort((a,b)=>a-b)[k])
    }
    return answer;
}