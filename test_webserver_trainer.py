
#test_xyz.py  or xyz_test.py
import pytest
import time
import requests
import json

#Ex: test_webserver.py

#each test function should have syntax: "test*()"

def add_user(new_user, new_passwd):
  resp = requests.get(f"http://192.168.29.250:9999/user/add/{new_user}/{new_passwd}")
  reply = resp.content.decode()
  print("REPLY:", reply)
  reply = json.loads(reply)
  return reply["status"]


@pytest.mark.dev
@pytest.mark.unit
def test_one(): #this function is acting as "test case"
  assert 1 == 2

@pytest.mark.dev
def test_two(): #this function is acting as "test case"
  assert 1 == 1
  
@pytest.mark.stage
@pytest.mark.unit
def test_three(): #this function is acting as "test case"
  assert 1 == 2

@pytest.mark.stage
def test_four(): #this function is acting as "test case"
  assert 1 == 1

@pytest.mark.prod
def test_five(): #this function is acting as "test case"
  assert 1 == 1 
