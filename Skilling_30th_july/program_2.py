import pytest

@pytest.mark.parametrize("n,f",[(0,1),(1,1),(2,2),(3,6),(4,6),(5,20)])
def test_fac(n,f):
	assert ret_factorial(n)==f
def ret_factorial(n):
	x = 1
	for i in range(1,n):
		x = x*i
	return x
