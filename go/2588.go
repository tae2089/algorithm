package main

import (
	"fmt"
	"strings"
)

func main()  {
	var input1 int32
	fmt.Scanln(&input1)
	var input2 string
	fmt.Scanln(&input2)
	input2s := strings.Split(input2, "")
	// for i := len(input2s)-1; 0 <= i; i--{
	// 	input2sIndexValue ,err := strconv.Atoi(string(input2s[i]))
	// 	if err != nil {
	// 		panic(err)
	// 	}
	// 	fmt.Println(input2CharArrayIntValue*int(input1))
	// }
	// input2IntValue, err := strconv.Atoi(input2)
	// if err != nil{
	// 	panic(err)
	// }
	// fmt.Println(input1*int32(input2IntValue))
}