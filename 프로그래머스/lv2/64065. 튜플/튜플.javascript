function solution(s) {
    let answer = []
    s = s.replace(/[{]/g,'[').replace(/[}]/g,']')
    let arr = eval(s).sort((a,b) => a.length-b.length)
    for (let set of arr){
            let difference = set.filter(x=>!answer.includes(x));
            answer.push(...difference)
    }
    console.log(answer)
    return answer
}