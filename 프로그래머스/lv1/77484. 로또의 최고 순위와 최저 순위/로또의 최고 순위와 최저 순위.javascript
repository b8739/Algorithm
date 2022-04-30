function solution(lottos, win_nums) {
    let answer = []
    let win_cnt = 0
    //score
    let score = new Map ()
    for (let [idx,num] of [6,5,4,3,2].entries()){
        score.set(num,idx+1)
    }
    score.set(0,6)
    score.set(1,6)
    
    //lottos
    let lotto_res = new Map()
    for (let num of lottos){
        lotto_res.set(num,lotto_res.get(num)+1||1) //있으면 추가, 없으면 0
    }
    //check
    for (let win of win_nums){
        if (lotto_res.get(win)){
            win_cnt += 1
        }    
    }
    // 0 update
    //최고 
    zero_cnt = lotto_res.get(0)||0
    
    answer[0] = score.get(win_cnt+zero_cnt||1)
    //최저
    answer[1] = score.get(win_cnt||1)
    
    //set에 has로 확인하고 있으면 없앰
    return answer
}