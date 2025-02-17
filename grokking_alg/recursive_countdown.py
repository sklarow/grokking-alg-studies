def countdown (i):
    print (i)  
    if i <= 1:      # base case
        return
    else:           # recursive case
        countdown(i-1)
        

countdown(3)
countdown(-122)
countdown(0)
countdown(1)
countdown(10)
