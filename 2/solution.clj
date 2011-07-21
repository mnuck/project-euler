(def fibs (lazy-cat [0 1]
  (map + fibs (rest fibs))))

(def sum [& args]
  (apply + args))

(def solution
  (sum (take-while #(<= % 4000000)
                (filter even? fibs))))

(print solution "\n")
