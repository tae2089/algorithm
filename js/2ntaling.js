function solution(n) {
	let answer = 0;
    let dp = Array(n).fill(0)
    dp[0] = 1
    dp[1] = 2
    for(var i=2; i<n; i++){
        let a = dp[i-1] + dp[i-2]
        dp[i] = a %  1000000007
    }
    return dp[n-1];
}
console.log(solution(4))
