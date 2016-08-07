import pytest


@pytest.fixture(autouse=True)
def skip_testrpc_and_wait_for_mining_start(web3_empty,
                                           wait_for_miner_start,
                                           skip_if_testrpc):
    web3 = web3_empty

    skip_if_testrpc(web3)

    wait_for_miner_start(web3)

    assert web3.eth.mining
    assert web3.eth.hashrate
    assert web3.miner.hashrate