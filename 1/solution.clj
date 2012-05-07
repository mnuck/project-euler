; Project Euler #1

(def solution
  (reduce + 
          (set (mapcat #(take-nth % (range 1000)) 
                       [3 5]))))

(. javax.swing.JOptionPane (showMessageDialog nil solution))

