J = [
     [
      [0,0,0],
      [1,1,1],
      [0,0,1]
     ],
     
     [
      [0,1,0],
      [0,1,0],
      [1,1,0]
     ],

     [
      [1,1,1],
      [1,0,0],
      [0,0,0]
     ],

     [
      [0,1,1],
      [0,1,0],
      [0,1,0]
     ]
    ]    
    
rawr = []

for x,arrays in enumerate(J[0]):
    for y,blocks in enumerate(arrays):
        print(blocks,' ',x,' ',y)
    