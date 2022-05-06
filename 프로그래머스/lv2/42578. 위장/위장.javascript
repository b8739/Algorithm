function solution(clothes) {
    let answer = 1
    let count = {}
    for (let i of clothes){
        count[i[1]] = (count[i[1]]||1)+1
    }
    
    for (let category in count){
        answer*=count[category]
    }

    return answer-1
}