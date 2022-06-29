# filename should be like test_xyz.py or xyz_test.py
# ex: test_webserver.py
# pytest is a framework

import pytest
import numpy.random as rd
# dependant on assertion


# start all function name with test*() else it wont be considered as test
# this is a test case

def test_one():
  assert 1 == 1, "first test case fail"

def test_two():
  expected = 10
  actual = 20
  assert expected == actual, "second test case fail"

# assert takes two args. boolean expression and a message to display if it fails

def test_three():
  n = rd.randint(1,10)
  count = n + 10
  assert count < 15, "randint tests failed"
