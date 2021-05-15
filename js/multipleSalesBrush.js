function solution(enroll, referral, seller, amount) {
    var answer = [];
    var recommend = {};
    var result = {};
    var a = 0;
    var s = '';
    result['-'] = 0;
    for (var key in enroll) {
        recommend[enroll[key]] = referral[key];
        result[enroll[key]] = 0;
    }
    for (var _ in seller) {
        a = amount[_] * 100;
        s = seller[_]
        result[s] += a
        while (true) {
            a = parseInt(a / 10);
            if (a < 1) {
                break;
            } else {
                result[s] -= a;
                result[recommend[s]] += a;
                s = recommend[s];
            }
            if (s == '-')
                break;
        }
    }
    for (var i = 0; i < enroll.length; i++) {
        answer.push(result[enroll[i]]);
    }
    return answer;
}