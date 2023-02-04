#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #A<B
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))
        #A>B
        def test_sample2 (self):
                self.assertEqual (48, calc(8,6))
        #A=0
        def test_sample3 (self):
                self.assertEqual (-1, calc(0,150))
        #B=0
        def test_sample4 (self):
                self.assertEqual (-1, calc(23,0))
        #Bismax
        def test_sample5 (self):
                self.assertEqual (999, calc(1,999))
        #Bis1000
        def test_sample6 (self):
                self.assertEqual (-1, calc(1,1000))
        #B:string
        def test_sample7 (self):
                self.assertEqual (-1, calc(3,'b'))
        #A is not int
        def test_sample8 (self):
                self.assertEqual (-1, calc(0.1,999))