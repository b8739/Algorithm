function solution(s) {
    var answer = '';
    //map
    dict = new Map()
    english = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for (let i=0;i<10;i++){
        dict.set(english[i],i)
    }
    //s
    let word = ''
    
    for (const l of s){
        //숫자일 때
        if (!isNaN(l)){
            answer = answer.concat(l)
            continue
        }
        //숫자가 아닐 때
        word = word.concat(l)
        let converted = dict.get(word)
        if (converted ==undefined){
            continue
        }
        
        //영단어 완성됐을때
        
        else{
            answer = answer.concat(converted)
            word = ''
            continue
        }
    }
    return parseInt(answer);
}