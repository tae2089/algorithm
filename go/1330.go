package main

import "fmt"

func Func1330() {
	
	var a int32
	var b int32

	fmt.Scanln(&a, &b)

	if a > b {
		fmt.Print(">")
	}else if a < b {
		fmt.Print("<")
	}else{
		fmt.Print("==")
	}
}