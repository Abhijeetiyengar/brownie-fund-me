# Add a new network : brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=1337
# Add a main net forknetwork : brownie networks add development mainnet-fork-dev fork=https://eth-mainnet.alchemyapi.io/v2/epTLbjAwORLNGGX2QSyDiYb4Z9iS_xzN host=http://127.0.0.1 cmd=ganache-cli accounts=10 mnemonic=brownie port=7545

from brownie import accounts, config, network, MockV3Aggregator

LOCAL_FORKED_NETWORKS = ["mainnet-fork-dev"]
LOCAL_NETWORKS = ["ganache-local", "development"]


def get_account():
    if (network.show_active() in LOCAL_NETWORKS or network.show_active() in LOCAL_FORKED_NETWORKS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def get_price_feed_account():
    if (network.show_active() not in LOCAL_NETWORKS):
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        mock_aggregator = MockV3Aggregator.deploy(8, 200000000000, {
            "from": get_account()})
        return mock_aggregator.address
