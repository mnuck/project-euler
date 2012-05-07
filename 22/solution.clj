; Project Euler #22
;
; The only difficulty here is that slurp does some sort of overly helpful
; character escaping, which I had to reverse. The Right Way would be to
; not use slurp.

(use '[clojure.string :only (split escape)])

(def score-map {\A  1 \B  2 \C  3 \D  4 \E  5 \F  6 \G  7 \H  8 \I  9
                \J 10 \K 11 \L 12 \M 13 \N 14 \O 15 \P 16 \Q 17 \R 18
                \S 19 \T 20 \U 21 \V 22 \W 23 \X 24 \Y 25 \Z 26
                \\  0 \"  0})

(def escape-map {\" ""})

(defn score-word [s]
  (if (= 0 (count s)) 0
    (+ (score-map (first s)) (score-word (rest s)))))

(def names
  (sort (map #(escape % escape-map) (split (slurp "names.txt") #"\",\""))))

(defn score-names [xs n]
    (if (= 0 (count xs)) 0
      (+ (* n (score-word (first xs))) 
         (score-names (rest xs) (inc n)))))

(def solution (score-names names 1))

(print solution "\n")
