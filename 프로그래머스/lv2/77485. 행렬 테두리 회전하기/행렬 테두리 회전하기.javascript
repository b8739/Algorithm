function solution(rows, columns, queries) {
    var answer = [];
    //2차원 배열 생성
    let arr = Array.from(new Array(rows+1),() => new Array(columns+1))
    
    let idx = 0
    //배열에 값 집어 넣기
    for (let i=1;i<=rows;i++){
        for (let j=1;j<=columns;j++){
            arr[i][j] = ++idx
        }
    }
    //stack
    for (let q of queries){//[2,2,5,4] x1,y1,x2,y2
        let [x1,y1,x2,y2] = q
        let stack = []

        //맨 위, 행 고정
        for (let i=y1; i<y2; i++){
            stack.push(arr[x1][i])
        }
        //오른쪽,열 고정
        for (let i=x1; i<x2; i++){
            stack.push(arr[i][y2])
        }

        //맨 밑, 행 고정
        for (let i=y2; i>y1; i--){
            stack.push(arr[x2][i])
        }
        //왼쪽, 열 고정
        for (let i=x2; i>x1; i--){
            stack.push(arr[i][y1])
        }    
        //최소값
        answer.push(Math.min(...stack))
        let first = stack.pop()
        stack.unshift(first)
        //stack에서 꺼내서 배열 값 바꾸기

        //맨 위, 행 고정
        for (let i=y1; i<y2; i++){
            arr[x1][i]= stack.shift()
        }
        //오른쪽,열 고정
        for (let i=x1; i<x2; i++){
            arr[i][y2] = stack.shift()
        }

        //맨 밑, 행 고정
        for (let i=y2; i>y1; i--){
            arr[x2][i] = stack.shift()
        }
        //왼쪽, 열 고정
        for (let i=x2; i>x1; i--){
            arr[i][y1] = stack.shift()
        }    
        
    }
    return answer;
}