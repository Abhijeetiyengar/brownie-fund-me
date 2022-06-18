from brownie import FundMe
from scripts.helpful_scripts import get_account, get_price_feed_account


def deploy_fund_me():
    account = get_account()

    funde_me = FundMe.deploy(
        get_price_feed_account(), {'from': account})
    print(funde_me.address)


def main():
    deploy_fund_me()
