print('''You are at school. The teacher asks you to get a chair from the storage room.
You leave the classroom. You enter a dark storage room with two doors. 
Do you go through door #1 or door #2?''')

door = input('> ')

if door == '1':
    print("There is a giant bear here eating a cheese cake.'")
    print('What do yo do?')
    print('1. Talk to the bear.')
    print('2. Take the cake.')
    
    bear = input('> ')
    
    if bear == '1':
        print('The bear hits you on the head. You fall asleep. The teacher finds you sleeping in the storage room. Good job.')
    elif bear == '2':
        print('The bear eats your legs. Good job.')
    else:
        print(f'Well, choosing to {bear} is a good idea.')
        print('The bear runs away. Behind the bear is a chair for your classroom.')
            
elif door == '2':
    print("You open the door and see your mother. She is angry.")
    print('1. You run away.')
    print('2. You hide.')
    print('3. You think you are dreaming and close your eyes.')
    print('4. You sit down and cry.')
    
    insanity = input('> ')
    
    if insanity == '1' or insanity == '2':
        print('You mother runs fast and catches you. She is angry because you are not in class. She tells the teacher to give you lots of homework.')
        print('Good job!')        
    elif insanity == '3':
        print('You close your eyes. You open your eyes. Your mother is still there. She is angry because you are not in class. She tells the teacher to give you lots of homework.')
        print('Good job!')
    else:
        print('You realize that the woman is not your mother. She is the school nurse. Next to the nurse is a chair for the classroom.')   
            
else:
    print('You walk around and fall asleep. The teacher finds you sleeping in the toilet. Good job!')
