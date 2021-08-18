function createPoint(p1, p2) {
    const result = [];
    var dist = Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
    if (dist > 10) {
        const middle = {
            x: (p1.x + p2.x) / 2,
            y: (p1.y + p2.y) / 2,
        };
        result.push(middle);
        const left = createPoint(p1, middle);
        const right = createPoint(middle, p2);
        return result.concat(left).concat(right);
    }
    return result;
}
function addpoInts(arr) {
    const left = createPoint(arr[0], arr[1]);
    arr = arr.concat(left);
    return arr.sort(function (a, b) {
        return a.x - b.x;
    });
}

const a = addpoInts([
    { x: 100, y: 100 },
    { x: 200, y: 200 },
]);
console.log(a);
