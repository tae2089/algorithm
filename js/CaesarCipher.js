s = 'a b';
function solution(s, n) {
    return s
        .split('')
        .map((c) => {
            if (c === ' ') return ' ';
            const isUpletter = c.toUpperCase() === c;
            let code = c.charCodeAt() + n;
            if ((isUpletter && code > 90) || (!isUpletter && code > 122)) {
                code -= 26;
            }
            return String.fromCharCode(code);
        })
        .join('');
}

solution(s, 1);
