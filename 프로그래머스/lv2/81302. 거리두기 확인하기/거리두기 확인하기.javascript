function solution(places) {
  var answer = [];
  answer = places.map((place) => {
      //전체 대기실
      return place.some((room, rowIdx)=>
           room.split('').some((curr,colIdx,roomArr)=>{
              if (curr === 'X') return false;
              let peopleAround = [
                  roomArr[colIdx+1]||"",
                  roomArr[colIdx-1]||"",
                  (place[rowIdx+1]||"")[colIdx],
                  (place[rowIdx-1]||"")[colIdx],
              ].filter((curr)=>curr=='P').length
              return ((curr=='P' && peopleAround>0) || (curr=='O' && peopleAround>1)) 
          })
      ) ? 0 : 1
  })
  return answer;
}