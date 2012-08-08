;;; Project Euler 57

(defn root-two-helper [n]
  (if (zero? n) 0
      (/ 1 (+ 2 (root-two-helper (dec n))))))

(defn root-two-approx [n]
  (+ 1 (root-two-helper n)))

(defn longer-numerator [r]
  (> (count (str (numerator r)))
     (count (str (denominator r)))))

(defn solution []
  (count
   (filter #(longer-numerator (root-two-approx %))
           (range 1 1001))))

(time (print (solution) "\n"))
