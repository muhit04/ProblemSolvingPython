import pytest
from check_valid_ip import IpAddrValidator


def test_char_in_ipv4():
    i = IpAddrValidator('128.A.0.255')
    assert i.check_ipv4() == False

def test_valid_ipv4():
    i = IpAddrValidator('10.0.0.1')
    assert i.check_ipv4() == True

def test_more_octact_ipv4():
    i = IpAddrValidator('128.A.0.255.54')
    assert i.check_ipv4() == False

def test_invalid_char_ipv4():
    i = IpAddrValidator('$.103.255')
    assert i.check_ipv4() == False

def test_valid_ipv6():
    i = IpAddrValidator('1200:0000:AB00:1234:0000:2552:7777:1313')
    assert i.check_ipv6() == True

def test_invalid_format_ipv6():
    i = IpAddrValidator('1200:0000:AB00:1234:::7777:1313')
    assert i.check_ipv6() == False