package main

func maximumWealth(accounts [][]int) int {
	var maxWealth = 0
	for _, custom := range accounts {
		var customWealth = 0
		for _, bank := range custom {
			customWealth += bank
		}
		if maxWealth < customWealth {
			maxWealth = customWealth
		}
	}
	return maxWealth
}
