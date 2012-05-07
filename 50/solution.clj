; Project Euler #50
;
; Which prime, below one-million, 
;  can be written as the sum of the most consecutive primes?

(use 'clojure.contrib.lazy-seqs)
(use 'clojure.contrib.seq)

(def small-primes
  (vec (take-while #(< % 1000000) primes)))

(def small-primes-set
  (set (take-while #(< % 1000000) primes)))

(defn prime? [n]
  (contains? small-primes-set n))

(defn consecutive-primes [n]
  (for [i (range (- (inc (count small-primes)) n))]
    (take n (nthnext small-primes i))))

(defn check-length [n]
  (some prime? (for [xs (consecutive-primes n)] (apply + xs))))

(defn report-length [n]
  (apply max (filter prime? (for [xs (consecutive-primes n)] (apply + xs)))))

; (defn max-length-from [n]
;   (loop [usable-primes (nthnext small-primes n) sum 0 i 0]
;     (print sum "\n")
;     (if (not (prime? (+ sum (first usable-primes)))) i
;       (recur (rest usable-primes) (+ sum (first usable-primes)) (inc i)))))
