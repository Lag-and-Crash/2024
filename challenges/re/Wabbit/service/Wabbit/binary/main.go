package main

import (
	"fmt"
	"math/rand"
)

func getFlag() {
	chars := []int{84, 69, 53, 68, 77, 106, 82, 55, 90, 122, 66, 102, 100, 122, 82, 122, 98, 86, 57, 121, 77, 51, 89, 122, 99, 110, 77, 48, 98, 70, 56, 120, 98, 108, 57, 51, 77, 50, 74, 102, 89, 122, 66, 117, 100, 68, 81, 120, 98, 106, 78, 121, 99, 49, 56, 53, 79, 71, 70, 53, 89, 50, 100, 104, 90, 72, 48, 61}

	for i := 0; i < len(chars); i++ {
		fmt.Print(string(chars[i]))
	}
}

func main() {
	if rand.Float64() == 2 {
		getFlag()
	}

	fmt.Println("Go have fun! ;)")
}
