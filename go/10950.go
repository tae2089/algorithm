package main

import "fmt"

func main() {
	var testCase int
	fmt.Scanln(&testCase)
	
	for i:=0; i<testCase; i++ {
		var a int
		var b int
		fmt.Scanln(&a, &b)
		fmt.Printf("%d\n",a+b)
	}
}