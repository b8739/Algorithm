
function solution (participant, completion) {
    participant.sort()
    completion.sort()
    for (let [idx,v] of participant.entries()){
        if (v!=completion[idx]){
            return v
        }
    }
}