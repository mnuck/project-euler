;;; Project Euler 16
;;; Sum of the digits of 2 ** 1000
(ns project-euler.problem16
  (:require [clojure.math.numeric-tower :as math]
            [project-euler.core :as pe]))

(def bignum (math/expt 2 1000))
(def bignumseq (pe/num-to-digit-seq bignum))

(time
 (def solution16
   (int (apply + bignumseq))))

(print solution16 "\n")

; (. javax.swing.JOptionPane (showMessageDialog nil solution10))
