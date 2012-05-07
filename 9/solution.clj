; a,b,c = {1, 2, 3, ...}
; a < b < c
; a^2 + b^2 = c^2
; a + b + c = 1000
; return abc

(def solution 
  (for [a (range 1 1000)
        b (range 1 1000) 
        c (range 1 1000) 
        :when (and (= 1000 (+ a b c))
                   (< a b c)
                   (= (* c c) (+ (* a a) (* b b))))]
    (* a b c)))

(print solution "\n")
