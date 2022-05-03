function solution(record) {
    
    let entered = "님이 들어왔습니다."
    let left = "님이 나갔습니다."

    var answer = [];
    
    let id_list = new Map()
    
    for (let rec of record){
        let arr = rec.split(' ')
        
        if (arr[0] == 'Enter'||arr[0] == 'Change') id_list.set(arr[1],arr[2])
        if (arr[0] == 'Enter') answer.push([arr[1],entered])
        else if (arr[0] == 'Leave') answer.push([arr[1],left])    
    }
    answer = answer.map(x=>(id_list.get(x[0])+x[1]))
    
    return answer;
}