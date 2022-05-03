function solution(s, n) {
    let answer = ''
    for (let i=0;i<s.length; i++){
        if (s[i] == ' ') {
            answer =answer.concat(' ')
            continue
        }            
        
        let ascii = s[i].charCodeAt()+n
        //같으면 원래도 소문자, 다르면 원래는 대문자
        let ascii_z = s[i] == s[i].toLowerCase() ? 122 : 90
        let final = ascii > ascii_z ? ascii-26 : ascii
        
        answer =answer.concat(String.fromCharCode(final))
    }
    return answer;
}