'''
@date Aug 17, 2010
@author: Matthew Todd

This file is part of Test Parser
by Matthew A. Todd

Test Parser is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Test Parser is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.
'''
import unittest
from TestParser.Common.Observable import Observable
from TestParser.View.Text.TextStatisticView import TextStatisticView
from TestParser.View.Text.TextViewController import TextViewController

class Model(Observable):
    def __init__(self, results):
        super().__init__()
        self.results = results
            
class TextStatisticView_Test(unittest.TestCase):
    def test_displayNone(self):
        '''
        Test display code when model doesn't contain any data
        '''
        model = Model(None)
        controller = TextViewController(model)
        TextStatisticView(model, controller)
        
        model.notifyObservers()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()