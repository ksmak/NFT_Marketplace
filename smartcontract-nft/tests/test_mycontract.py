import pytest

from brownie import accounts, SimpleNFT


@pytest.fixture
def token():
    return accounts[0].deploy(SimpleNFT, "MyNFT Marketplace", "MFT")


def test_nft_operations(token):
    # accounts[0] - contract owner
    # accounts[1] - seller
    # accounts[2] - buyer

    token.createArt('xxx', accounts[1], '4 ether',
                    '01.01.2023 00:00:01', 'my art', {'from': accounts[0]})

    arts = token.getAllArts()
    assert arts[0][0] == 0
    assert arts[0][1] == 'xxx'
    assert arts[0][2] == accounts[1]
    assert arts[0][3] == '4 ether'
    assert arts[0][4] == '01.01.2023 00:00:01'
    assert arts[0][5] == 'my art'

    token.sendMoney({'from': accounts[2], 'value': '10 ether'})
    assert token.getBalance() == '10 ether'
    assert token.getBalances(accounts[2]) == '10 ether'

    token.buyArt(accounts[2], 0, '1 ether', {'from': accounts[0]})

    arts = token.getAllArts()
    assert arts[0][0] == 1
    assert arts[0][1] == 'xxx'
    assert arts[0][2] == accounts[2]
    assert arts[0][3] == '4 ether'
    assert arts[0][4] == '01.01.2023 00:00:01'
    assert arts[0][5] == 'my art'

    token.resellArt(0, '5 ether', {'from': accounts[0]})

    arts = token.getAllArts()
    assert arts[0][0] == 0
    assert arts[0][1] == 'xxx'
    assert arts[0][2] == accounts[2]
    assert arts[0][3] == '5 ether'
    assert arts[0][4] == '01.01.2023 00:00:01'
    assert arts[0][5] == 'my art'
