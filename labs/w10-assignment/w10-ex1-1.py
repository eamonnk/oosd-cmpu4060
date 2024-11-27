import random
import string
from collections import deque

class Source:
    # defining a class variable so cna re-use and call across other methods
    

    # have an input value of 'Upper' method here so the different methods can interact as per example file
    def __init__(self, u):
        self.upper=u
    
        self.do_work_rand_letters=[]
        
        
    # have an input value of 'Upper' method here so the different methods can interact as per example file
    def do_work(self):
        #self.letter()=u
            
        #create random number between 1 and 10
        #work_rand_int=1
        do_work_rand_int=random.randint(1, 10)
        print(do_work_rand_int)
        
        #use that random number to generate that number if random letters 
        letters = string.ascii_lowercase
        print(letters)
        # use the random choices method specifying the letters we created and k defines the length of the list
        # which is our random num between 1 and 10 which we created earlier 
        self.do_work_rand_letters=random.choices(letters, k=do_work_rand_int)
        print(self.do_work_rand_letters)
        print(type(self.do_work_rand_letters))
        print(type(self.do_work_rand_letters[0]))
        # return self.do_work_rand_letters
        # print(self.do_work_rand_letters)
        # print(type(self.do_work_rand_letters))
        # print(type(self.do_work_rand_letters[0]))
        for letter_obj in self.do_work_rand_letters:
            self.upper.queue_work.append(letter_obj)
            print(letter_obj)     
    
    
    def print(self):
        print(self.do_work_rand_letters)
        # print(type(self.do_work_rand_letters))
        # print(type(self.do_work_rand_letters[0]))        


class Upper:
    # defining a class variable so can re-use and call across other methods
    #queue_deq_obj=deque()

    def __init__(self, s):
        self.storer=s
        self.queue_deq_obj=deque()

    
    # define a method that will take a list of items and pass it into a deque queue object
    def queue_work(self, l):
        self.letter=l
        
        self.queue_deq_obj.append(l)
        for i in self.queue_deq_obj:
            print(self.queue_deq_obj)

        
        
        # self.letter
        # self.do_work_rand_letters=do_work_rand_letters
        
        # queue_deq_obj=deque()
       
        # for i in self.do_work_rand_letters:
        #     self.queue_deq_obj.append(i)
        
        print(self.queue_deq_obj)
        print(type(self.queue_deq_obj))
              
    def print(self):
        print(self.queue_deq_obj)
        print(type(self.queue_deq_obj))
        
class Storer:
    
    def __intit__(self):
        pass   
        
        
# crearing instances of the different classes and then linking them. Must have them i this order as the previous one depends on the next one being created and Storer is the only one without a required parameter

mystorer=Storer()
myupper=Upper(mystorer)
mysource=Source(myupper)

myupper.print()
mysource.print()


# mysource=Source()
# randon_letters = mysource.Source_do_work()
# myupper1=Upper()
# myupper1.queue_work(randon_letters)
