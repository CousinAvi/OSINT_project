import web3
from web3 import HTTPProvider
from web3 import Web3
from web3 import WebsocketProvider
from web3.contract import ConciseContract
import json
import os

class Crypto():
	def __init__(self, contract, addresses):
		self.contract_address = Web3.toChecksumAddress(contract)
		self.addresses = addresses
		self.node_url = "wss://mainnet.infura.io/ws/v3/TOKEN_HERE"
		self.w3 = Web3(WebsocketProvider(self.node_url, websocket_kwargs={'timeout': 60}))
		self.abi = json.loads(open("./python_base/crypto/erc20.abi", "r").read())
		self.contract = self.w3.eth.contract(abi=self.abi, address=self.contract_address)

	def main(self):
		balance = 0
		
		for i in self.addresses:
			balance += self.contract.functions.balanceOf(Web3.toChecksumAddress(i)).call()

		balance = balance / self.contract.functions.decimals().call()

		return (self.contract.functions.name().call(), balance)