(defn num-to-digit-seq [n]
  (if (< n 10)
    (list n)
    (concat (num-to-digit-seq (quot n 10))
            (list (rem n 10)))))

(defn num-to-binary-seq [n]
  (if (< n 2)
    (list n)
    (concat (num-to-binary-seq (quot n 2))
            (list (rem n 2)))))

(defn palindrome-seq? [n]
  (and
   (= (first n) (last n))
   (if (< (count n) 4) 
     true
     (recur (rest (butlast n))))))

;(defn palindrome-seq? [n]
;(= n (reverse n)))


(defn decimal-palindrome? [n]
  (palindrome-seq? (num-to-digit-seq n)))

(defn binary-palindrome? [n]
  (palindrome-seq? (num-to-binary-seq n)))

(defn double-palindrome? [n]
  (and (decimal-palindrome? n)
       (binary-palindrome? n)))

(time (def solution (apply + (filter double-palindrome? (range 1 1000000)))))

(print solution "\n")
