function solution(cacheSize, cities) {
    var answer = 0;
    let queue = []
    for (let city of cities){
        city = city.toLowerCase()
        //없을 경우
        if (cacheSize==0) return cities.length*5
        
        if (!queue.includes(city))
        {
            if (queue.length == cacheSize) queue.shift()
            queue.push(city)
            answer+=5
        }
        //있을 경우
        else{
            const index = queue.indexOf(city)
            queue.splice(index,1)
            queue.push(city)
            answer+=1
        }
    }
    return answer;
}