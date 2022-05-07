function solution(skill, skill_trees) {
    var answer = skill_trees.length;
    let pattern = new RegExp(`[^${skill}]`,"g")
    for (let tree of skill_trees){
        let converted = tree.replace(pattern,'')

        for (let i=0;i<converted.length; i++){
            
           if (skill[i] != converted[i]) 
           {
               answer--
               break
           }
        }
    }
    
    return answer;
}