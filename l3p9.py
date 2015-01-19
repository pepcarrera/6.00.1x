# -*- coding: utf-8 -*-
print('Please think of a number between 0 and 100!')
low = 0
high = 100
guess = (high + low)/2
result = ''
while result != 'c':
    print 'Is your secret number %d?' % guess
    result = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
    if result == 'c':
        print 'Game over. Your secret number was: %d' % guess
        break
    elif result == 'l':
        low = guess
        guess = (high + low)/2
    elif result == 'h': 
        high = guess
        guess = (high + low)/2    
    else:
        print 'sorry I did not understand your input'

            
    
    