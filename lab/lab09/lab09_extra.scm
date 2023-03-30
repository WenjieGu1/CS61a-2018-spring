;; Extra Scheme Questions ;;


; Q5
(define lst
  (cons (cons 1 nil)
    (cons 2
      (cons (cons 3 (cons 4 nil))
        (cons 5 nil))))
)

; Q6
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
  (if (null? lst) nil
  (if (eq? item (car lst)) (remove item (cdr lst))
  (cons (car lst) (remove item (cdr lst)))
  )))


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (if (= 0 (modulo (max a b) (min a b)) (min a b))
    (gcd (min a b) (modulo (max a b) (min a b))))
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
  (if (null? s) nil
    (cons (car s) (no-repeats 
      (filter (lambda x (not= x (car s))) s)
      )))
)

; Q10
(define (substitute s old new)
  (if (null? s) nil
  (if (pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new))
  (if (eq? (car s) old) (cons new (substitute (cdr s) old new))
    (cons (car s) (substitute (cdr s) old new))
))))

; Q11
(define (sub-all s olds news)
  (if (null? s) nil
  (if (equal? s olds) news
  (if (equal? (car s) olds) (cons news (sub-all (cdr s) olds news))
  (if (equal? (cdr s) olds) (cons (sub-all (car s) olds news) news)
  (if (pair? (car s)) (cons (sub-all (car s) olds news) (sub-all (cdr s) olds news))
    (cons (car s) (sub-all (cdr s) olds news))
))))))
