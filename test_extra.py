
#test_xyz.py  or xyz_test.py
import pytest
import time
import os
#Ex: test_extra.py

#each test function should have syntax: "test*()"

env = os.getenv("TYPE")
if(not env):
  env = "DEV"
  
@pytest.mark.skipif(env != "DEV", reason="This is part of dev")
def test_one(): #this function is acting as "test case"
  print("\nEXECUTING >>>>>>>>>>>>>TEST_ONE\n")
  assert 1 == 2


@pytest.mark.skipif(env = "DEV", reason="This is part of dev")
def test_two(): #this function is acting as "test case"
  print("\nEXECUTING >>>>>>>>>>>>>TEST_TWO\n")
  assert 1 == 1
  
@pytest.mark.xfail
def test_three(): #this function is acting as "test case"
  print("\nEXECUTING >>>>>>>>>>>>>TEST_THREE\n")
  assert 1 == 1


def test_four(): #this function is acting as "test case"
  print("\nEXECUTING >>>>>>>>>>>>>TEST_FOUR\n")
  assert 1 == 1


def test_five(): #this function is acting as "test case"
  print("\nEXECUTING >>>>>>>>>>>>>TEST_FIVE\n")
  assert 1 == 2
