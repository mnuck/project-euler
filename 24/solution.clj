; (defn num-to-digit-seq [n]
;   (if (< n 10)
;     (list n)
;     (concat (num-to-digit-seq (quot n 10))
;             (list (rem n 10)))))
; 
; (defn pad-digit-seq [xs n]
;   (if (>= (count xs) n) 
;     xs
;     (recur (cons 0 xs) n)))
; 
; (defn is-permutation? [n x]
;   (let [xs (set (pad-digit-seq (num-to-digit-seq n) x))]
;     (every? #(contains? xs %) (range x))))
; 
; (def permutations (filter #(is-permutation? % 10) (range 123456788 9876543210)))
; 
; (defn split-when [xs ys]
;   (print xs ys)
;   (if (> (first ys) (first (take-last 1 xs)))
;     [xs ys]
;     (split-when (concat xs (list (first ys)) (rest ys)))))
;
; oh hey, clojure-contrib has something

(use 'clojure.contrib.combinatorics)
(print (nth (lex-permutations [0 1 2 3 4 5 6 7 8 9]) 999999) "\n")
