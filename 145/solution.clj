(defn num-to-digit-seq [n]
  (if (< n 10)
    (list n)
    (concat (num-to-digit-seq (quot n 10))
            (list (rem n 10)))))

(defn digit-seq-to-num
  ([xs] (digit-seq-to-num 0 xs))
  ([n xs]
    (if (= 0 (count xs)) n
      (digit-seq-to-num (+ (* n 10) (first xs)) (rest xs)))))

(defn reverse-num [n]
  (digit-seq-to-num (reverse (num-to-digit-seq n))))

(defn euler-reversible? [#^Integer n]
  (and
    (> (mod n 10) 0)
    (every? odd? (num-to-digit-seq (+ n (reverse-num n))))))

(def solution 
  (count (filter euler-reversible? (range 10000000 100000000))))

(print solution "\n")

; 100 -           20  2 digits - 20
; 1000 -         120  3 digits - 100
; 10000 -        720  4 digits - 600
; 100000 -       720  5 digits - ZERO
; 1000000 -    18720  6 digits - 18000
; 10000000 -   68720  7 digits - 50000
; 100000000 -         8 digits -
; 1000000000 -        9 digits - 
; 
; 1 3 5 7 9
; 
