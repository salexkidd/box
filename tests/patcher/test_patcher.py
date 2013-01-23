import unittest
from lib31.patcher import Patcher

#Fixtures
VAR = 'var'
DICT = {'value': 'dict'}
CLASS = type('CLASS', (object,), {'value': 'class'})

#Tests
class PatcherTest(unittest.TestCase):  
    
    BUFFER = {
        'var': VAR,
        'dict': DICT['value'],
        'class': CLASS.value,
    }
    
    def setUp(self):
        self.patcher = Patcher(globals())
            
    def test(self):
        #Patch
        self.patcher.patch({
            'VAR': False,
            'DICT["value"]': False,
            'CLASS.value': False, 
        })
        self.assertEqual(VAR, False)
        self.assertEqual(DICT['value'], False)
        self.assertEqual(CLASS.value, False)
        #Restore
        self.patcher.restore()
        self.assertEqual(VAR, self.BUFFER['var'])
        self.assertEqual(DICT['value'], self.BUFFER['dict'])
        self.assertEqual(CLASS.value, self.BUFFER['class'])        