;
; truncatable primes
;

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
  (take-while #(< % 1000000) primes))
  
(def small-primes-set
  (set small-primes))

(defn prime? [n]
  (contains? small-primes-set n))

(defn rip-leftmost [n]
  (digit-seq-to-num (rest (num-to-digit-seq n))))

(defn left-truncatable? [n]
  (if (< n 10)
    (prime? n)
    (and (prime? n) (left-truncatable? (rip-leftmost n)))))

(defn right-truncatable? [n]
  (if (< n 10)
    (prime? n)
    (and (prime? n) (right-truncatable? (quot n 10)))))

(defn truncatable? [n]
  (and (right-truncatable? n) (left-truncatable? n)))

; first 4 small primes are ineligible to be truncatable
(def solution
  (apply + (filter truncatable? (nthnext small-primes 4))))

(print solution "\n")
