function solution(arr)
{
    var answer = [];

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    let temp = -1
    for (let i of arr){
        if (temp != i){
            temp = i
            answer.push(i)
        }
    }
    
    return answer;
}