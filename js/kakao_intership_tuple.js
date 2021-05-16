const s = '{{2},{2,1},{2,1,3},{2,1,3,4}}';

function soluction(s) {
    var answer = [];
    var counter = [];
    s = s.replace('{{', '');
    s = s.replace('}}', '');
    const s_split = s.split('},{');
    const values = s_split.flatMap(x => x.split(','));
    const keys = [...new Set(values)];

    const dic = {};
    values.forEach(x => {
        if (dic[x] === undefined) {
            dic[x] = 1;
        } else {
            dic[x] = dic[x] + 1;
        }
    });

    for (let number in dic) {
        answer.push([number, dic[number]]);
    }
    answer.sort(function (a, b) {
        return b[1] - a[1];
    });
    answer = answer.map(x => parseInt(x[0]));

    return answer;
}

console.log(soluction(s));
