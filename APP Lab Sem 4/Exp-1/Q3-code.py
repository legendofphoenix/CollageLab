def TowerOfHanoi(n,start,end,middle): 
    if n==1: 
        print("Move disk",n,"from tower",start,"to tower",end)  
        return
    TowerOfHanoi(n-1, start, middle, end) 
    print("Move disk",n,"from tower",start,"to tower",end) 
    TowerOfHanoi(n-1, middle,end,start) 
TowerOfHanoi(4,'A','C','B')  
