package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Func1620() {
	w := bufio.NewWriter(os.Stdout)
	r := bufio.NewReader(os.Stdin)

	defer w.Flush()

	var poketmonCnt int
	var problemCnt int
	
	fmt.Fscanf(r, "%d %d\n", &poketmonCnt,&problemCnt)
	poketmonmap := make(map[string]int)
	poketmonList := make([] string,0,poketmonCnt)
	// poketmonPloblemList := make([] string,0,problemCnt)
	for i:=0;i<poketmonCnt;i++ {
		text, _ := r.ReadString('\n')
		text = strings.TrimSuffix(text, "\n")
		poketmonmap[text]	= i+1
		poketmonList = append(poketmonList, text)
	}

	for i:=0;i<problemCnt;i++ {
		text, _ := r.ReadString('\n')
		text = strings.TrimSuffix(text, "\n")
		result, check := isNumber(text)
		if  check {
			fmt.Println(poketmonList[result-1])
		}else{
			fmt.Println(poketmonmap[text])
		}
	}
}


func isNumber(data string) (int, bool) {
	result ,err := strconv.Atoi(data)
	if err != nil {
		return 0,false
	}
	return result,true
}