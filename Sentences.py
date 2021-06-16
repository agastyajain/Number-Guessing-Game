inputBox = input("Enter a sentence : ")
no_of_characters = 0
words = 1
pattern = [1, 2, 3, 4, 5]

for character in inputBox:
    #print(character)
    #print(inputBox)
    no_of_characters = no_of_characters + 1
    if character == ' ':
        words = words+1

i = 0
while i <= len(inputBox):
   print(inputBox[0:i])
   i = i+1

#print('Total No. Of Words : ' + str(words))

