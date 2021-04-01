package main

func kidsWithCandiesV2(candies []int, extraCandies int) []bool {
	var threshold = 0
	for _, c := range candies {
		if threshold < c {
			threshold = c
		}
	}
	threshold -= extraCandies // now we reduce the threshold with extraCandies

	var b []bool
	for _, c := range candies {
		// compare c to threshold
		if c >= threshold {
			b = append(b, true)
		} else {
			b = append(b, false)
		}
	}
	return b
}
