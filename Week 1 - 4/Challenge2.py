start = int(input('Pick a starting number: '))
finish = int(input('Pick a finishing number: '))

while start != finish:
    if start < finish:   
        if (start % 2) == 0:
            print(start)
        start += 1    
    else:
        if (start % 2) == 0:
            print(start)
        start -= 1


print('Finished')