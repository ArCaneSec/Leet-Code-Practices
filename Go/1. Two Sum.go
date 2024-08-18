package main

import (
	"fmt"
	
)

func twoSum(nums []int, target int) []int {
	n_index := 1

	for v_i, v := range nums {
		j_index := n_index
		for _, j := range nums[n_index:] {
			if v+j == target {
				return []int{v_i, j_index}
			}
			j_index += 1
		}
		n_index += 1
		if n_index == len(nums) {
			return nums
		}
	}
	return nums
}
func TwoSum(nums []int, target int) []int {
	hash := make(map[int]int, len(nums))
	var needed_num int 
	for i, v := range nums {
		needed_num = target - v
		if index, ok := hash[needed_num]; ok{
			return []int{i, index}
		}
		hash[v] = i
	}
	return nil
}

func main() {
	fmt.Println(twoSum([]int{1, 2, 3, 5}, 8))
	fmt.Println(TwoSum([]int{3,2,4}, 6))
}
