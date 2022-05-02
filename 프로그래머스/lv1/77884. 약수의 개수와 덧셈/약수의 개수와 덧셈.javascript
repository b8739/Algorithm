function solution(left, right) {
    var answer = 0;
    for (let i =left ; i<right+1;i++){
        if (isDivisorsEven(i)){
            answer+=i
        }
        else answer-=i
    }
    return answer;
}

function isDivisorsEven(num){
    let divisors = 0
    if (num == 1) return false
    for (let i = 2; i<num;i++){
        if (num%i===0){
            divisors+=1
        }
    }
    
    if (divisors%2===0){
        return true
    }
    return false
    
}