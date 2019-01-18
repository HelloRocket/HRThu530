print('''You are at school. the teacher askes you to get a chair from the storage room.
you keave the classroom. You enter a dark storage room with two doors. 
Do you go through door #1 or door #2?''')

door = input('> ')

if door == '1':
    print("There's a giant bear here eating a cheese cake.'")
    print('What do yo do?')
    print('1. Take the cake.')
    print('2. Talk to the bear.')
    
    bear = input('> ')
    
    if bear == '1':
        print('The bear eats your Head. Good job.')
    elif bear == '2':
        print('The bear eats your legs. Good job.')
    else:
        print(f'Well, choosing to {bear} is a good idea.')
        print('The bear runs away. Behind the bear is a chair for your classroom.')
            
elif door == '2':
    print("You look into the eyes of a scary clown. your go crazy!")
    print('1. Blueberries are flying.')
    print('2. My brain is pink.')
    print('3. Understanding English singing tanuki songs.')
    print('4. There is no clown. There is no clown.')
    
    insanity = input('> ')
    
    if insanity == '1' or insanity == '2':
        print('Your body is alive but your mind is jelly.')
        print('Good job!')        
    elif insanity == '3' or insanity == '4':
        print('You close your eyes. You open your eyes. The scary clown eats you.')
        print('Good job!')
    else:
        print('The clown is a picture on the wall. Next to the picture is a chair for the classroom.')   
    
        
else:
    print('You walk around and fall asleep. The teacher finds you sleeping in the toilet. Good job!')
