;;; Project Euler 55

(defn reverse-integer [n]
  "reverse the order of digits in n"
  (BigInteger. (apply str (reverse (str n)))))

(defn palindrome? [n]
  "true if n is the same forward and reverse"
  (= n (reverse-integer n)))

(defn lychrel? [n]
  "true if n is probably a Lychrel number"
  (loop [i 50 x (+ n (reverse-integer n))]
    (if (palindrome? x)
      false
      (if (= i 0)
        true
        (recur (dec i) (+ x (reverse-integer x)))))))

(defn solution [n]
  "the number of positive integers < n that are probably Lychrel numbers"
  (count (filter lychrel? (range 1 n))) "\n")

(time (print (solution 10001)))