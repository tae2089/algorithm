package main

import "fmt"

func Func2739(){
	var input int
	fmt.Scanln(&input)

	for i := 1; i < 10; i++{
		fmt.Printf("%d * %d = %d\n",input, i, input * i)
	}
}