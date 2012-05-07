(use 'clojure.contrib.math)

(def solution
  (mod (apply + (map #(expt % %) (range 1 1001))) 10000000000))

(print solution "\n")
