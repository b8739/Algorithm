

function solution(nums) {
    //중복이 없어진 nums 배열
    can_take = nums.length/2 //2
    nums = [...new Set(nums)]
    var answer = 0;
    can_take > nums.length ? answer = nums.length : answer = can_take
    return answer;
}