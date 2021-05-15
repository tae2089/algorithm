//const n = prompt('입력해주세요.').split('');

let checkBrackets = (e) => {
	var count = 0;
	console.log(e.length);
	// 괄호 갯수가 짝수로 떨어지는지 확인
	for (var i=0; i<e.length;i++){
		if (e[i] === '('){
			count++; 
		}
		if(e[i]=== ')'){
			count--;
		}
	}
	if (count !== 0){
      return false;
	}

	// 괄호를 스택에 넣어서 스택이 0면 true
	let 괄호 = [];
    for (let i in e){
        if (e[i] === '(') {
            괄호.push('(');
        }
            
        if (e[i] === ')') {
            if (괄호.length === 0) {
                return false;
            }
            괄호.pop();
        }   
    }
    return true;
};
console.log(checkBrackets("("));


if (checkBrackets("(") === true){
 console.log("YES");
}else{
 console.log("NO");
}
