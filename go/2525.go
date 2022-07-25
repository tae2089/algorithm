package main

import "fmt"

func Func2525(){
	var A int32 //hour
	var B int32 //minute
	var C int32 //minute
	fmt.Scanln(&A,&B)
	fmt.Scanln(&C)
	A = A*60
	total_minutes := A + B + C
	hour := total_minutes / 60
	minute := total_minutes % 60
	fmt.Printf("%d %d",hour % 24,minute)
}