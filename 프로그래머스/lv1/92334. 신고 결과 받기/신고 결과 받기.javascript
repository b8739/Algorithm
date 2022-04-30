function solution(id_list, report, k) {
    var answer = [];
    
    for (let i of id_list){
        answer.push(0)
    }
    let id_list_map = new Map()
    
    for (let idx in id_list){
        id_list_map.set(id_list[idx],idx)
        
    }
    
    let splitReport  = report.map(x=>x.split(' '))
    let newReport = {}
    for (let report of splitReport){
        if (report[1] in newReport == false){
            newReport[report[1]] = new Set()
        }
        newReport[report[1]].add(report[0])
    }
    for (let id in newReport){
        
        if (newReport[id].size>=k){
            for (let mailId of newReport[id]){
                let ans_idx = id_list_map.get(mailId)
                
                // console.log(ans_idx)
                answer[ans_idx]+=1
            }
        }
    }
    
    console.log(answer)
    return answer;
}
let id_list = ["muzi", "frodo", "apeach", "neo"]
let report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
let k =  2

solution(id_list,report,k)