# '''
# Week 9 - Lab Assignment - Containers
# Exercise 1 - 1 of 2 files

# --w10-ex1-source-upper-storer.py--
# -eamonn kelly
# '''

class Source:
    # defining a class variable so cna re-use and call across other methods
    

    # have an input value of 'Upper' method here so the different methods can interact as per example file
    # u is the instance of Upper being passed into 'Source' constructor
    def __init__(self, u):
        self.upper=u
        self.source_do_work_rand_letters=[]
        
        
    # have an input value of 'Upper' method here so the different methods can interact as per example file
    def do_work(self):

        print("---------------------------------------------------------------------------")
        print("-------------------------- Source - do_work  ------------------------------")
        print("---------------------------------------------------------------------------")
        source_do_work_rand_int=random.randint(1, 10)
        print(" Generated Source Class random number: {}".format(source_do_work_rand_int))
        #use that random number to generate that number if random letters. Ten below crates letters a to z lower case
        # so full alphabet, from which we will later randomly select letters using our random.choices() method 
        source_letters = string.ascii_lowercase
        print("Source class letters_2: {} ".format(source_letters))
        # use the random choices method specifying the letters we created and k defines the length of the list
        # which is our random num between 1 and 10 which we created earlier 
        # we call the 'Source' method queue_work here and feed the letter objs into it one by one
        self.source_do_work_rand_letters=random.choices(source_letters, k=source_do_work_rand_int)
        print("Source class - generated letters: {} ".format(self.source_do_work_rand_letters))
        for source_letter_obj in self.source_do_work_rand_letters:
            self.upper.queue_work(source_letter_obj)
            print("Source class passed {} to Upper class".format(source_letter_obj))
   
    
    def print(self):
        print("Source class letters: {} ".format(self.source_do_work_rand_letters))


class Upper:
    # defining a class variable so can re-use and call across other methods
    # queue_deq_obj=deque()

# s is the storer instance that is being passed into the 'Upper' constructor
    def __init__(self, s):
        self.storer=s
        self.upper_queue_deq_obj=deque()

    
    # define a method that will take a list of items and pass it into a deque queue object
    def queue_work(self, l):
        self.letter=l
        
        print("---------------------------------------------------------------------------")
        print("-------------------------- Upper - queue_work  ----------------------------")
        print("---------------------------------------------------------------------------")
        
        self.upper_queue_deq_obj.append(l)
        print("Upper class added '{}' to Upper deque. Current Upper deque is: {} ".format(l, self.upper_queue_deq_obj))
        
    
    def do_work (self):
        
        
        print("---------------------------------------------------------------------------")
        print("-------------------------- Upper- do_work  --------------------------------")
        print("---------------------------------------------------------------------------")
        # take random number of length of queue, take the min() value of either one
        upper_do_work_rand_int=min(random.randint(1, 10), len(self.upper_queue_deq_obj))
        print("Generated Upper class random number: {} ".format(upper_do_work_rand_int))
        
        #use that random number to iterate through the deque object. Have to do over range of that number so add range method
        # FIFO =>  append right(add to the front)  > pop left(remove from back)
        for upper_letter_obj in range(upper_do_work_rand_int):
            letters_popped=self.upper_queue_deq_obj.popleft()
            letters_popped_upped=letters_popped.upper()
            self.storer.queue_work(letters_popped_upped)
            print("Upper class converted and popped {} to {} and passed it to Storer queue:" .format(letters_popped, letters_popped_upped))
    
    def queue_length(self):
        return (len(self.upper_queue_deq_obj))
        
    
    def print(self):
        print("Remaining deque in Upper class {}: ".format(self.upper_queue_deq_obj))
        
class Storer:
    
    def __init__(self):
        self.storer_queue_deq_obj=deque()
        self.storer_set_obj=set()
    
    def queue_work(self, sl):
        self.storer_letter=sl
        
        print("---------------------------------------------------------------------------")
        print("-------------------------- Storer - queue_work  ---------------------------")
        print("---------------------------------------------------------------------------")
        self.storer_queue_deq_obj.append(sl)
        print("Storer class added {} to deque. Current Storer deque is: {} ".format(sl, self.storer_queue_deq_obj))
        
    def do_work (self):
        
        print("---------------------------------------------------------------------------")
        print("-------------------------- Storer - do_work  ------------------------------")
        print("---------------------------------------------------------------------------")
        # take random number of length of deque queue, take the min() value of either random num or len of queue
        storer_do_work_rand_int=min(random.randint(1, 10), len(self.storer_queue_deq_obj))
        print("Generated Storer class random number: {} ".format(storer_do_work_rand_int))
        
        # use that random number to iterate through the deque object. Have to do over range of that number so add range method
        # FIFO =>  append right(add to the front)  > pop left(remove from back)
        for storer_letter_obj in range(storer_do_work_rand_int):
            letters_popped_storer=self.storer_queue_deq_obj.popleft()
            self.storer_set_obj.add(letters_popped_storer)
            print("Storer class popped from Storer class deque {} and added to Storer set() object. Current Storer Set is: {} ".format(letters_popped_storer, self.storer_set_obj))
    
    def queue_length(self):
        
        return (len(self.storer_queue_deq_obj))
    
    # we'll use sorted() to sort alphabetically as it generates a new list
    def get_store(self):
        self.storer_list_obj=[]
        self.storer_list_obj=list(self.storer_set_obj)
        return sorted(self.storer_list_obj)
        
    
    
    def print(self):
        print("Final deque in Storer class: {}".format(self.storer_queue_deq_obj))
        print("Final set in Storer class: {} ".format(self.storer_set_obj))
# creating instances of the different classes and then linking them. Must have them i this order as the previous one depends on the next one being created and Storer is the only one without a required parameter

mystorer=Storer()
myupper=Upper(mystorer)
mysource=Source(myupper)

#calling do_work method in 'mysource' instance, then 'myupper', then 'mystorer'
# num is control for while loop, we increment at end of each loop

num=1
# To specify number of loops modify value in 'while num < 50:' below
while num < 50:
    print(" ****************************************************************************************")
    print("     ********************************** --- Iteration {} --- ************************".format(num))
    print(" ****************************************************************************************")
    mysource.do_work()
    myupper.do_work()
    mystorer.do_work()

    print("---------------------------------------------------------------------------")
    print("--------------------- queue length in each iteration ----------------------")
    print("---------------------------------------------------------------------------")
    print("Upper -- Queue length --- {} :".format(myupper.queue_length()))
    print("Storer -- Queue length --- {} :".format(mystorer.queue_length()))
    num+=1

    print(" ****************************************************************************************")
    print("     ************* --- Finished Iteration through While loop --- *****************")
    print(" ****************************************************************************************")

print("---------------------------------------------------------------------------")
print("----------- letters of the alphabet not stored in the Storer object--------")
print("---------------------------------------------------------------------------")

# we'll define two sets and subtract them from each other and see if anything is left.
# This will be easier than iterating through a list
# if nothing left every letter in alphabet is accounted for and no letters missing
# if the final set of letters is True it contains letters which are mising
final_storer_obj=set(mystorer.get_store())
alphabet_upper=set(string.ascii_uppercase)
letters_not_in_storer_object=alphabet_upper-final_storer_obj

if letters_not_in_storer_object:
    print("The following letters were not in the Final storer Object. {}".format(sorted(letters_not_in_storer_object)))
else:
    print("The Final storer Object contains all letters of the alphabet, no letters are missing. ")
    
