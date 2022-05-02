function solution(N, stages) {
    var answer = [];
    
    stages.sort((a,b)=>a-b)
    let mappedArr = []
    // 1 2 2 2 3 3 4 6
    for (let i =1 ; i<N+1;i++){
        //state에 도달
        let qualified = stages.filter(s=>s>=i);
        let entered = qualified.length;
        
        //현재 그 state랑 값이 똑같으면 머물러있다는 의미
        let uncleared = qualified.filter(s=>s==i).length
        let cleared = entered-uncleared
        
        let failRate = uncleared/entered
        mappedArr.push([i,failRate])
    }
    mappedArr.sort((a, b) => b[1] - a[1]); //value기준 내림차순
    mappedArr = mappedArr.map(x=>{return x[0]})
    
    return mappedArr;
}