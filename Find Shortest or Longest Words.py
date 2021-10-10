#Create funtion to input a list of strings and find the shortest and longest words.

#creating an empty list
new_list = []

# a list of strings as input and split the strings
words = [item for item in input("Enter the list items : ").split(',')]
#print(words)
def find_short_long_word(words_list):
    shortest = None
    longest = None
    new_list = []
    for i in words:
        length = len(i)
        #print(length)
        if shortest is None:
            shortest = i
            new_list.append(i)
        elif longest is None:
            longest = i
            new_list.append(i)
        elif length > len(longest):
            new_list[1] = i
    return tuple(new_list)

print(find_short_long_word(words)) #call the function
