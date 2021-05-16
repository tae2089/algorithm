const record = [
    'Enter uid1234 Muzi',
    'Enter uid4567 Prodo',
    'Leave uid1234',
    'Enter uid1234 Prodo',
    'Change uid4567 Ryan',
];

function solution(record) {
    let answer = [];
    let newArr = record.map(str => str.split(' '));
    let nickNameDic = {};
    newArr.forEach(value => {
        if (value.length === 3) {
            nickNameDic[value[1]] = value[2];
        }
    });
    newArr.forEach(value => {
        if (value[0] === 'Enter') {
            answer.push(nickNameDic[value[1]] + '님이 들어왔습니다.');
        } else if (value[0] === 'Leave') {
            answer.push(nickNameDic[value[1]] + '님이 나갔습니다.');
        }
    });
    return answer;
}

solution(record);
