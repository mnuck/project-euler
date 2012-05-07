; sum of all primes less than 2 million

(defn prime? [n]
  (and (> n 1) 
       (not-any? #(zero? (mod n %)) 
                 (range 2 (quot n 2)))))

(def solution
  (apply + (take-while #(< % 2000000) (filter prime? (range)))))

(print solution "\n")
