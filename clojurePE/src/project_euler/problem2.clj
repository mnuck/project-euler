(ns project-euler.problem2
  (:require [project-euler.core :as pe]))

(time
 (def solution2
   (reduce + (take-while #(<= % 4000000)
                         (filter even? pe/fibs)))))

(print solution2 "\n")

; (. javax.swing.JOptionPane (showMessageDialog nil solution1))
