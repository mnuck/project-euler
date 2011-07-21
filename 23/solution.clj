(def proper-divisors (fn [n]
  (filter #(zero? (mod n %))(range 1 n))))

(def abundant? (memoize (fn [n]
  (> (apply + (proper-divisors n)) n))))

(def abundants
  (apply hash-set 
    (filter abundant? (range 1 28124))))

(defn has-no-abundant-sum? [n]
  (not-any? #(contains? abundants (- n %)) abundants))

(def solution
  (apply + (filter has-no-abundant-sum? (range 1 28124))))

(print solution "\n")
