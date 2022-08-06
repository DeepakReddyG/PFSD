import pytest
@pytest.mark.parametrize("n,m",[(2,4),(4,16),(5,10),(10,13)]) 

def test_factor(n,m):
	assert m%n==0
