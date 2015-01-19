s = 'zyxwvutsrqponmlkjihgfedcba'

def longestSub(sub):
    position = 0
    longest = ''
    while position < len(sub):
        sample = sub[0:len(sub)-position]
#        print 'at while' + sample
        if sample == ''.join(sorted(sample)) and len(sample) > len(longest):
            longest = sample
#            print 'at longest' + str(longest)
        position += 1
#        print 'here is my position' + str(position)
    return longest
    
position = 0
longest = ''
while position < len(s)-1:
    sample = s[position:len(s)]
#    print 'at while' + ' ' + sample
    longSample = longestSub(sample)
#    print 'at while long' + ' ' + longSample
    if len(longSample) > len(longest):
        longest = longSample
#        print 'at longest' + ' ' + str(longest)
    position += 1
    
print('Longest substring in alphabetical order is: ' + longest)
    
    
    




            
        

        
        
        