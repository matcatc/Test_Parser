'''
@date Jul 1, 2010
@author Matthew A. Todd
'''

from TestParser.Parser import BoostParser, PythonUnittestParser
from TestParser.Model import BoostRunner, PythonUnittestRunner

class UndefinedTestFrameworkError(Exception):
    pass

class FrameworkFactory(object):
    '''
    Abstract Factory for test frameworks.
    @date Jul 1, 2010
    @author Matthew A. Todd
    '''

    @staticmethod
    def selectFramework(framework):
        '''
        Select the framework to use.
        
        @return the concrete framework factory.
        '''
        if framework.lower() == "Boost".lower():
            return BoostFactory()
        elif framework.lower() == "PyUnittest".lower():
            return PythonUnittestFactory()
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
    
class BoostFactory(FrameworkFactory):
    def createRunner(self):
        return BoostRunner.BoostRunner()
    
    def createParser(self):
        return BoostParser.BoostParser()

class PythonUnittestFactory(FrameworkFactory):
    def createRunner(self):
        return PythonUnittestRunner.PythonUnittestRunner()
    
    def createParser(self):
        return PythonUnittestParser.PythonUnittestParser()