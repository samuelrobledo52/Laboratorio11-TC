(declare-const a Bool)
(declare-const b Bool)
(define-fun f () Bool
  (= (not (and a b)) (and (not a) (not b))))
(assert (not f))
(check-sat)
(get-model)
