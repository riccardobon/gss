#!/bin/bash

rm .htmlcov/* .coverage -f
nosetests -vs --rednose --with-coverage --cover-html --cover-html-dir=htmlcov_nose --cover-erase --cover-package=gss_module

exit 0
