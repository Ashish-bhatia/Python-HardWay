print "Hello World!\n"
#return square

def squarelist():
    numberlist1 = [1,2,3,4,5]
    resultlist1 = []
    for i in numberlist1:
        resultlist1.append(i**2)
    return resultlist1
    
squaredlist1 = squarelist()
print(squaredlist1)



def squarelistusingyeild():
    numberlist2 = [1,2,3,4,5]
    for i in numberlist2:
        print("Called" + str(i))
        yield (i**2)

squaredlist2 = []
gen = squarelistusingyeild()


print(gen.next())
print(gen.next())
print(gen.next())
print(gen.next())
print(gen.next())
