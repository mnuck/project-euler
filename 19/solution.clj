;
; Project Euler #19
;
; This is terrible.

(def weekdays { 0 :sunday
                1 :monday
                2 :tuesday
                3 :wednesday
                4 :thursday
                5 :friday
                6 :saturday })

(def months { :january    0
              :february   1
              :march      2
              :april      3
              :may        4
              :june       5
              :july       6
              :august     7
              :september  8
              :october    9
              :november  10
              :december  11})

(def days-in { :january   31
               :march     31
               :april     30
               :may       31
               :june      30
               :july      31
               :august    31
               :september 30
               :october   31
               :november  30
               :december  31})

(defn leap-year? [year]
  (if (not (zero? (mod year 4))) false
    (if (zero? (mod year 400))   true
      (if (zero? (mod year 100)) false
                                 true))))

(defn days-in-month [month year]
  (if (= month :february)
    (if (leap-year? year) 29 28)
    (days-in month)))

(defn days-in-year [year]
  (if (leap-year? year) 366 365))

(defn day-of-year [day month year]
  (+ day (reduce + (map days-in-month 
    (keys (select-keys months (for [[k v] months :when (< v (months month))] k)))
    (repeat year)))))

(defn days-since-epoch [day month year]
  (+ (day-of-year day month year)
    (reduce + (map days-in-year (range 1900 year)))))

(defn day-of-week [day month year]
  (weekdays (mod (days-since-epoch day month year) 7)))

(def solution 
  (count (filter #(= % :sunday) 
    (for [month (keys months) year (range 1901 2001)] 
      (day-of-week 1 month year)))))

(print solution "\n")
