;
; to-da-fifth numbers

(defn num-to-digit-seq [n]
  (if (< n 10)
    (list n)
    (concat (num-to-digit-seq (quot n 10))
            (list (rem n 10)))))

(def to-da-fifth
  (memoize (fn [n]
    (* n n n n n))))

(defn fifther? [n]
  (= n (apply + (map to-da-fifth (num-to-digit-seq n)))))

(def solution
  (apply + (filter fifther? (range 2 2000000))))

(print solution "\n")