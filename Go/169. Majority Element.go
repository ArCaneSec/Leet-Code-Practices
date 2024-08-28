package main

import (
	"fmt"
)

func majorityElement(nums []int) int {
	n := len(nums)
	m := make(map[int]int, n)
	for _, val := range nums {
		if _, ok := m[val]; ok {
			m[val] += 1
		} else {
			m[val] = 1
		}
		if m[val] > n / 2{
			return val
		}
	}
	return 0
}

func MajorityElement(nums []int) int {
	var (
		ans = nums[0]
		votes = 1
	)
	for _, val := range nums[1:] {
		if val == ans {
			votes += 1
		}else {
			if votes > 1{
				votes -= 1
			} else {
				ans = val
			}
		}
	}
	return ans
}

func main() {
	fmt.Println(MajorityElement([]int{1,1,2, 2, 3, 1}))
}
