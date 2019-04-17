# cryptohw3

1
The ERC20 contract address is: 0x8B6565b970b71D945f79BFAEDF51b6962b7FA185
https://rinkeby.etherscan.io/address/0x8b6565b970b71d945f79bfaedf51b6962b7fa185 

2
The Winning contract address is:  0x292E468240a3524124e2cCb21e4f10EdE9Bec896
https://rinkeby.etherscan.io/address/0x292e468240a3524124e2ccb21e4f10ede9bec896

3.1 

B4d44f7f598c8ce17292fc883817afc2175a5a40d9e0c58f is Rafael’s key

3.2 

One potential vulnerability is that the user can produce invalid transactions on the chain via double spending. After 192 transactions, we could only observe < 192 bits, depending how many times such user produces invalid transactions.
To mitigate such issues, the backdoor should only allow user to produce valid transaction on each block so that the chain is intact w.r.t user’s secret key.

3.3 

The scheme can be modified to leak a user’s PK 2 bits at a time, thus reducing the time to reveal the entire secret key to half.

4 

The tumblers have almost the same amount transaction value as the output. The outputs happen after tumbler transactions by a short delay time. The differences in values are due to the transaction fee. As we can see, mixing bitcoin won’t completely solve the anonymity issue.The 4 tumbler and output pairs down below:
					
135g5Es7VXvbaAkwzguv7q7xaSSTifav5H (Bitcoin Fog - foggeddriztrcar2.onion)
Sends to					
13MUZ1Qk36LqExdcSRDZCxNRP1pcz1b5mT 


1MVXpgczazLvbtS8Nfp9v3Qpj4d8pUNXQM (Grams Helix - grams7enufi7jmdl.onion/helix) 
Sends to
1MTbp4bFftessrbTTpM5SC5Ap1iKaMHrM7
	
					
1GcZjZnfQUCs9L9RoAFLdd8YET2WQWrDAz (CoinCloud - coincloud25txgdf.onion)
Sends to
18RwKzXtL5YGvFwa9BHrPRvqXLkdYWsGfp 	
			
1KGhtebk4Nr2zZSn2NaFepeNF6KyjxpPJZ (PenguinMixer - penguinsmbshtgmf.onion) 
Sends to
1BCaztysy2paguXjuC8c652vckNMks69ce


Evaluation:
Appropriate Difficult
Spend 14 hours in total
Appropriate amount of coding

