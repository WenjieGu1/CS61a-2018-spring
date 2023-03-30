(define (find s predicate)
  'YOUR-CODE-HERE
  (cond
    ((null? s) #f)
    ((predicate (car s)) #t)
    (else (find (cdr-stream s) predicate))
      )
)

(define (scale-stream s k)
  'YOUR-CODE-HERE
  (if (null? s) nil
    (cons-stream (* k (car s)) (scale-stream (cdr-stream s) k)))
)

(define (has-cycle s)
  'YOUR-CODE-HERE
  (define i s)
  (define (helper s)
    (cond
      ((null? s) #f)
      ((eq? i s) #t)
      (else (helper (cdr-stream s)))
)))
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
