package main

import (
	"fmt"
	"slices"
)

func longestCommonPrefix(strs []string) string {
	prefix := strs[0]
	var pIndex int
	for _, val := range strs[1:] {
		pIndex = 0
		for index, char := range val {
			if index <= len(prefix)-1 && prefix[index] == byte(char) {
				pIndex += 1
			} else {
				break
			}
		}
		prefix = prefix[:pIndex]
		if prefix == "" {
			return ""
		}
	}
	return prefix
}

func longestCommonPrefixSorted(s []string) string{
	slices.Sort(s)
	first := s[0]
	last := s[len(s) -1]
	readUntil := 0
	for index, val := range first{
		if last[index] == byte(val){
			readUntil += 1
		}
	}
	return first[:readUntil]
}

func main() {
	fmt.Println(longestCommonPrefix([]string{"flower","flower","flower", "flower"}))
	fmt.Println(longestCommonPrefixSorted([]string{"flower","flower","flower", "flower"}))
}
