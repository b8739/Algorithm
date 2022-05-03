function solution(n) {
    let answer = 0
    for (let i=2;i<=n;i++){
        answer += isPrime(i)
    }
    return answer;
}

function isPrime(num){
    for (let i =2;i<=Math.sqrt(num);i++){
        if(num%i===0){
            return 0
        }
    }
    return 1
    
}
