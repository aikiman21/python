'''
Created on 22 avr. 2013

@author: 5936005
'''
import unittest
from main import lireConf


class Test(unittest.TestCase):


    def testlireConf(self):
        racine, fichierHabilitation, fichierHabilitationEtablissemet = lireConf()
        print(racine, fichierHabilitation, fichierHabilitationEtablissemet)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testlireConf']
    unittest.main()