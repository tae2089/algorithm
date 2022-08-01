package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	var a,b,c int
	fmt.Fscan(r, &a, &b, &c)
	total := a * b * c
	var arr []int = make([]int, 10)
	for total > 0 {
		arr[total % 10] ++
		total /= 10
	}
	for i := 0; i < 10; i++ {
		w.WriteString(strconv.Itoa(arr[i]))
		w.WriteByte('\n')
	}
	defer w.Flush()
}