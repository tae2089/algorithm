let checkUsed = [];
var result = 0;
var answer = 0;

function findWord(begin, target, words, answer, checkUsed) {
    if (begin === target) {
        if (result === 0 || result > answer) result = answer;
    }
    for (var i = 0; i < words.length; i++) {
        var diff = 0;
        for (var j = 0; j < words[i].length; j++) {
            if (begin[j] !== words[i][j]) {
                diff++;
            }
        }
        let check = 0;
        for (var k = 0; k < answer; k++) {
            if (checkUsed[k] === words[i]) {
                check = 1;
            }
        }
        if (diff === 1 && check === 0) {
            checkUsed.push(words[i]);
            findWord(words[i], target, words, answer + 1, checkUsed);
        }
    }
}

function solution(begin, target, words) {
    var isValid = false;
    for (var i = 0; i < words.length; i++) {
        if (target === words[i]) {
            isValid = true;
        }
    }
    if (!isValid) {
        return 0;
    }

    findWord(begin, target, words, answer, checkUsed);
    return result;
}