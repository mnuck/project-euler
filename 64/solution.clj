;;; Project Euler 64

(defn floor [n]
  (int (Math/floor n)))

(defn f [S sqrS m d a]
  (let [m1 (- (* d a) m)
        d1 (/ (- S (* m1 m1)) d)
        a1 (floor (/ (+ sqrS m1) d1))]
    [m1 d1 a1]))

(defn repeat-length-helper [S sqrS i used m d a]
  (let [result (f S sqrS m d a)]
    (if (contains? used result) i
        (apply repeat-length-helper
               (concat [S sqrS (inc i) (conj used result)] result)))))

(defn repeat-length [S]
  (repeat-length-helper S (Math/sqrt S) 0 (set []) 0 1 (floor (Math/sqrt S))))

(defn square? [n]
  (= n (* (int (Math/sqrt n)) (int (Math/sqrt n)))))

(defn solution []
  (count
   (filter odd? 
           (map repeat-length
                (filter #(not (square? %))
                        (range 1 10001))))))

(time (print (solution) "\n"))

