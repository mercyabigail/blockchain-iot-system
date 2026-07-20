
import json
import hashlib
from web3 import Web3

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
assert w3.is_connected(), "Ganache connection failed."

# Load contract information
with open("../build/contract_info.json") as file:
    contract_info = json.load(file)

contract_address = contract_info["contract_address"]
abi = contract_info["abi"]

contract = w3.eth.contract(
    address=contract_address,
    abi=abi
)

# Administrator account
account = "0x7a28A7Ea1Fbd17AFd1D6Ca37a968562769dfF1ad"
private_key = "0xb29555a4b6c0792efa9eb67abd10cdab3fdf17f2324b6add7ca46d1e7514d536"

# -----------------------------
# Device Information
# -----------------------------

device_id = input("Enter Device ID: ")
device_name = input("Enter Device Name: ")
secret = input("Enter Device Secret: ")

credential_hash = hashlib.sha256(
    secret.encode()
).digest()

nonce = w3.eth.get_transaction_count(account)

transaction = contract.functions.registerDevice(

    device_id,

    device_name,

    credential_hash

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

receipt = w3.eth.wait_for_transaction_receipt(
    tx_hash
)

print("--------------------------------")

print("DEVICE REGISTERED")

print("--------------------------------")

print("Device ID:", device_id)

print("Device Name:", device_name)

print("Transaction:")

print(tx_hash.hex())

print("Block:", receipt.blockNumber)