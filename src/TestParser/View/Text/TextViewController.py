'''
@date Aug 16, 2010
@author matcat

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

from .. import  Controller

class TextViewController(Controller.Controller):
    '''
    A simple controller for TextResultView.
    
    Because all/most of the text views don't need to override
    anything, we're going to just have one main controller for all
    text based views.
    
    Nothing to override
    @see Controller.Controller
    '''