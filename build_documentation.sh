#!/bin/bash

# This file is part of Test Parser
# by Matthew A. Todd
#
# Test Parser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Test Parser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.

# file is used to build all of Test Parser's documentation.
# Used by setup.py

echo "building doxygen documentation"
cd doc
doxygen doxygen.Doxyfile

echo "building docbook documentation"
cd docbook
xmlto html -m config.xsl manual.dbk
mv index.html manual.html

xmlto html -m config.xsl technical.dbk
mv index.html technical.html

xmlto html -m config.xsl screenshots.dbk
mv index.html screenshots.html