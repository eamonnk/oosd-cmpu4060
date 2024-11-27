# word = "computing"
# for character in word:
#    print("{}: {}".format(word.index(character), character))
   
# names = ['jim', 'john', 'jane', 'jen']

# # create an enumerated list
# print(list(enumerate(names)))

# # get a list of strings preceded by 1-based indices
# [ str(x[0] + 1) + " " + x[1] for x in enumerate(names) ]
# # or
# list(str(x[0] + 1) + " " + x[1] for x in enumerate(names))

# some names
names = ["ben", "con", "ann", "dan"]
scores = [23, 67, 34, 12]
# define a lambda expression that returns the 
# index in the list 'names' for the given string value
#---------------
get_index_for_name = lambda nm : names.index(nm)
# use it
get_index_for_name('ann')
get_index_for_name('ben')
#--------
get_score_for_person = lambda nm : scores[names.index(nm)]
get_score_for_person("ben")
get_score_for_person("dan")

sorted(names, key=get_score_for_person)
# or
sorted (names, key=lambda n : scores[names.index(n)])



