const user_input = "복잡한 세상 편하게 살자"
let result = '';

let test_src =  user_input.split(" ") 
let test_src2 = test_src.map(s => s.slice(0,1))
let test_src3 = test_src2.reduce((s,i) => s+i ) 

console.log(test_src3);