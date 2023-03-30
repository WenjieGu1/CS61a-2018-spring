; Q1
(define (compose-all funcs)
  (if (eq? (cdr funcs) nil) (car funcs) 
    (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))
)))

; Q2
(define (tail-replicate x n)
  (define (helper n a)
    (if (eq? n 1) a
      (helper (- n 1) (cons x a))
      ))
  (helper n (list x))
)
