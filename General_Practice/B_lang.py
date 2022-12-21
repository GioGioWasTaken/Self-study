word=str(input("Enter the word you'd like to change to the B language: "))
#in the B langauge B must included between every second letter, except the first one.
def change_to_b_lang():
   index=0
   new_word = []
   while index<len(word)-1: #while index is smaller than the length of the word. The "-1" is meant to prevent it from being equal.
        for letter in word:
            #print(letter)
            if index%2==0:
                letter=''.join((letter,'b'))
            new_word.append(letter)
            index=index+1
   print(new_word)
   print(''.join(new_word))
change_to_b_lang()
