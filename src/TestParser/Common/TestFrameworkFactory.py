'''
Because user will only end up using a small portion of the the imports
and we use each import once, we import where its needed. This way if an
user doesn't use an import, we don't waste resources importing it. In
addition, this allows users to avoid having dependencies for the
modules that aren't used. Example: PLY for JUnitParser.

@date Jul 1, 2010
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


class UndefinedTestFrameworkError(Exception):
    '''
    Exception for when we receive a unrecognized Test Framework.
    '''
    def __init__(self, framework):
        self.framework = framework
    def __str__(self):
        return self.framework
    def __repr__(self):
        return str(self)

class TestFrameworkFactory(object):
    '''
    Abstract Factory for test frameworks. Create runners and parsers.
    
    Singleton.
    
    Use:
    @code
    FrameworkFactory.selectFramework(framework)
    FrameworkFactory.createRunner()
    FrameworkFactory.createParser()
    @endcode
    
    @note: Calling a create method when the framework hasn't been selected
    will result in an exception. 
    
    @date Jul 1, 2010
    @author Matthew A. Todd
    '''
    
    ## singleton factory
    factory = None

    @classmethod
    def selectFramework(cls, framework, bFileRunner = False):
        '''
        Select the framework to use.
        
        If we're using a fileRunner, we wrap the decorator around the normal
        factory.
        
        @return the concrete framework factory.
        '''
        if framework.lower() == "Boost".lower():
            cls.factory = _BoostFactory()
        elif framework.lower() == "PyUnittest".lower():
            cls.factory = _PythonUnittestFactory()
        elif framework.lower() == "JUnit".lower():
            cls.factory = _JUnitFactory()
        else:
            raise UndefinedTestFrameworkError(framework)
        
        if bFileRunner:
            cls.factory = _FileRunnerDecorator(cls.factory)
    
    @classmethod
    def createRunner(cls):
        return cls.factory.createRunner()
    
    @classmethod
    def createParser(cls):
        return cls.factory.createParser()

class _FileRunnerDecorator():
    '''
    Allows for the file runner to be used by any test framework.
    
    @date Sep 10, 2010
    '''
    def __init__(self, factory):
        self.factory = factory
    
    def createRunner(self):
        from TestParser.Model.FileRunner import FileRunner
        return FileRunner()
    
    def createParser(self):
        return self.factory.createParser()
    
    
class _BoostFactory():
    def createRunner(self):
        from TestParser.Model.BoostRunner import BoostRunner
        return BoostRunner()
    
    def createParser(self):
        from TestParser.Parser.BoostParser import BoostParser
        return BoostParser()

class _PythonUnittestFactory():
    def createRunner(self):
        from TestParser.Model.PythonUnittestRunner import PythonUnittestRunner
        return PythonUnittestRunner()
    
    def createParser(self):
        from TestParser.Parser.PythonUnittestParser import PythonUnittestParser
        return PythonUnittestParser()
    
class _JUnitFactory():
    def createRunner(self):
        from TestParser.Model.JUnitRunner import JUnitRunner
        return JUnitRunner()
    
    def createParser(self):
        from TestParser.Parser.JUnitParser import JUnitParser
        return JUnitParser()