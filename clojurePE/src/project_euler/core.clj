(ns project-euler.core)

(def fibs
  (lazy-cat [0 1]
            (map + fibs (rest fibs))))

(defn max-factor [number]
  (loop [n number factor 2]
    (if (= n factor)
      n
      (if (zero? (mod n factor))
        (recur (/ n factor) factor)
        (recur n (inc factor))))))

(defn num-to-digit-seq [n]
  (if (< n 10)
    (list n)
    (concat (num-to-digit-seq (quot n 10))
            (list (rem n 10)))))

(defn palindrome-seq? [n]
  (and
    (= (first n) (last n))
    (if (< (count n) 4)
      true
      (palindrome-seq? (rest (butlast n))))))

(defn palindrome? [n]
  (palindrome-seq? (num-to-digit-seq n)))

(def prime-certainty 10)
(defn probably-prime? [n]
  (.isProbablePrime (BigInteger/valueOf n) prime-certainty))

(defn pythagorean-triplet? [a b c]
  (= (* c c) (+ (* a a) (* b b))))
