function solution(numbers) {
    numbers.sort()
    var answer = 0;

    let idx = 0
    for (let i =0; i<10;i++){
        if (i != numbers[idx]){
            answer += i
        }
        else{
          idx+=1  
        }
    }
    return answer;
}

