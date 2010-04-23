'''
@date Apr 23, 2010
@author matcat
'''
from BoostTestParser.Common.Observer import Observer


class Mock_Observer(Observer):
    
    def __init__(self):
        self.notified = False
    
    def update(self):
        self.notified = True
        