function solution(progresses, speeds) {
    var answer = [];
    let days = [];
    
    for (let i=0;i<progresses.length; i++){
        days.push(Math.ceil((100-progresses[i]) / speeds[i]))
    
    }
    console.log(days)

    let deployed = days.shift()
    
    answer.push(1)
    
    for (let d of days){
        console.log(`d: ${d}`)
        console.log(`deployed: ${deployed}`)
        
        if (d<=deployed){
            answer[answer.length-1]+=1
        }
        else{
            answer.push(1)
            deployed = d
            
        }
    }
    
    
    return answer;
}