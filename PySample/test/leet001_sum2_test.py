'''
Created on 2017-9-3

@author: NiroLN
'''
import unittest
#import pkg
# from pkg.leet001_sum2 import leet001_sum2
from pkg.leet001_sum2 import *


class Test(unittest.TestCase):


    def testName(self):
#         pass
        arr = leet001_sum2().twoSum([2,3,5], 7)
        self.assertEqual(arr, (2,0));


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()