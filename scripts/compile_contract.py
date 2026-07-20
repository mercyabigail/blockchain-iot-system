from solcx import install_solc, compile_standard
import json

install_solc("0.8.19")

with open("../contracts/DeviceRegistry.sol", "r") as file:
    contract = file.read()

compiled = compile_standard(
    {
        "language": "Solidity",
        "sources": {
            "DeviceRegistry.sol": {
                "content": contract
            }
        },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": [
                        "abi",
                        "metadata",
                        "evm.bytecode",
                        "evm.bytecode.sourceMap"
                    ]
                }
            }
        }
    },
    solc_version="0.8.19"
)

with open("../build/compiled_code.json", "w") as file:
    json.dump(compiled, file, indent=4)

print("Smart contract compiled successfully.")