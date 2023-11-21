package main

import "fmt"


func main(){
	list := []int{2, 3, 9, 1, 4, 5, 7, 8, 6}
	selectionSort(list)
	fmt.Println(list)

    list2 := []int{2, 3, 9, 1, 4, 5, 7, 8, 6}
    fmt.Printf("mergesort:")
    fmt.Println(margeSort(list2))
}

//O(n^2)
func selectionSort(a []int) []int {
    for i := 0; i < len(a); i++ {
        min := i
        for j := i + 1; j < len(a); j++ {
            if a[j] < a[min] {
                min = j
            }
        }
        a[i], a[min] = a[min], a[i]
        //fmt.Printf("i: %d, min: %d, a: %v\n", i, min, a)
    }
    return a
}


//O(nlogn)
func margeSort(a []int) []int {
    if len(a) == 1 {
        return a
    }
    m := len(a) / 2
    return merge(margeSort(a[:m]), margeSort(a[m:]))
}

func merge(a, b []int) []int {
    x := make([]int, 0, len(a)+len(b))
    // aとbが空でない間繰り返す
    for len(a) > 0 && len(b) > 0 {
        if a[0] <= b[0] {
            x = append(x, a[0])
            a = a[1:]
        } else {
            x = append(x, b[0])
            b = b[1:]
        }
    }
    // aが空になったらbをxに追加
    if len(a) == 0 {
        x = append(x, b...)
    }

    if len(b) == 0 {
        x = append(x, a...)
    }
    return x

}
