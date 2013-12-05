;;; Project Euler 1
;;; Sum of the multiples of 3 or 5 less than 1000
(ns project-euler.problem1)

(defn fives [n]
  (= 0 (mod n 5)))

(defn threes [n]
  (= 0 (mod n 3)))

(defn matching [n]
  (or (fives n)
      (threes n)))

(time
 (def solution1
   (apply + (filter matching (range 1000)))))

(print solution1 "\n")

; (. javax.swing.JOptionPane (showMessageDialog nil solution1))
