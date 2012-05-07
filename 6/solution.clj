; difference between the sum of the squares of the first 100 natural numbers
; and the square of the sum of the first 100 natural numbers

(def nums (range 1 101))
(def square-of-sum (let [x (apply + nums)] (* x x)))
(def sum-of-squares (apply + (map #(* % %) nums)))
(def solution (- square-of-sum sum-of-squares))

(print solution "\n")
