'Q1
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

'Q2
(define (sign x)
  ((> x 0) 1)
  ((< x 0) -1)
  (else 0)
)

'Q3
(define (square x) (* x x))

(define (pow b n)
  (cond
    ((eq? n 1) b)
    ((eq? n 2) (square b))
    ((even? n) (square (pow b (/ n 2))))
    (else (* b (square (pow b (/ (- n 1) 2)))))
))

(define (ordered? s)
  (if (null? (cdr s)) #t
    (if (< (car s) (cadr s)) #f
      (ordered? (cdr s))
)))

(define (nodots s)
  (if (pair? s)
    (cons (car s) (nodots (cdr s)))
    (if (null? s)
      nil
      (cons s nil)))
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          ((< v (car s)) #f)
          ((= v (car s)) #t)
          (else (contains? (cdr s) v)) 
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((= v (car s)) s)
          (else (cons (car s) (add (cdr s) v)))
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((> (car s) (car t)) (intersect s (cdr t)))
          (else (intersect (cdr s) t)) 
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
          ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
          ))
