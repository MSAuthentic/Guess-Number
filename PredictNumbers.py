import math
from tensorflow import keras
from tensorflow.keras import Sequential, layers
import numpy as np 


train_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
train_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]


model = Sequential([
    layers.Input(shape=(1,)),    
    layers.Dense(10, activation='relu'),
    layers.Dense(1) # linear layer  
])

model.compile(optimizer='sgd',
              loss='mse',
              metrics=['mae'])

model.fit(train_numbers, train_labels, epochs=500)   
test_numbers  =  np.array([train_numbers])

arr = []
test_number = np.mean(test_numbers)

blnGuessed = False

def GetGuessingNumber():
    arr = []
    with open(r'ML\Excercises\10\Guessing.csv') as f  :
        for i in f:
            d = i.replace('\n','')
            arr.append(int(d)) 
        return arr
        
def WriteNotGuessed(arr,res):
    with open(r'ML\Excercises\10\Guessing.csv','w') as file:
            try:
               arr.append(int(res))
               for i in arr: 
                    file.write(str(i) +'\n')
            except  Exception as e:
                print(e)       
                 
while blnGuessed == False:     
   
    arr= GetGuessingNumber()    
    test_number = np.bincount(arr).argmax()
    
    test_number = np.array([int(test_number)])
    predictions = model.predict(test_number)
    
    print('The number you thinked could be approximated in: ' + str(int(math.ceil(predictions))))
    
    res = input('Did i guess? y/n |  ')
    
    if res == 'y':    blnGuessed=True  
    elif res == 'n':       
        
        res= input('Write the number you thinked! ')
        
        WriteNotGuessed(arr,res)
        
    else: print('ERROR! ')

        
    