import json
from web3 import Web3
from datetime import datetime

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

if not w3.is_connected():
    print("Failed to connect to Ganache")
    exit()

# Load contract information
with open("../build/contract_info.json", "r") as file:
    contract_info = json.load(file)

contract = w3.eth.contract(
    address=contract_info["contract_address"],
    abi=contract_info["abi"]
)

print("\n===================================================")
print("           BLOCKCHAIN EVENT LOG")
print("===================================================\n")

# --------------------------------------------------
# Device Registered Events
# --------------------------------------------------
events = contract.events.DeviceRegistered.get_logs()

for event in events:

    print("DEVICE REGISTERED")
    print("----------------------------------------")
    print("Device ID :", event["args"]["deviceID"])
    print("Wallet    :", event["args"]["wallet"])
    print()

# --------------------------------------------------
# Authentication Success Events
# --------------------------------------------------
events = contract.events.AuthenticationSuccess.get_logs()

for event in events:

    timestamp = datetime.fromtimestamp(
        event["args"]["timestamp"]
    )

    print("AUTHENTICATION SUCCESS")
    print("----------------------------------------")
    print("Device ID :", event["args"]["deviceID"])
    print("Time      :", timestamp)
    print()

# --------------------------------------------------
# Authentication Failed Events
# --------------------------------------------------
events = contract.events.AuthenticationFailed.get_logs()

for event in events:

    timestamp = datetime.fromtimestamp(
        event["args"]["timestamp"]
    )

    print("AUTHENTICATION FAILED")
    print("----------------------------------------")
    print("Device ID :", event["args"]["deviceID"])
    print("Time      :", timestamp)
    print()

# --------------------------------------------------
# Device Revoked Events
# --------------------------------------------------
events = contract.events.DeviceRevoked.get_logs()

for event in events:

    print("DEVICE REVOKED")
    print("----------------------------------------")
    print("Device ID :", event["args"]["deviceID"])
    print()

print("===================================================")