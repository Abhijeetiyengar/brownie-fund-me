from brownie import FundMe, Contract
import json
from scripts.helpful_scripts import get_account


def fund():
    funde_me = FundMe[-1]
    print(funde_me)
    print(funde_me.balance())
    # account = get_account()
    # entrace_fee = funde_me.getEntranceFee()
    # print(entrace_fee)
    # print("Starting funding")
    # funde_me.fund({"from": account, "value": entrace_fee})
    # print("Funding done")
    # balance = funde_me.balance()
    # print(f"balnce of contract is {balance}")


def fund_on_fork():

    f = open('build/contracts/FundMe.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # get abi
    abi = data["abi"]

    # print(abi)
    # Forked address : "0x56924d5417e071df9dD19D8Decbdd0dAf03E346B"
    # Rinkeby : "0x17808565D8B1f4940251576d89a25B5D7e3eCB2d"
    # Local Ganache : "0xE89431ABc14677c815d8aa01Ef22fA06d8d42ddA"

    funde_me = Contract.from_abi("FundMe",
                                 "0x17808565D8B1f4940251576d89a25B5D7e3eCB2d", abi)
    print(funde_me.getVersion())
    print(funde_me.balance())
    account = get_account()
    entrace_fee = funde_me.getEntranceFee()
    print(entrace_fee)
    print("Starting funding")
    funde_me.fund({"from": account, "value": entrace_fee})
    print("Funding done")
    balance = funde_me.balance()
    print(f"balnce of contract is {balance}")


def withdraw():
    funde_me = FundMe[-1]
    funde_me.withdraw({"from": get_account()})
    balance = funde_me.balance()
    print(f"balnce of contract is {balance}")


def main():
    # fund()
    # withdraw()
    fund_on_fork()
