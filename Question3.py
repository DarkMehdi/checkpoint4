def sum(slist):
    res = 0
    for ele in range(0, len(slist)):
	    res += int(slist[ele])
    
    print(res)
def multi(mlist) :
     
    mres = 1
    for x in mlist:
         mres = mres * int(x)
    print(mres)
listy=[input(int()),input(int()),input(int()),input(int()),input(int())]
listsum=[listy[0],listy[2],listy[4]]
listmulti=[listy[1],listy[3]]
sum(listsum)
multi(listmulti)