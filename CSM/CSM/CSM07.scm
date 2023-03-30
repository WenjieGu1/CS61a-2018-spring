;1.
;(a) ((1) 2 (3 4 . 5) 6)
;(b) ((1 (2 3 4)) 2 . 3)
;(c) 4
;(d) 0.5
;(e) 4
;(f) Error (g) Error
;(h) boom2 (i) Error
;(j)
(define boom2 (define (boom3) (/ 1 0))) ;unfinished

;2.
;(a) Error	(b) #f  (c)3  (d)0  (e)Error  (f)#f

;3.
((lambda (foo bar) (+ foo bar)) 3 (+ 3 2))

(define (waldo lst)
	(if (null? lst) #f
	(if (eq? (car lst) 'waldo) #t
	(waldo (cdr lst)))))

(define (waldo2 lst)
	(if (null? lst) #f
	(if (eq? (car lst) 'waldo) 0
	(if (waldo2 (cdr lst)) (+ (waldo2 (cdr lst)) 1) #f)
)))

(define (filter fn s)
	(if (null? s) nil
	(if (fn (car s)) (cons (car s) (filter fn (cdr s)))
	(filter fn (cdr s))
)))

(define (quicksort s)
	(if (null? s) nil
	;else
		(append
		(quicksort (filter (lambda (e) (< e (car s))) s))
			(append (list (car s))
				(quicksort (filter (lambda (e) (> e (car s))) s)))
)))