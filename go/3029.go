package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var input1 string
	fmt.Scanln(&input1)
	var input2 string
	fmt.Scanln(&input2)
	n := GetSecond(strings.Split(input1, ":"))
	w := GetSecond(strings.Split(input2, ":"))
	var M int
	if n>=w{
		M =  w - n + 86400
	}else{
		M = w - n
	}
	fmt.Printf("%02d:%02d:%02d",M/3600,M%3600/60,M%3600%60)
}


func GetSecond(input []string)(int){
	h,err := strconv.Atoi(input[0])
	if err != nil {
		panic(err)
	}
	m ,err:= strconv.Atoi(input[1])
	if err != nil {
		panic(err)
	}
	s,err:= strconv.Atoi(input[2])
	if err != nil {
		panic(err)
	}
	return 60*(60*h+m)+s
}