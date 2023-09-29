# Refugee Secure Data using Blockchain
A refugee data storage project using blockchain
Refugee Camp


Introduction
The Refugee Camp application is a Flask application that uses OpenCV to photograph refugees and save their data on the blockchain using Geth, Truffle, and the web3 Python library. The application is intended to assist refugee camps in more efficiently and securely managing their data.
Technical Architecture
The Refugee Camp application is structured on three layers:
• Presentation tier: This tier is in charge of managing user interactions and displaying the user interface. The Flask web framework is used to implement the presentation tier.
• Application tier: This tier is in charge of handling business logic and interfacing with the blockchain. The OpenCV library, the Geth Ethereum client, the Truffle framework, and the web3 Python package are used to build the application tier.
• Data layer: The data tier is in charge of storing refugee data on the blockchain. The Ethereum blockchain is used to implement the data tier.
Technical Implementation
The Refugee Camp application is developed using Flask. The OpenCV library is used by the programme to capture photographs of migrants. The photographs are then cropped and scaled before being uploaded to the blockchain through the Geth Ethereum client. The Truffle framework and the web3 Python library are also used to store the refugee's name, nationality, and contact information on the blockchain.

Refugee Camp Smart Contract
The Refugee Camp smart contract is implemented using the Truffle framework. The smart contract has the following functions:
•	storeImage(bytes32 imageHash): Stores a refugee's image on the blockchain.
•	storeRefugeeInformation(string name, string nationality, string contactInfo): Stores a refugee's name, nationality, and contact information on the blockchain.
•	getRefugeeInformation(bytes32 imageHash): Retrieves a refugee's information from the blockchain.
Usage
Personnel at the camp must first install the necessary dependencies and deploy the smart contracts to the Ethereum blockchain before using the Refugee Camp application. Workers may begin photographing migrants and storing their data on the blockchain once the smart contracts are in place.

Employees would launch the Refugee Camp programme and tap the "Capture" button to picture a refugee. After that, the application would open a camera window, allowing employees to picture the refugee. Following the capture of the image, the application will crop and resize it before saving it on the blockchain and the users would also need to fill out the details of the refugees like name nationality and contact info 
Employees would utilise the Refugee Camp application and click the "Save" button to store refugee information on the blockchain. 

The application would then display a form on which employees may enter the refugee's name, nationality, and contact information. This information Is stored on the blockchain using the smart contract.

To see and manage refugee information on the blockchain, personnel would use the Refugee Camp application and click the "View Data" button. The user can then see  a list of all refugees whose data is recorded on the blockchain. 
Benefits

The Refugee Camp application offers the following advantages: • Assists refugee camps in managing their data more efficiently and securely.
• Offers a secure way to keep refugee information.
• Facilitates the sharing of refugee information with other organisations.
• Assists refugees in proving their identity and gaining access to services.

Conclusion

The Refugee Camp app is a useful tool that can assist refugee camps in improving the efficiency and security of their data administration. It could also assist refugees in proving their identity and gaining access to services.

Future Features 
Adding face detection for database matching 
Adding more robust search and data analytic features 
