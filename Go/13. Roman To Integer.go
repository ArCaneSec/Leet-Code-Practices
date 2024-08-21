package main

import "fmt"

func romanToInt(s string) int {
	romans := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	num := 0

	for i, v := range s {
		if i < len(s) - 1 && romans[v] < romans[rune(s[i+1])] {
				num -= romans[v]
			}else{
				num += romans[v]
			}
	}
	return num
}

func main() {
	fmt.Println(romanToInt("IVMXXL"))
}
