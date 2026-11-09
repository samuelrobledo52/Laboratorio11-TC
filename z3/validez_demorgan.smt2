(declare-const a Bool)
(declare-const b Bool)
(define-fun demorgan () Bool
  (= (not (and a b)) (or (not a) (not b))))
(assert (not demorgan))
(check-sat)
