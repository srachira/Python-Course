__author__ = 'SuSh'
#input = {'user2': 'shravan', 'user3': 'spandana', 'user1': 'apoorva'}

dict = {"abcd":"apoorva","def":"user","dhsjgf":"shravan"}
def print_subforums():
    header = ("SubForums","Created By")
    dict_list=dict.items()
    dict_list.insert(0,header)
    col_width = max(len(word) for row in dict_list for word in row) + 2  # padding
    for row in dict_list:
        print "".join(word.ljust(col_width) for word in row)


print_subforums()
