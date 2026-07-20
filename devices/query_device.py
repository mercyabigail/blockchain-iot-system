import json
from web3 import Web3

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

if not w3.is_connected():
    print("Connection failed")
    exit()

# Load contract information
with open("../build/contract_info.json", "r") as file:
    contract_info = json.load(file)

contract = w3.eth.contract(
    address=contract_info["contract_address"],
    abi=contract_info["abi"]
)

device_id = input("Enter Device ID: ")

registered, authenticated, revoked = contract.functions.getDeviceStatus(
    device_id
).call()

print("\n======================================")
print("      DEVICE STATUS")
print("======================================")

print(f"Device ID       : {device_id}")
print(f"Registered      : {'YES' if registered else 'NO'}")
print(f"Authenticated   : {'YES' if authenticated else 'NO'}")
print(f"Revoked         : {'YES' if revoked else 'NO'}")

print("--------------------------------------")

if registered and authenticated and not revoked:
    print("ACCESS STATUS   : GRANTED")
else:
    print("ACCESS STATUS   : DENIED")

print("======================================")