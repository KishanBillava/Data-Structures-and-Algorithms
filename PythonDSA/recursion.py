def funcOne():
    funcTwo()
    print('One')

def funcTwo():
    funcThree()
    print('Two')

def funcThree():
    print('Three')

funcOne()