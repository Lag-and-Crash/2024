#lang racket
(require jni)

;; Construct flag and encryption parameters
(define string "supersecret-")
(set! string (string-append string "flag-was-here"))
(set! string (string-append string "-391391948223-"))
(set! string (string-append string "LVBCS0RGMldpdGhIbWFjU0hBMjU2LQ-"))
(set! string (string-append string "YWpWMk5URnpjekJ3TlRGdVpuVnNJUT09"))

;; This is our native method which will be called from Java
(define (get-name obj)
  (jni-new-string string))

;; Set up the JVM
(current-jni-dump-exceptions? #t)
(define env (get-jni-env))
(current-jni-env env)

;; Register the method
(define encrypt-class (jni-find-class "bnKCbaBDFLAHldhlasdasd"))
(send encrypt-class
      register-natives!
      (list (list "akdnasdadsaahbnidxlakndlasd" "()Ljava/lang/String;" get-name)))

;; Create an instance of the Java object
(define encrypt-ctor (send encrypt-class get-method-id "<init>" "()V"))
(define encrypt (jni-new-object encrypt-class encrypt-ctor))

;; Call the native Java method
(define encrypt-mid (send encrypt-class get-method-id "calkhbscluafudklnkalcs" "()Ljava/lang/String;"))
(define encryption (send encrypt call-method encrypt-mid))

(define out (open-output-file "./output" #:exists 'replace))
(write (send encryption get-chars) out)
(close-output-port out)