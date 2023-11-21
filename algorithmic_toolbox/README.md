## [Algorithmic Toolbox](https://www.coursera.org/learn/algorithmic-toolbox?specialization=data-structures-algorithms)

### week2

- Fibonacci

  - recursion
  - list <- faster!　 Avoids redundant calculations by storing and reusing previously computed values.

- Greatest Common Divisor (最大公約数)

  - find answer from 0 <- too slow
  - use euclid

- Big-O Notation

  - Figuing out accurate runtime is a huge mess !
  - Asymptotic Notation : ランダウの漸近記法
    [Big O Notation Cheat Sheet](https://flexiple.com/algorithms/big-o-notation-cheat-sheet)

### week3 　 Greedy algorithm

- Greedy algorithm (貪欲法)

  - a greedy choice is called safe choice if there is an optimal solution consistent with this first choice
  - make some first choice -> solve a pronlem of the same kind -> smaller (like: fewer digits, fewer patients.. etc)
  - such small problems are called subproblem

1. Make a greedy choice
2. Prove that it's a safe choice
3. reduce to a subproblem
4. solve the subproblem

### week4 Divide and Conquer

分割統治は問題を 1 つ以上のサブ問題に分割し、それを個別に解決できるという利点を利用する

- Linear Search 線型探索
  - 前から順番に配列を確認して行く
- Binary Search 二分探索

  - ソート済みである配列から、二分して絞っていき、探索する。より高速
  - 計算量は O(logN)

- Multiply two polynominals

  - https://www.geeksforgeeks.org/multiply-two-polynomials-2/?ref=lbp
  - [カラツバ法](https://qiita.com/square1001/items/1aa12e04934b6e749962#3-2-%E7%94%BB%E6%9C%9F%E7%9A%84%E3%81%AA%E6%8E%9B%E3%81%91%E7%AE%97%E3%81%AE%E6%96%B9%E6%B3%95%E3%82%AB%E3%83%A9%E3%83%84%E3%83%90%E6%B3%95)

- Sort
  - Selction Sort O(n^2)
  - Merge Sort O(nlogn)
    - O(logn) : 再帰的に 2 分割
    - O(n) : 各部分リストを独立にソート。各要素は 1 度だけ比較される
  -
