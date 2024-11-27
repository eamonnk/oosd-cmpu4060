import random
import string
from collections import deque

class Source:
    # defining a class variable so cna re-use and call across other methods
    do_work_rand_letter=[]

    def __init__(self):
        pass
        
    def Source_do_work(self):
        
        #create random number between 1 and 10
        #work_rand_int=1
        
        do_work_rand_int=random.randint(1, 10)
        print(do_work_rand_int)
        
        #use that random number to generate that number if random letters 
        letters = string.ascii_lowercase
        print(letters)
        do_work_rand_letters=random.choices(letters, k=do_work_rand_int)
        print(do_work_rand_letters)
        print(type(do_work_rand_letters))
        print(type(do_work_rand_letters[0]))
        
class Upper:
    # defining a class variable so cna re-use and call across other methods
    queue_deq_obj=deque()


    def Upper_queue_works(self, do_work_rand_letters):
        self.do_work_rand_letter=do_work_rand_letters
        
        queue_deq_obj=deque()
       
        for i in self.do_work_rand_letters:
        
        
        
        
        
        
    


mysource=Source()
mysource.Source_do_work()
