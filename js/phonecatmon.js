const array = [3, 3, 3, 2, 2, 2];
function solution(nums) {
    const newArr = nums.filter((item, index) => nums.indexOf(item) === index);
    return newArr.length > nums.length / 2 ? nums.length / 2 : newArr.length;
}

solution(array);
