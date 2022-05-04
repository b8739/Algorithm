function solution(s)
{
    let arr = []
    
    for (let i of s){
        if (arr.length == 0 || arr[arr.length-1]!=i){
            arr.push(i)
            continue
        }
        //같다면
        else{
            arr.pop()
        }
        
    }
    return arr.length==0 ? 1 : 0
}