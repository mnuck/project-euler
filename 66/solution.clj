;;; Project Euler 65

(defn continued-fraction-helper [xs]
  (if (empty? xs) 0
      (/ 1 (+ (first xs)
              (continued-fraction-helper (rest xs))))))

(defn continued-fraction [xs]
  (+ (first xs)
     (continued-fraction-helper (rest xs))))

(defn continuation-finder [n ir]
  (if (zero? n) '()
    (cons (int ir)
          (continuation-finder (dec n)
                               (/ 1 (- ir (int ir)))))))

(defn floor [n]
  (int (Math/floor n)))

(defn cont-of-sqrt
  ([i S]
     (let [sqrS (Math/sqrt S)]    
       (cont-of-sqrt i S sqrS
                     0 1 (floor sqrS))))
  ([i S sqrS m d a]
     (if (zero? i) []
         (let [m1 (- (* d a) m)
               d1 (/ (- S (* m1 m1)) d)
               a1 (floor (/ (+ sqrS m1) d1))]
           (concat [a]
                   (cont-of-sqrt (dec i) S sqrS m1 d1 a1))))))

(defn diophantine-solution? [x y D]
  (= 1 (- (* x x) (* y y D))))

(defn check-diophantine [n D]
  (let [r (continued-fraction (cont-of-sqrt n D))
        n (if (ratio? r) (numerator r) r)
        d (if (ratio? r) (denominator r) 1)]
    (if (diophantine-solution? n d D)
      n
      false)))

(defn find-diophantine-min-x [D]
  (loop [n 2
         result (check-diophantine n D)]
    (if result
      [result D]
      (recur (inc n) (check-diophantine (inc n) D)))))

(defn square? [n]
  (= n (* (int (Math/sqrt n)) (int (Math/sqrt n)))))

(defn solution []
  (apply max-key
         (cons first 
               (map find-diophantine-min-x
                    (filter #(not (square? %)) (range 1 1000))))))

(time (print (solution) "\n"))
