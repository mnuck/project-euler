(ns project-euler.problem4
  (:require [project-euler.core :as pe]))

(def solution4 (apply max
  (filter pe/palindrome?
    (for [n1 (range 100 1000) n2 (range 100 1000)]
      (* n1 n2)))))

solution4

; (. javax.swing.JOptionPane (showMessageDialog nil solution4))
