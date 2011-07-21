; Project Euler #32
;
; Find the sum of all products whose multiplicand/multiplier/product
;  identity can be written as a 1 through 9 pandigital.

(defn num-to-digit-seq [n]
  (if (< n 10) (list n)
    (concat (num-to-digit-seq (quot n 10))
            (list (rem n 10)))))

(defn pandigital? [xs]
  (and (= 9 (count xs))
       (= (set xs) #{1 2 3 4 5 6 7 8 9})))

(defn pandigital-product? [x y]
  (pandigital? (mapcat num-to-digit-seq [x y (* x y)])))
