(defn maxfactor [number]
  (loop [n number factor 2]
    (if (= n factor)
      n
      (if (zero? (mod n factor))
        (recur (/ n factor) factor)
        (recur n (inc factor))))))

(def solution (maxfactor 600851475143 2))

(print solution "\n")
