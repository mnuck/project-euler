(ns project-euler.problem5
  (:require [clojure.math.numeric-tower :as math]))

(def solution5
  (reduce math/lcm (range 1 20)))

solution5

; (. javax.swing.JOptionPane (showMessageDialog nil solution5))
