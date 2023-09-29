from web3 import Web3

# Connect to your Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))   


contract_address = '0xYourContractAddress'
contract_abi = [
    
]

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Read data from the CSV file and add it to the smart contract
with open('data.csv', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:  # Skip the header row
        name, nationality, contact, image_path = line.strip().split(',')
        contract.functions.addPerson(name, nationality, contact, image_path).transact()

# Check the number of records stored in the contract
record_count = contract.functions.getPersonCount().call()
print(f"Number of records stored in the contract: {record_count}")


