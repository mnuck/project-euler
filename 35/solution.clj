(use 'clojure.contrib.lazy-seqs)
(use 'clojure.contrib.seq)

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

(print "Generating Primes...\n")
(def small-primes 
  (set (take-while #(< % 1000000) primes)))

(defn prime? [n]
  (contains? small-primes n))

(defn circular-prime? [n]
  (let [xs (num-to-digit-seq n)]
    (every? prime? (map digit-seq-to-num (rotations xs)))))

(def circular-primes
  (filter circular-prime? small-primes))

(print "Counting circular primes...\n")
(def solution 
  (count (filter circular-prime? (range 1 1000000))))

(print solution "\n")
