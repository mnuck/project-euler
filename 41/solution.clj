; Project Euler #41
;
; Largest pandigital prime

(use 'clojure.contrib.lazy-seqs)
(use 'clojure.contrib.seq)

(defn num-to-digit-seq [n]
  (if (< n 10) (list n)
    (concat (num-to-digit-seq (quot n 10))
            (list (rem n 10)))))

(defn pandigital-seq? [xs n]
  (and (= n (count xs))
       (= (set xs) (set (range 1 (inc n))))))

(defn pandigital-num? [n] 
  (let [xs (num-to-digit-seq n)]
    (pandigital-seq? xs (count xs))))

(def pandigital-primes
  (filter pandigital-num? primes))

(def solution 
  (nth pandigital-primes 537))

(print solution "\n")
