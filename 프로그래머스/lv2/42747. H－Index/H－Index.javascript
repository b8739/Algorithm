

function solution(citations) {
    var hindex=0;
    const length = citations.length
    citations.sort((a,b)=>b-a)
    
    for(let i=0;i<length;i++){
        if(citations[i]<=i) break
        hindex+=1
    
        
    }
    return hindex;
}