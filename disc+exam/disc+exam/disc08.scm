; Write a tail recursive function that returns the nth fibonacci number. We define
;fib(0) = 0 and fib(1) = 1.
(define (fib n)
	(define (fib-sofar n x total1 total2)
		(cond 
			((= x n) total1)
			(else (define a (+ total1 total2)) (define total1 total2) (define total2 a)
				(fib-sofar n (+ x 1) total1 total2)
			)))
(fib-sofar n 0 0 1)
)

; Write a tail recursive function that takes in a Scheme list and returns the numerical
;sum of all values in the list. You can assume that the list is well-formed and contains
;only numbers (no nested lists).
(define (sum lst)
	(define (sum-tail lst result)
	(if (null? lst) result
		(sum-tail (cdr lst) (+ (car lst) result))))
(sum-tail lst 0))

;Write a tail recursive function that takes in a number and a sorted list. The function
;returns a sorted copy with the number inserted in the correct position.

;(a) Begin by writing a tail recursive function that reverses a list.
(define (reverse lst)
	(define (reverse-sofar lst lst-sofar)
		(if (null? lst) lst-sofar
			(reverse-sofar (cdr lst) (cons (car lst) lst-sofar))))
(reverse-sofar lst nil))

;(b) Next, write a tail recursive function that concatenates two lists together.
(define (append a b)
	(define (rev-append-tail a b)
		(if (null? a) b
			(rev-append-tail (cdr a) (cons (car a) b))
			))
(rev-append-tail (reverse a) b))

;(c) Finally, implement insert. You may use reverse and append.
(define (insert n lst)
	(define (rev-insert lst rev-lst)
		(cond ((null? lst) (reverse (cons n rev-lst)) )
			((> (car lst) n) (append (reverse rev-lst) (cons n lst)) )
			(else (rev-insert (cdr lst) (cons (car lst) rev-lst)) )))
 (rev-insert lst nil))