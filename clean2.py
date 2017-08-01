
#edit the list to whatever you would like
a = [30, 34, 75, 27, 8, 58, 10, 1, 59, 2322]
def dropsort(list):
    print list
    if sorted(list) == list:
        print "list is sorted"
        return None
    c = []
    if list[0] < list[1]:
        c.append(list[0])
    else:
       c.append(list[1])
    for x in range(0,len(list) - 1 ):
        if list[x] < list[x+1]:
            c.append(list[x+1])
    dropsort(c)
dropsort(a)
