from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545" # ganache url
web3 = Web3(Web3.HTTPProvider(ganache_url))

wallet_1 = "0xf9c63a17FD6a584916830d515C4229c536D7aa30" # ganache
wallet_2 = "0xac795B9e584Aa8de4aa265D74174256f921d102C" # ganache

private_key = "737fd7fe85ffb7ec6bd843870f60208c781f40ab16178f4cd6cc8445f3b86e17"

nonce = web3.eth.getTransactionCount(wallet_1)

# get nonce
# build a transaction

tx = {
    'nonce': nonce,
    'to': wallet_2,
    'value': web3.toWei(4, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('30', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

# 0x5dc82187543068b04e315e6335bf660226e128e3d5596e1d2cedf7769fe919e3
# etherscan