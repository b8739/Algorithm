function solution(str1, str2) {
    var answer = 0;
    
    let set_1 = convertToSet(str1)
    let set_2 = convertToSet(str2)
    
    let [map_1,map_2] = [countSetElement(set_1),countSetElement(set_2)]
    //합집합
    let union = []
    let union_keys = new Set([... map_1.keys(),... map_2.keys()])
    
    for(let k of union_keys){        
        let max_cnt = Math.max(map_1.get(k)||0,map_2.get(k)||0)
        union.push(...k.repeat(max_cnt).split(k).slice(0,-1).fill(k))
    }
    
    //교집합
    let intersection = []
    let inter_keys = [...union_keys].filter(x=>map_1.has(x) && map_2.has(x))
    
    for(let k of inter_keys){        
        let min_cnt = Math.min(map_1.get(k)||0,map_2.get(k)||0)
        intersection.push(...k.repeat(min_cnt).split(k).slice(0,-1).fill(k))
    }
    
    //공집합
    if (intersection.length == 0 && union.length == 0) return 65536
    
    answer = Math.floor(intersection.length/union.length*65536)
    return answer;
}

function convertToSet(str){
    str = str.toLowerCase()
    return str.split('').map((x,idx)=>(
       x.concat(str[idx+1])
    )).slice(0,-1).filter(set=>set.search(/[\W\d_]/g)==-1)
}
function countSetElement(arr){
    let cnt_map = new Map()
    for (let i of arr){
        cnt_map.set(i,cnt_map.get(i)+1||1)
    }
    return cnt_map
}