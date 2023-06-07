#!/bin/bash

main () {

	ls -lR | grep $1 | less;
}

main "$@" 
