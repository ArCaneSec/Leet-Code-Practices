package main

import "fmt"

func removeDuplicates(nums []int) int {
	prev := nums[0]
	writeIndex := 1
	k := 1

	for _, num := range nums {
		if num != prev{
			nums[writeIndex] = num
			writeIndex += 1
			k += 1
			prev = num
		}
	}

	return k
}

func main() {
	nums := []int{1, 1, 1, 2, 3, 3, 4}
	fmt.Println(removeDuplicates(nums), nums)
}
