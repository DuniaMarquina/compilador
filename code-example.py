print('LET\'S TRY THIS \\OUT')
  
#Comment here
def x(a):
    print('called with',a)
    if a == 1:
        return 2
    if a*2 > 10:
        return 999 / 4
        # Another comment here

    return a+2*3

print('mutiline-expression', "ints")

t = 4+1/3*2+6*(9-5+1)
print('predence test; should be 34+2/3:', t, t==(34+2/3))

print('numbers', 1,2,3,4,5)
if 1:
   8
   a=9
   print(x(a))

print(x(1))
print(x(2))
print(x(8),'3')
print('this is decimal', 1/5)

print(t,a)
a,t = t,a
print(t,a)
