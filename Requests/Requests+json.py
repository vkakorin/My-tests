import requests

response = requests.get(
    "https://devgateway.defiyield.app/v2/protocol/Curve?addresses[]=0xd874387ebb001a6b0bea98072f8de05f8965e51e&chains=1,4,6,3,5,7,10")


def test_Status_Code_Equals_200():
    assert response.status_code == 200


def test_Errors_IsEmpty():
    response_body = response.json()
    assert response_body['errors'] == []


def test_Chain_Name():
    response_body = response.json()
    assert response_body['data']['protocol']['chains'][0] == 'eth'


def test_Protocol_TotalVelue():
    response_body = response.json()
    assert response_body['data']['total'] > 0


def test_Stacking_TotalVelue():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['staking']['totalValue'] > 0


def test_Pools_Stats_TVL():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['stats']['tvl'] > 0


def test_Staking_Balance():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['staking']['items'][0]['stakingToken']['tokens'][0][
               'balance'] > 0


def test_Staking_Value():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['staking']['items'][0]['stakingToken']['tokens'][0][
               'value'] > 0


def test_Staking_Price():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['staking']['items'][0]['stakingToken']['tokens'][0][
               'price'] > 0


def test_Staking_Rewards_price():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['staking']['items'][0]['rewards'][0]['price'] > 0


def test_Staking_Rewards_Balance():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['staking']['items'][0]['rewards'][0]['claimableData'][
               'balance'] > 0


def test_Staking_Rewards_Value():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['staking']['items'][0]['rewards'][0]['claimableData'][
               'value'] > 0


def test_Pools_LpToken_Price():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['lpToken']['price'] > 0


def test_Pools_Stats_TVL():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['stats']['tvl'] > 0


def test_Pools_Stats_Share():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['stats']['share'] > 0


def test_Pools_TotalVelue():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['totalValue'] > 0


def test_Pools_FirstTokens_Price():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['tokens'][0]['price'] > 0


def test_Pools_SecondTokens_Price():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['tokens'][1]['price'] > 0


def test_Pools_ThirdTokens_Price():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['tokens'][2]['price'] > 0


def test_Pools_FourthTokens_Price():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['tokens'][3]['price'] > 0


def test_Pools_FirstTokens_Value():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['tokens'][0]['value'] > 0


def test_Pools_SecondTokens_Value():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['tokens'][1]['price'] > 0


def test_Pools_ThirdTokens_Value():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['tokens'][2]['price'] > 0


def test_Pools_FourthTokens_Value():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['tokens'][3]['price'] > 0


def test_Pools_FirstTokens_Balance():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['tokens'][0]['balance'] > 0


def test_Pools_SecondTokens_Balance():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['tokens'][1]['balance'] > 0


def test_Pools_ThirdTokens_Balance():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['tokens'][2]['balance'] > 0


def test_Pools_FourthTokens_Balance():
    response_body = response.json()
    assert response_body['data']['wallets'][0]['chains'][0]['pools']['items'][0]['tokens'][3]['balance'] > 0
