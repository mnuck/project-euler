; 10001st prime number

(defn prime? [n]
  (and (> n 1) 
       (not-any? #(zero? (mod n %)) 
                 (range 2 (quot n 2)))))

(def solution
  (nth (filter prime? (range)) 10001))

(print solution "\n")