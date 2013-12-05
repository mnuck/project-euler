(ns project-euler.problem10
  (:require [project-euler.core :as pe]))

(def prime? pe/probably-prime?)

(def solution10
  (apply + (take-while #(< % 2000000) (filter prime? (range)))))

solution10

; (. javax.swing.JOptionPane (showMessageDialog nil solution10))
