#!/bin/bash

# file is used to build all of Test Parser's documentation.
# Used by setup.py

echo "building doxygen documentation"
cd doc
doxygen doxygen.Doxyfile

echo "building docbook documentation"
cd docbook
xmlto html -m config.xsl manual.dbk