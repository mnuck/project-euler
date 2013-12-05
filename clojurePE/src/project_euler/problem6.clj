(ns project-euler.problem6)

(def nums (range 1 101))
(def square-of-sum (let [x (apply + nums)] (* x x)))
(def sum-of-squares (apply + (map #(* % %) nums)))

(def solution6 (- square-of-sum sum-of-squares))

solution6

; (. javax.swing.JOptionPane (showMessageDialog nil solution6))
