# '''
# Week 9 - Lab Assignment -
# Containers - Exercise 2 - 2 of 2 files

# --w10-ex2.py--
# -eamonn kelly
# '''

# This file is runnable. Just run in IDE and UI menu will display and options cnabe selected in turn as needed
# output will eb displayed and can exit by choosing exit option when finished.
# structure of the file is
#  - Dictionary class
#  - DictionaryUI class
#  - initial dict data and instance calls are at the end of the file

class Dictionary:
    
    
    def __init__(self, d):
        self.data=d

    
    def print(self):
        print("The following is the current dictionary content :  {} ".format(self.data))


    def word_lookup(self, w):
        self.word=w
        
        if self.word not in self.data:
            print("The word < {} > is not in the dictionary. Please try a different word.".format(self.word))
        else:
            self.data.get(self.word)
            print("the word < {} > is in the dictionary. It means  < {} >".format(self.word, self.data[self.word]))

# as need to be able to add >=1 word at a time need flexible number of arguments in the method input
# so we use * 
    def add_word(self, *words_defs):
        self.words_defs=words_defs
        print("Please Enter a word and definition with 'No quotes' in the form {< word > : < definition > }" )
        print("You can enter multiple keys and values if you wish, separated by a comma")
        
        # we only check for dict and str input types, as we provide prompts for users in hwo to input he data
        # could add more options to make it more robust but ran out of time 
        # check to see if the added word is a dictionary format of key value pair
        for item in self.words_defs:
            if isinstance(item, dict):
                for word, definition in item.items():
                    if word in self.data:
                        print("Warning The word < {} > already exists. ".format(word))
                        update_word=input("Do you wish to update anyway? y/n:  ")
                        if update_word=='y':
                            self.data[word]=definition
                        else:
                            print("We have not updated the word.")

                    else:
                        self.data[word]=definition
            # scenario where data entered as a string, split the string on the : and then strop any excess whitespaces
            elif isinstance (item, str):
                word, definition = item.split(":", 1)
                word, definition = word.strip(), definition.strip()
                print(word)
                print(definition)
                if word in self.data:
                    print("Warning The word < {} > already exists. ".format(word))
                    update_word=input("Do you wish to update anyway? y/n:  ")
                    if update_word=='y':
                       self.data[word]=definition
                    else:
                        print("We have not updated the word.")
                else:
                    self.data[word]=definition
                    print("We have added << {}:{} >> key value pair to the dictionary: ".format(word, definition))
                        
                
        
    def delete_word(self, duw):
        self.delete_user_word=duw
        
        if not self.delete_user_word in self.data:
            print(" The word  < {} > is not in the dictionary. Please try another word. ".format(self.delete_user_word))
        elif self.delete_user_word in self.data:
            self.data.pop(self.delete_user_word)
            print("The word  < {} > , and its definition, has been removed from the dictionary. ".format(self.delete_user_word))
        
class DictionaryUI:
    
    # constructor will take a value dictionary, this is the instance of the dictionary that we will start off the Dictionary class
    # i.e. we create a dictionary class instance, then create a DictionaryUI class instance based off that instance
    def __init__(self, d):
        self.dictionary=d
        
   # run method() - this will call the dictionary methods. we will generally add a print statement after the method call
   # so can demo output has changed
    def run(self):
        
         # condition state to run while loop = True and set to False when we choose to exit at option 7.
         # the below
        num = True
        while num:
            print("----------------------------------------------------------------------")
            print("-------------------------  Dictionary Menu  --------------------------")
            print("----------------  Choose from the following options  -----------------")
            print("----------------------------------------------------------------------")
            print("1. Look up Word")
            print("2. Add single Word")
            print("3. Add Multiple Words")
            print("4. Add word that already exists")
            print("5. Delete Word")
            print("6. Print Dictionary")
            print("7. Exit")
            
            dict_choice=input("To choose, please type 1, 2, 3, 4, 5, 6 or 7 and press Enter: ")
            print(dict_choice)
            print(type(dict_choice))
            
            # match str object
            if dict_choice== '1':
                print(" -----------------------------------------------------------------------")
                print(" --------------------- 1. Look up word----------------------------------------")
                print(" -----------------------------------------------------------------------")
                word=input("Enter the word you wish to look up: For example 'apple', ;'baby', 'car' , 'deer', 'earth' >>   ")
                print("")
                self.dictionary.word_lookup(word)
                print("")
            elif dict_choice=='2':
                print(" -----------------------------------------------------------------------")
                print(" --------------------- 2. add single word----------------------------------------")
                print(" -----------------------------------------------------------------------")
                single_word_defn=input("Enter the single word and definition with no quotes: For example >> ice : cold and can skate on it << :   ")
                mydict.add_word(single_word_defn)
                mydict.print()
            elif dict_choice=='3':
                print(" -----------------------------------------------------------------------")
                print(" --------------------- 3. add multiple words----------------------------------------")
                print(" -----------------------------------------------------------------------")
                multi_word_defn=input("Enter the multiple words and definitions with no quotes separated by a comma: For example >> big: very big object, small : a very small thing, tiny : a very tine object << :   ")
                mydict.add_word(multi_word_defn)
                mydict.print()
            elif dict_choice=='4':
                print(" -----------------------------------------------------------------------")
                print(" --- 4.  add word that already exists---Input (y\\n) is required ---------")
                print("Have hard coded the key value pair for 'apple' just to force the y/n prompt to make sur eit is demo'd")
                mydict.add_word({'apple': 'red and tasty'})
                mydict.print()
            elif dict_choice=='5':
                print(" -----------------------------------------------------------------------")
                print(" ------------------ 5.  Deletion of word from Dictionary   ---------------")
                print(" -----------------------------------------------------------------------")
                user_del_word=input("Enter the word you wish to  delete For example 'apple', 'baby', 'car' , 'deer', 'earth' >>   ")
                mydict.delete_word(user_del_word)
                mydict.print()
            elif dict_choice=='6':
                print(" -----------------------------------------------------------------------")
                print(" --------------------  6. Print Dictionary content ---------------------")
                print(" -----------------------------------------------------------------------")
                mydict.print()
            elif dict_choice=='7':
                print(" -----------------------------------------------------------------------")
                print(" -------  7. You have chosen to exit. Thank You and Good Bye ----------")
                print(" -----------------------------------------------------------------------")
                num = False
                break
            else:
                print(" You have entered an invalid option. You will exit the program. Please run the program again and select a valid opion if you wish")

            
    

dict_data={
"apple": "a fruit, can be green, red or yellow",
"baby": "a very young person", 
"car":	"a transport vehicle",
"deer":	"an animal with antlers",
"earth": "a planet, the one we live on"
}

mydict=Dictionary(dict_data)
mydict.print()
mydict_ui=DictionaryUI(mydict)
mydict_ui.run()
