'''
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

from TestParser.Parser import BoostParser, PythonUnittestParser, JUnitParser
from TestParser.Model import BoostRunner, PythonUnittestRunner, JUnitRunner

class UndefinedTestFrameworkError(Exception):
    '''
    Exception for when we receive a unrecognized Test Framework.
    '''
    pass

class FrameworkFactory(object):
    '''
    Abstract Factory for test frameworks.
    
    Singleton.
    
    
    @date Jul 1, 2010
    @author Matthew A. Todd
    '''
    
    ## singleton factory
    factory = None

    @classmethod
    def selectFramework(cls, framework):
        '''
        Select the framework to use.
        
        @return the concrete framework factory.
        '''
        if framework.lower() == "Boost".lower():
            cls.factory = _BoostFactory()
        elif framework.lower() == "PyUnittest".lower():
            cls.factory = _PythonUnittestFactory()
        elif framework.lower() == "JUnit4".lower():
            cls.factory = _JUnitFactory(4)
        elif framework.lower() == "JUnit3".lower():
            cls.factory = _JUnitFactory(3)
        else:
            raise UndefinedTestFrameworkError()

    def __init__(self):
        '''
        Constructor
        '''
    
    def createRunner(self):
        raise NotImplementedError
    
    def createParser(self):
        raise NotImplementedError
    
class _BoostFactory(FrameworkFactory):
    def createRunner(self):
        return BoostRunner.BoostRunner()
    
    def createParser(self):
        return BoostParser.BoostParser()

class _PythonUnittestFactory(FrameworkFactory):
    def createRunner(self):
        return PythonUnittestRunner.PythonUnittestRunner()
    
    def createParser(self):
        return PythonUnittestParser.PythonUnittestParser()
    
class _JUnitFactory(FrameworkFactory):
    def __init__(self, version):
        self.version = version
    def createRunner(self):
        return JUnitRunner.JUnitRunner(self.version)
    def createParser(self):
        return JUnitParser.JUnitParser(self.version)