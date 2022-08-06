import pytest 
@pytest.mark.parametrize("num,sum",[(1,1),(2,3),(3,6),(4,10)])
def test_natural_numbers_sum(num,sum):
	assert num*((num+1)/2) == sum

