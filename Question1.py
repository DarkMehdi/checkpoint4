""" a=input(int())
b=input(int())
c=input(int()) """
def compar(a,b,c) :
    if a>=b and a>=c :
        l=a
    elif b>=a and b>=c :
        l=b
    elif c>=a and c>=b :
        l=c
    print(l)
compar(input(int()),input(int()),input(int()))