from pythonisms import __version__

from pythonisms.pythonisems import LinkedList 

import pytest
def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def data():
  list = LinkedList()
  list.insert(3)
  list.insert(8)
  list.insert(5)
  return list



def test_len_of_list(data):
  actual = len(data)
  excepted = 3
  assert actual == excepted
  
def test_dunder_str_method(data):
    
    actual = str(data) 
    expexted ="[5] -> [8] -> [3] -> None"
    assert actual == expexted
def test_dunder_get_item_method_1(data):
    actual = data[0] 
    excepted = 5 
    assert actual == excepted   
def test_dunder_get_item_method_2(data):
    actual = data[1] 
    excepted = 8 
    assert actual == excepted     
def test_dunder_get_item_method_3(data):
    actual = data[2] 
    excepted = 3 
    assert actual == excepted               

def test_dunder_itrate(data):
    expected=[5,8,3]
    for idx, item in enumerate(data):
        assert item==expected[idx]