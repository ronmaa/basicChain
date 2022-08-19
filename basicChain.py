#basic blockchain

import datetime
import hashlib

class Blockchain:
    def __init__(self):
        self.chain=[]
        self.create_block(proof = 1,prev_hash='0')
        
    def create_block(self,proof,prev_hash):
        block={'index':len(self.chain)+1,
               'timestamp':str(datetime.datetime.now()),
               'proof':proof,
               'prev_hash':prev_hash}
        self.chain.append(block)
        return block
    
    def get_prev_block(self):
        return self.chain[-1]
    
    def proof_of_work(self,prev_proof):
        new_proof=1
        check_proof=False
        while check_proof is False:
            hash_value=hashlib.sha256(str(new_proof**2 - prev_proof**2).encode()).hexdigest()
            if hash_value[:4]=='0000':
                check_proof=True
            else:
                new_proof +=1
        return new_proof