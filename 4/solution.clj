; largest palindromic number formed by multiplying two 3 digit numbers

(defn num-to-digit-seq [n]
  (if (< n 10)
    (list n)
    (concat (num-to-digit-seq (quot n 10))
            (list (rem n 10)))))

(defn palindrome-seq? [n]
  (and
    (= (first n) (last n))
    (if (< (count n) 4) 
      true
      (palindrome-seq? (rest (butlast n))))))

(defn palindrome? [n]
  (palindrome-seq? (num-to-digit-seq n)))

(def solution (apply max 
  (filter palindrome? 
    (for [n1 (range 100 1000) n2 (range 100 1000)] (* n1 n2)))))

(print solution "\n")
