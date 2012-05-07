;
; 0.123456789 10 11 12 13 14 ...
;
; d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
;

(defn num-to-digit-seq [n]
  (if (< n 10) (list n)
    (concat (num-to-digit-seq (quot n 10))
            (list (rem n 10)))))

(defn dee
  ([d] (dee d 1 1))
  ([d i n] ; d = requested index, i = current index, n = current number
    (let [nseq (num-to-digit-seq n)]
      (if (< d (+ i (count nseq)))
        (nth nseq (- d i))
        (recur d (+ i (count nseq)) (inc n))))))

(def solution 
  (* (dee 1) (dee 10) (dee 100) (dee 1000) 
     (dee 10000) (dee 100000) (dee 1000000)))

(print solution "\n")
