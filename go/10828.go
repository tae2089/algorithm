package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)


var (
	w = bufio.NewWriter(os.Stdout)
	r = bufio.NewReader(os.Stdin)
)

type Stack []int


// Pop from stack
func (s *Stack) Pop() int {
	if len(*s) != 0 {
		data := (*s)[len(*s)-1]
		(*s) = (*s)[:len(*s)-1]
		return data
	}
	return -1
}


func(s *Stack) Empty() int{
	if len(*s) == 0 {
		return 1
	}
	return 0
}


func(s *Stack) Size() int{
	return len(*s)
}


func(s *Stack) Top() int{
	if s.Empty() == 1 {
		return -1
	}
	return (*s)[s.Size()-1]
}


func(s *Stack) Push(i int) {
	(*s) = append((*s), i)
}


func Func10828() {

	defer w.Flush()

	var n int
	fmt.Fscanf(r, "%d\n", &n)
	var stack Stack
	
	for i := 0; i < n; i++ {
		text, _ := r.ReadString('\n')
		text = strings.TrimSuffix(text, "\n")
		split := strings.Split(text, " ")
		switch split[0] {
			case "push":
				fmt.Print(11)
			case "pop":
				fmt.Print(22)
			case "empty":
				stack.Empty()
		}
	}
}