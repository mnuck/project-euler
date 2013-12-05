(ns project-euler.problem9
  (:require [project-euler.core :as pe]))

(def solution9
  (loop [a 1
         b 2]
    (let [c (- 1000 a b)]
      (if (> c 0)
        (if (or (<= c b) (= a b))
          (recur 1 (+ b 1))
          (if (pe/pythagorean-triplet? a b c)
            (* a b c)
            (recur (+ a 1) b)))))))

solution9

; (. javax.swing.JOptionPane (showMessageDialog nil solution9))
