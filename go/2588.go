package main

import (
	"fmt"
	"strconv"
)

func main()  {
	var input1 int32
	fmt.Scanln(&input1)
	var input2 string
	fmt.Scanln(&input2)
	input2CharArray := []rune(input2)
	for i := len(input2CharArray)-1; 0 <= i; i--{
		input2CharArrayIntValue,err := strconv.Atoi(string(input2CharArray[i]))
		if err != nil {
			panic(err)
		}
		fmt.Println(input2CharArrayIntValue*int(input1))
	}
	input2IntValue, err := strconv.Atoi(input2)
	if err != nil{
		panic(err)
	}
	fmt.Println(input1*int32(input2IntValue))
}