import random
import string
from collections import deque

class Source:
    # defining a class variable so cna re-use and call across other methods
    

    # have an input value of 'Upper' method here so the different methods can interact as per example file
    # u is the instance of Upper being passed into 'Source' constructor
    def __init__(self, u):
        self.upper=u
        self.source_do_work_rand_letters=[]
        
        
    # have an input value of 'Upper' method here so the different methods can interact as per example file
    def do_work(self):

        source_do_work_rand_int=random.randint(1, 10)
       
        #use that random number to generate that number if random letters 
        source_letters = string.ascii_lowercase
        print(source_letters)
        # use the random choices method specifying the letters we created and k defines the length of the list
        # which is our random num between 1 and 10 which we created earlier 
        # we call the 'Source' method queue_work here and feed the letter objs into it one by one
        self.source_do_work_rand_letters=random.choices(source_letters, k=source_do_work_rand_int)
        for source_letter_obj in self.source_do_work_rand_letters:
            self.upper.queue_work(source_letter_obj)
            print(f"Source passed '{source_letter_obj}' to Upper")
   
    
    def print(self):
        print(self.source_do_work_rand_letters)
        print(source_letter_obj)
        # print(type(self.do_work_rand_letters))
        # print(type(self.do_work_rand_letters[0]))        


class Upper:
    # defining a class variable so can re-use and call across other methods
    #queue_deq_obj=deque()

# s is the storer instance that is being passed into the 'Upper' constructor
    def __init__(self, s):
        self.storer=s
        self.upper_queue_deq_obj=deque()

    
    # define a method that will take a list of items and pass it into a deque queue object
    def queue_work(self, l):
        self.letter=l
        
        self.upper_queue_deq_obj.append(l)
        print(f"Upper added '{l}' to deque. Current deque: {self.upper_queue_deq_obj}")
        
    
    def do_work (self):
        
        # take random number of length of queue, take the min() value of either one
        upper_do_work_rand_int=min(random.randint(1, 10), len(self.upper_queue_deq_obj))
        print(upper_do_work_rand_int)
        
        #use that random number to iterate through the deque object. Have to do over range of that number so add range method
        # FIFO =>  append right(add to the front)  > pop left(remove from back)
        for upper_letter_obj in range(upper_do_work_rand_int):
            letters_popped=self.upper_queue_deq_obj.popleft()
            letters_popped_upped=letters_popped.upper()
            print(f"Upper converted '{letters_popped}' to '{letters_popped_upped}' and passed it to Storer")
            self.storer.queue_work(letters_popped_upped)
    
    def print(self):
        print(self.upper_queue_deq_obj)
        print(type(self.upper_queue_deq_obj))
        print(f"Remaining deque in Upper: {self.upper_queue_deq_obj}")
        
class Storer:
    
    def __init__(self):
        self.storer_queue_deq_obj=deque()
    
    def queue_work(self, sl):
        self.storer_letter=sl
        
        self.storer_queue_deq_obj.append(sl)
        print(f"Storer added '{sl}' to deque. Current deque: {self.storer_queue_deq_obj}")
        
    def print(self):
        print(f"Final deque in Storer: {self.storer_queue_deq_obj}")
# creating instances of the different classes and then linking them. Must have them i this order as the previous one depends on the next one being created and Storer is the only one without a required parameter

mystorer=Storer()
myupper=Upper(mystorer)
mysource=Source(myupper)

#calling do_work method in 'mysource' instance, then 'myupper'
mysource.do_work()
myupper.do_work()
myupper.print()
mysource.print()
mystorer.print()
