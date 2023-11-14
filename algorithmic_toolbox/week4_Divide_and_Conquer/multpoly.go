package main

import "fmt"

// ex. A(1,2,3), B(3,4,5) -> (x^2 + 2x + 3)(3x^2 + 4x + 5) = 3x^4 + 10x^3 + 22x^2 + 22x + 15
func main() {
	fmt.Println(multPoly(3, []int{1, 2, 3}, []int{3, 4, 5}))
	fmt.Println(karatsubaMultPoly(3, []int{1, 2, 3}, []int{3, 4, 5}))
}

// O(n^2)
func multPoly(n int, a, b []int) []int {
	product := make([]int, 2*n-1)

	for i := 0; i < 2*n-1; i++ {
		product[i] = 0
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			product[i+j] += a[i] * b[j]
		}
	}
	return product
}

// O(n^log2(3))
func karatsubaMultPoly(n int, a, b []int) []int {
	if n <= 1 {
		if n == 0 {
			return []int{}
		}
		return []int{a[0] * b[0]}
	}

	mid := n / 2
	a0, a1 := a[:mid], a[mid:]
	b0, b1 := b[:mid], b[mid:]

	a0b0 := karatsubaMultPoly(mid, a0, b0)
	a1b1 := karatsubaMultPoly(n-mid, a1, b1)

	a0plusa1 := make([]int, mid)
	b0plusb1 := make([]int, mid)
	for i := 0; i < mid; i++ {
		a0plusa1[i] = a0[i] + a1[i]
		b0plusb1[i] = b0[i] + b1[i]
	}

	middle := karatsubaMultPoly(mid, a0plusa1, b0plusb1)

	result := make([]int, 2*n-1)

	for i, v := range a0b0 {
		result[i] += v
	}
	for i, v := range a1b1 {
		result[i+2*mid] += v
	}

	for i := 0; i < len(middle); i++ {
		result[i+mid] += middle[i]
		if i < len(a0b0) {
			result[i+mid] -= a0b0[i]
		}
		if i < len(a1b1) {
			result[i+mid] -= a1b1[i]
		}
	}

	return result
}
