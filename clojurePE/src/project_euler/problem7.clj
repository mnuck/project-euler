(ns project-euler.problem7
  (:require [project-euler.core :as pe]))

(def prime? pe/probably-prime?)

(def solution7
  (nth (filter prime? (range)) 10001))

solution7

; (. javax.swing.JOptionPane (showMessageDialog nil solution7))
