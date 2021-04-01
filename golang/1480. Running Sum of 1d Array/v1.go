package main

func runningSum(nums []int) []int {
	var current = 0
	var sum []int
	for _, num := range nums{
		current += num
		sum = append(sum, current)
	}
	return sum
}