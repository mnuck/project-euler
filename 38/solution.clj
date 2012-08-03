;;; Project Euler 38

(defn pandigital-9? [n]
  "A pandigital number contains exactly one each of the digits 1-9"
  (= '(\1 \2 \3 \4 \5 \6 \7 \8 \9)
     (sort (str n))))

(defn generate [i]
  (new Long
       (loop [j 1 current ""]
         (if (< (.length current) 9)
           (recur (inc j) (str current (* i j)))
           current))))

(defn solution [n]
  "Largest pandigital number that can be formed by generate"
  (apply max
         (filter pandigital-9?
                 (map generate (range n)))))

(time (solution 100000))
