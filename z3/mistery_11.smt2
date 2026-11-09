(define-fun mistery ((x Int)) Bool
  (and
    (> x 1)
    (not (exists ((z Int) (y Int))
      (and (< y x) (< z x) (> y 1) (> z 1) (= x (* y z)))))))
(assert (mistery 11))
(check-sat)
