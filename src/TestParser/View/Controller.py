'''
@date Mar 22, 2010
@author Matthew A. Todd

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

from ..Common import Observer

class Controller(Observer.Observer):
    '''
    Our common-basic controller.

    Doesn't do anything with updates.
    Doesn't use any threading.
    If we were to use threading, we'd have to make sure to
    spawn a non daemonic thread.
    @see TestParser.Observable.Observable.notifyObservers()
    '''
    def __init__(self, model):
        '''
        Constructor
        '''
        self.model = model
        self.model.registerObserver(self)
    
    def update(self):
        '''
        Nothing for our controller to do when model updates us
        '''
        pass
    
    def run(self):
        '''
        Simply tells the model to parse
        
        @see Model.runAll()
        '''
        self.model.runAll()
        
