(define (fib-even-sum count)
  (fib-iter 1 1 count 0))

(define (fib-iter a b count result)
  (if (> a count)
	result
	(if (even? a)
	  (fib-iter (+ a b) a count (+ a result))
	  (fib-iter (+ a b) a count result))))

;ans
(fib-even-sum 4000000)

