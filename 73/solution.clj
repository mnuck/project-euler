(use '[clojure.contrib.math :only (gcd)])

(defn in-the-band [n]
  (and (< (/ 1 3) n)
       (> (/ 1 2) n)))

(defn reduced-proper-fractions [n]
  (map / (filter #(= 1 (gcd % n)) (range 1 n)) (repeat n)))

(defn banded-fractions [n]
  (filter in-the-band (reduced-proper-fractions n)))

(def solution 
 (count (mapcat banded-fractions (range 2 12001))))

(print solution "\n")
