
from myLBproject.lib import sum, who_am_i



def test_sum():
    assert sum(2, 4) == 6



def test_whoami():

    res = who_am_i()

    assert "Leonor" in res.split()