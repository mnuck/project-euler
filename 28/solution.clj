; Project Euler #28
;
; Key insight is that the upper right corner is n^2 for odd n > 1
;  with the other corners being in a mathematical relation to n^2.
;  Factor it out and you get 4n^2 - 6n + 6

(defn outer-edge-sum [n]
  (if (even? n) 0
    (if (= 1 n) 1
      (+ 6 (- (* 4 (* n n)) (* 6 n)))))) ; 4n^2 - 6n + 6

(defn full-spiral-sum [n]
  (reduce + (map outer-edge-sum (range 1 (inc n)))))

(def solution
  (full-spiral-sum 1001))

(print solution "\n")
