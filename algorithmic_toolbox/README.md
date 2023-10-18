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
