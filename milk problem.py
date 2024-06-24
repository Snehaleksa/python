a=100
b=200
L=int(input('Enter Litter'))
if L<=a:
   print('The cost of milk',L*15)
elif L<=b:
   print('The cost of milk ',a*15+(L-a)*20)
elif L<=300:
   print('The cost of milk',a*15+a*20+(L-b)*25) 
else:
   print('Out off stock')     
     

