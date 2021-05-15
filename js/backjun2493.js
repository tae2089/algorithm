//파일을 읽어오기 위해 Node.js의 built-in file system module인 fs를 썼다.
var fs = require('fs');

// input을 읽어와서 변수로 선언&할당한다.
// fs 모듈을 써서 경로(여기서는 '/dev/stdin')에 있는 파일을 동기적으로 읽어와서
// 그 내용을 input에 저장한다. toString().split(" ")에서 유추할 수 있는 것 처럼
// 읽어온 내용은 array로 저장이 된다.
var input = fs.readFileSync('/dev/stdin').toString().split(' ');

// input에서 지정한 벨류를 읽어와서 별개의 변수로 선언하고 활용한다.
// input 변수에 저장한 각 입력값이 지금은 string이기 때문에
// 이것을 문제에서 요구하는 숫자로 쓸려면 parseInt로 형변환을 해주어야 한다.
var a = parseInt(input[0]);
var b = parseInt(input[1]);

// 사실상 여기서부터 구현부라고 보시면 되겠다.
console.log(a+b);
