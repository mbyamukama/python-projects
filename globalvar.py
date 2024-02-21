newnums=[]
def run(list_of_integers):
  """write your code here."""
  for num in list_of_integers:
      if num%2==0 and list_of_integers.index(num)%2==0:
        print(num)
        newnums.append(num)
  return newnums
  
x = run([ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ])
print(x)
