(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n) (accumulate combiner start (- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
  (define (tail result n)
    (if (= n 0) (combiner start result)
      (tail (combiner result (term n)) (- n 1))))
  (tail (term n) (- n 1))
)

(define-macro (list-of expr for var in seq if filter-fn)
  ;implements list comprehensions, the if condition is optional
  (map (lambda (,var) ,expr) (filter (lambda (,var) ,filter-fn) ,seq))
)
