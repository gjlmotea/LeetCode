package main

func twoSum(nums []int, target int) []int {
	for i, n1 := range nums{
		for j, n2 := range nums{
			if i != j && n1 + n2 == target{
				return []int{i,j}
			}
		}
	}
	return nil
}