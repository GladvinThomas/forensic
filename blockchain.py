import random
import sys
import base64

import json

from web3 import Web3
from solcx import compile_standard



compiled_sol = compile_standard({
     "language": "Solidity",
     "sources": {
         "phb.sol": {
             "content": '''
                 pragma solidity >=0.4.0 <0.8.16;
               

                contract PHB {

                    struct File
                    {                     
                        int id1;
                        string hash;
                        
                    }

                    File []files;

                    function addFile(int id1,string memory hash) public
                    {
                        File memory e
                            =File(id1,hash
                                    );
                        files.push(e);
                    }

                    function getFile(int id1) public view returns(
                            
                            string memory
                            )
                    {
                        uint i;
                        for(i=0;i<files.length;i++)
                        {
                            File memory e
                                =files[i];
                            
                            if(e.id1==id1)
                            {
                                return(e.hash
                                   );
                            }
                        }
                        
                        
                        return("Not Found"
                               );
                    }

                   

                     


                    

                    
                       
                }

               '''
         }
     },
     "settings":
         {
             "outputSelection": {
                 "*": {
                     "*": [
                         "metadata", "evm.bytecode"
                         , "evm.bytecode.sourceMap"
                     ]
                 }
             }
         }
 })







def create_contract():
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    # get bytecode
    bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    pb = w3.eth.contract(abi=abi, bytecode=bytecode)

    # # Submit the transaction that deploys the contract
    tx_hash = pb.constructor().transact()

    # # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print("tx_receipt.contractAddress: ",tx_receipt.contractAddress)
    f=open('contract_address.txt','w')
    f.write(tx_receipt.contractAddress)
    f.close()


def addFile(id1,hash):
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))

	# get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    
    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    
    tx_hash = p1.functions.addFile(id1,hash).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)

    #print(tx_hash) 
    print(tx_receipt)
    

def get_file(id1):
    id1=int(id1)
    p1=get_contract()
    store = p1.functions.getFile(id1).call()
    print(store)
    return store
    

def get_contract():
    f=open('contract_address.txt','r')
    address=f.read()
    f.close()
    blockchain_address = 'http://127.0.0.1:7545'
    # # Client instance to interact with the blockchain
    w3 = Web3(Web3.HTTPProvider(blockchain_address))

    print(w3.isConnected())
    #w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(type(w3.eth.accounts[0]))

	# get bytecode
    # bytecode = compiled_sol['contracts']['phb.sol']['PHB']['evm']['bytecode']['object']

    # # get abi
    abi = json.loads(compiled_sol['contracts']['phb.sol']['PHB']['metadata'])['output']['abi']

    p1 = w3.eth.contract(
        address=address,
        abi=abi
    )
    return p1









if __name__=="__main__":
    
    create_contract()
    #get_file(7)