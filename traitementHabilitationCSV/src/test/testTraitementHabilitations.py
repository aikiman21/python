'''
Created on 21 avr. 2013

@author: Thomas
'''
import unittest
from traitementHabilitations.traitementHabilitations import filtrer

class Test(unittest.TestCase):


    def test_filtrer(self):
        first = 2
        second = 2
        msg = print("test to do")        
        self.assertEqual(first, second, msg)
        #filtrer(srcHabilitations, dstHabilitations, srcHabilitationsEtab, dstHabilitationsEtab)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()