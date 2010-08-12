'''
Because user will only end up using a small portion of the the imports
and we use each import once, we import where its needed. This way if an
user doesn't use an import, we don't waste resources importing it. In
addition, this allows users to avoid having dependencies for the
modules that aren't used.

@date Aug 12, 2010
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

class UndefinedViewFramework(Exception):
    '''
    Exception for when user gives an unknown ui framework.
    '''
    def __init__(self, framework):
        self.framework= framework
    def __str__(self):
        return "Unknown view framework: %s" % self.framework
    def __repr__(self):
        return self.str()

class ViewFactory():
    '''
    Abstract factory for views. All views will be of same GUI framework.
    
    Singleton
    '''
    
    ## singleton
    factory = None
    
    @classmethod
    def selectFramework(cls, framework):
        '''
        @return The concrete view factory
        '''
        framework = framework.lower()
        if framework == "qt":
            cls.framework = _QtFramework()
        elif framework == "tkinter":
            cls.framework = _TkinterFramework()
        elif framework == "text":
            cls.framework = _TextFramework()
        else:
            raise UndefinedViewFramework(framework)
    
    @classmethod
    def createResultView(cls):
        return cls.factory.createResultView()
    
    @classmethod
    def createStatisticView(cls):
        return cls.factory.createStatisticView()
    
class _QtFramework():
    def createResultView(self):
        pass
    
    def createStatisticView(self):
        pass
    
class _TkinterFramework():
    def createResultView(self):
        pass
    
    def createStatisticView(self):
        pass
    
class _TextFramework():
    def createResultView(self):
        pass
    
    def createStatisticView(self):
        pass
            