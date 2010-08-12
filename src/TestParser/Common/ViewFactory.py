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
    
    Use:
    @code
    ViewFactory.selectFramework(framework)
    ViewFactory.preViewInit()
    ViewFactory.createResultView(model)
    ViewFactory.startApplication()
    @endcode
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
            cls.factory = _QtFramework()
        elif framework == "tkinter":
            cls.factory = _TkinterFramework()
        elif framework == "text":
            cls.factory = _TextFramework()
        else:
            raise UndefinedViewFramework(framework)
    
    @classmethod
    def createResultView(cls, model):
        cls.factory.createResultView(model)
    
    @classmethod
    def createStatisticView(cls):
        cls.factory.createStatisticView()
    
    @classmethod
    def preViewInit(cls):
        '''
        Does any necessary initialization.
        
        Many frameworks require that the a root/application instance be
        created before any windows,widgets,etc. are created. This is where
        the root/application instance will be created
        '''
        cls.factory.preViewInit()
    
    @classmethod
    def startApplication(cls):
        '''
        Starts the actual application.
        
        Note, if the actual implementation needs access to the views that
        have been created, the factory needs to keep track of them. A member
        variable (list or similar) will probably be enough, but the
        create__View will need to make sure to add to this list.
        '''
        cls.factory.startApplication()



class _QtFramework():
    def createResultView(self, model):
        from TestParser.View import QtView
        controller = QtView.QtViewController(model)
        view = QtView.QtView(model, controller)
        view.show()
        
        controller.run()
    
    def createStatisticView(self):
        raise NotImplementedError()
    
    def preViewInit(self):
        import sys
        try:
            from PyQt4 import QtGui #@UnresolvedImport
        except:
            sys.exit("Failed to import PyQt4. QtView needs PyQt4 in order to function. Please install PyQt4 or choose another UI.")
        
        self.app = QtGui.QApplication(sys.argv)    
    
    def startApplication(self):
        import sys
        sys.exit(self.app.exec_())
        
    
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
            