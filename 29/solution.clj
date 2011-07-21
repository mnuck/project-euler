(use '(clojure.contrib.math expt))

(def solution 
  (count (set (for [a (range 2 101) b (range 2 101)] (expt a b)))))

(print solution "\n")

