function solution(people, limit) {
    var answer = 0;
    
    people.sort((a,b)=>a-b)
    let start = 0
    let end = people.length-1
    
    while (start<=end)
    {        
        answer += 1
        
        if (people[start]+people[end] <= limit){
            start+=1
            end-=1
        }
        else
            {
            end-=1
            }   
    }
    return answer;   
}

