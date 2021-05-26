const array = ['0', 1, 2, '0', '0', 3];
function solution(nums) {
    const max = nums.length / 2;
    const newArr = nums.filter((item, index) => nums.indexOf(item) === index);
    const cnt = newArr.length;
    if (cnt >= max) {
        return max;
    } else {
        return cnt;
    }
}

solution(array);
