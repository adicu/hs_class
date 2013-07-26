#!/bin/sh

if ! [ -d env ]; then
	virtualenv env
	. env/bin/activate
	pip install pantograph
else
	. env/bin/activate
fi

python main.py
