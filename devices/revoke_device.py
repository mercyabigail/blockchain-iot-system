import json
from web3 import Web3

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

assert w3.is_connected(), "Failed to connect to Ganache"

# Load contract information
with open("../build/contract_info.json", "r") as file:
    contract_info = json.load(file)

contract = w3.eth.contract(
    address=contract_info["contract_address"],
    abi=contract_info["abi"]
)

# Administrator account
account = "0x7a28A7Ea1Fbd17AFd1D6Ca37a968562769dfF1ad"
private_key = "0xb29555a4b6c0792efa9eb67abd10cdab3fdf17f2324b6add7ca46d1e7514d536"

# Device to revoke
device_id = input("Enter Device ID to revoke: ")

nonce = w3.eth.get_transaction_count(account)

transaction = contract.functions.revokeDevice(
    device_id
).build_transaction(
    {
        "from": account,
        "nonce": nonce,
        "gas": 300000,
        "gasPrice": w3.eth.gas_price,
        "chainId": w3.eth.chain_id
    }
)

signed_tx = w3.eth.account.sign_transaction(
    transaction,
    private_key
)

tx_hash = w3.eth.send_raw_transaction(
    signed_tx.raw_transaction
)

receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("\n==============================")
print("DEVICE REVOKED SUCCESSFULLY")
print("==============================")
print("Device ID :", device_id)
print("Transaction Hash :", tx_hash.hex())
print("Block Number :", receipt.blockNumber)