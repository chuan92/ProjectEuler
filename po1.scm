#!/usr/bin/guile
!#

;If we list all the natural numbers below 10 that are multiples of 3 or 5
;we get 3, 5, 6 and 9. The sum of these multiples is 23.
;Find the sum of all the multiples of 3 or 5 below 1000.
;
;
(define (sum term a next b)
 (if (> a b)
	 0
	 (+ (term a)
	    (sum term (next a) next b))))

(define (multiples? a)
		(cond ((= (remainder a 5) 0) a)
			  ((= (remainder a 3) 0) a)
			  (else 0)))

;ans
(sum multiples? 1 (lambda (x) (+ 1 x)) 999)

