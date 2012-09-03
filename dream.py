#! /usr/bin/env dreamthon
import os
import time


trash = (*files, trash_dir:'~/.Trash') ->
    files.each (f) ->
        to = os.join trash_dir, os.split(f)[-1] + '.' + time.now.iso
        print "{f} -> {to}"
        os.mv f, to 

(= trash (-> (*files trash_dir:'~/.Trash')
    (files .each (-> (f)
        (= to (os .join trash_dir (+ ((os .split f) -1) '.' (time .now .iso))))
        (print "{f} -> {to}")
        (os .mv f to)))))

main = -> trash *os.argv[1:]
