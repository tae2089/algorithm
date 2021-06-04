function solution(left, right) {
    let arr = [];
    let cnt = 0;
    for (i = 1; i < right + 1; i++) {
        arr.push(i);
    }

    for (i = left; i < right + 1; i++) {
        let arr2 = arr.filter((x) => {
            if (i % x == 0) return x;
        });
        arr2.length % 2 == 1 ? (cnt -= i) : (cnt += i);
    }
    return cnt;
}

solution(13, 17);
