package main

import "fmt"


func Func8393(){
	var input int
	total := 0
	fmt.Scanln(&input)
	for i:=1; i<=input; i++ {
		total = total + i
	}
	fmt.Print(total)
}