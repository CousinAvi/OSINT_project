import web3
from web3 import HTTPProvider
from web3 import Web3
from web3 import WebsocketProvider
from web3.contract import ConciseContract
import json
import os

class Txchain():
	def __init__(self, contract, source, destination):
		self.contract_address = Web3.toChecksumAddress(contract)
		self.source_address = Web3.toChecksumAddress(source)
		self.destination_address = Web3.toChecksumAddress(destination)
		self.node_url = "wss://mainnet.infura.io/ws/v3/YOUR_TOKEN"
		self.w3 = Web3(WebsocketProvider(self.node_url, websocket_kwargs={'timeout': 60}))
		self.abi = json.loads(open("./python_base/txchain/erc20.abi", "r").read())
		self.contract = self.w3.eth.contract(abi=self.abi, address=self.contract_address)
		self.start_block = self.w3.eth.blockNumber - 8640

	def trace(self, to):
		if to == self.destination_address:
			return [to]

		filter = self.contract.events.Transfer.createFilter(fromBlock=self.start_block, argument_filters={"from": to})
		start_events = filter.get_all_entries()
		
		for i in start_events:
			chain = self.trace(i["args"]["to"])
			if len(chain) > 0:
				chain.append(to)
				return chain

		return list()

	def main(self):
		tx_chain = []
		
		filter = self.contract.events.Transfer.createFilter(fromBlock=self.start_block, argument_filters={"from": self.source_address})
		start_events = filter.get_all_entries()
		print(start_events)
		for i in start_events:
			print(i)
			chain = self.trace(i["args"]["to"])
			if len(chain) > 0:
				chain.append(self.source_address)
				tx_chain = reversed(chain)

		return list(tx_chain)
'''
contract = "0xdac17f958d2ee523a2206206994597c13d831ec7"
source = "0x01b76af77e7e6b60f8b370df960d2afeaf46e9ba"
destination = "0x0a98fb70939162725ae66e626fe4b52cff62c2e5"
txchain = Txchain(contract, source, destination)
print(txchain.main())
'''