function solution(nums) {
    var answer = 0;
    
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for (let i=0;i<nums.length-2;i++){
        for (let j=i+1;j<nums.length-1;j++){
            for (let k=j+1;k<nums.length;k++){
                answer += isPrime(nums[i],nums[j],nums[k])
            }   
        }
    }
    return answer;
}
function isPrime(i,j,k){
    let num = i+j+k
    for(let i=2;i<=Math.sqrt(num);i++){
        if (num%i===0){
            
            return 0
        }
    }
    
    return 1
}