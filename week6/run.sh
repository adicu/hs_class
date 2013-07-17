#!/bin/sh

if ! [ -d env ]; then
	virtualenv env
	. env/bin/activate
	if [ -d pantograph ]; then
		cd pantograph
		git pull
	else
		git clone git@github.com:adicu/pantograph.git
		cd pantograph
	fi
	python setup.py install
	cd ..
else
	. env/bin/activate
fi

python main.py
