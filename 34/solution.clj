;
; factorian numbers

(defn num-to-digit-seq [n]
  (if (< n 10)
    (list n)
    (concat (num-to-digit-seq (quot n 10))
            (list (rem n 10)))))

(def factorial 
  (memoize (fn [n]
  (if (< n 2) 1
    (* n (factorial (dec n)))))))

(defn factorian? [n]
  (= n (apply + (map factorial (num-to-digit-seq n)))))

(def solution
  (apply + (filter factorian? (range 3 50000))))
  
(print solution "\n")
