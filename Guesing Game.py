#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random 
user_1 = random.randint(1,100)
attempts = 6
print('''Welcome to the game!!!''')
while True:
    while attempts > 0:
        guess = int(input('Please enter a number between 1 and 100>> '))
        if guess == user_1:
            print('Congratulations you have won!!')
            break
        elif guess < user_1:
            print('The number is too low!You have {} attempts left'.format(attempts - 1))
        else:
            print('The number is too high!You have {} attempts left '.format(attempts - 1))
        attempts -= 1
    if attempts == 0:
        print('I am really sorry!!The number was {}'.format(user_1))
    play_again = input('Do you want to play again? (yes/no) ')
    if play_again.lower() != 'yes':
        print('Thanks for playing!!!')
        break
    user_1 = random.randint(1,100)
    attempts = 6


# In[ ]:




