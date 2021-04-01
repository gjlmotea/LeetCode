package main

func v1(candies []int, extraCandies int) []bool {
	// find the max number of candies as threshold
	var threshold = 0
	for _, c := range candies {
		if threshold < c {
			threshold = c
		}
	}

	var b []bool
	for _, c := range candies {
		// compare c+extraCandies to threshold
		if c+extraCandies >= threshold {
			b = append(b, true)
		} else {
			b = append(b, false)
		}
	}
	return b
}
