# Given a number N, print the product of the digits
def GetProduct(n):
  product=1
  while(n>0):
    product=product*(n%10)
    n=n//10
  return product

n=int(input())
print(GetProduct(n))
