import json
from web3 import Web3

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

assert w3.is_connected(), "Failed to connect to Ganache"

# Load compiled contract
with open("../build/compiled_code.json") as file:
    compiled_sol = json.load(file)

bytecode = compiled_sol["contracts"]["DeviceRegistry.sol"]["DeviceRegistry"]["evm"]["bytecode"]["object"]

abi = compiled_sol["contracts"]["DeviceRegistry.sol"]["DeviceRegistry"]["abi"]

# Ganache account
account = "0x7a28A7Ea1Fbd17AFd1D6Ca37a968562769dfF1ad"

private_key = "0xb29555a4b6c0792efa9eb67abd10cdab3fdf17f2324b6add7ca46d1e7514d536"

# Contract object
DeviceRegistry = w3.eth.contract(
    abi=abi,
    bytecode=bytecode
)

# Current nonce
nonce = w3.eth.get_transaction_count(account)

# Build deployment transaction
transaction = DeviceRegistry.constructor().build_transaction(
    {
        "chainId": 1337,
        "gas": 3000000,
        "gasPrice": w3.to_wei("20", "gwei"),
        "nonce": nonce,
        "from": account
    }
)

# Sign transaction
signed_txn = w3.eth.account.sign_transaction(
    transaction,
    private_key=private_key
)

# Send transaction
tx_hash = w3.eth.send_raw_transaction(
    signed_txn.raw_transaction
)

print("Deploying contract...")
print("Transaction Hash:", tx_hash.hex())

# Wait for receipt
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("\nDeployment Successful!")
print("Contract Address:", receipt.contractAddress)

# Save ABI and contract address
contract_info = {
    "abi": abi,
    "contract_address": receipt.contractAddress
}

with open("../build/contract_info.json", "w") as file:
    json.dump(contract_info, file, indent=4)

print("\ncontract_info.json created successfully.")