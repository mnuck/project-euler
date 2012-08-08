;;; Project Euler 65

(defn lazy-a
  ([]  (lazy-a 2))
  ([n] (lazy-seq (concat [1 n 1] (lazy-a (+ n 2))))))

(defn euler-helper [xs]
  (if (empty? xs) 0
      (/ 1 (+ (first xs)
              (euler-helper (rest xs))))))

(defn euler-approx [n]
  (+ 2 (euler-helper (take (dec n) (lazy-a)))))

(defn digital-sum [n]
  (apply + (map #(Character/getNumericValue %) (str n))))

(defn solution []
  (digital-sum (numerator (euler-approx 100))))

(time (print (solution) "\n"))
