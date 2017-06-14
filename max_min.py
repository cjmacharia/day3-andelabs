def find_max_min(numbers): 

    """function definition pass in a parameter called numbers

        also we initialize the minimum and maximum variables."""

    minNumber = 0;                            
    maxNumber = 0;                             
    for n in numbers:  

        """ loop through the numbers  and inside this
        loop we have the coditions for finding the maximum and minimum values
        then we return the two numbers as an array """

        if n > maxNumber or maxNumber is 0:   
            maxNumber = n
        if n < minNumber or minNumber is 0:      
            minNumber = n
    if minNumber == maxNumber:                      
        return [len(numbers)]
    else:
        return [minNumber, maxNumber]
print(find_max_min([43,5,6,37]))   