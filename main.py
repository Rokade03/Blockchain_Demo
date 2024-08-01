import hashlib 
import time
import keyboard

def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

class User1:
    def __init__(self, balance):
        self.balance = balance

    def mined1(self):
        counter = 0
        while True:
            print(f"Current value: {counter}")
            counter += 0.10
            start_time = time.time()
            while time.time() - start_time < 2:
                if keyboard.is_pressed('q'):
                    print("Button pressed. Stopping the mine.")
                    print(f"You Collected {counter} Rockcoins")
                    self.balance = self.balance + counter
                    return 0
    def show_balance1(self):
        final = self.balance
        print(final)
        return final



class Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash

#Creates a Blockchain and in which genesis block is created which is the first block in creating a block chain.
class Blockchain:
    def __init__(self):
        hashLast = hashGenerator('Last_Generation')
        hashFirst = hashGenerator('First_Generation')

        genesis = Block('Gen_data', hashFirst, hashLast)
        self.chain = [genesis]

#A function which adds block after every transaction. 
    def add_block(self,data):
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data + prev_hash)
        block = Block(data, hash, prev_hash)
        self.chain.append(block)

bc = Blockchain()
u1 = User1(0)
print('Note: This is a demo on how blocks are created upon transactions.\n')
print('Welcome to Blockchain Demo:')
a = int(input('Type the Password:(6969)\n'))
if a==6969:
    user1=0
    block_no=0
    while user1!=6:
        user1=int(input("\nWelcome User1\n What Actions You want to Perform:\n 1.Send Rockcoin 2.Receive Rockcoin 3.Rockcoin Faucet 4.Check Balance 5.View the Blockchain 6.Exit\n"))
        if user1==1:
            send = float(input("Enter the Value = "))
            print(u1.show_balance1())
            if(send<=u1.show_balance1()):
                amount = u1.show_balance1() - send
                print("The Balance is = ",amount)
                u1 = User1(amount)
                block_no = block_no + 1
                sent = str(block_no)
                bc.add_block('sent '+sent)
            else:
                print("Not Enough Balance")
        elif user1==2:
            receive = float(input("Enter the Value(This is by some other user) = "))
            total = u1.show_balance1() + receive
            print("The Balance is = ",total)
            u1 = User1(total)
            block_no = block_no + 1
            received = str(block_no)
            bc.add_block('received '+received)
        elif user1==3:
            u1.mined1()
            block_no = block_no + 1
            mined = str(block_no)
            bc.add_block('mined '+mined)
        elif user1==4:
            print("You have",+u1.show_balance1(),"Rockcoins\n")
        elif user1==5:
            for block in bc.chain:
                print(block.__dict__)
        elif user1==6:
            print("Thank You")
        else:
            print('Invalid Option\n')
else:
    print("Logging Out...")
    exit()