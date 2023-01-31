
import statistics
lst=[]
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
for i in range(len(months)):
    elements=input("Enter Rainfall in {} :".format(months[i]))
    lst.append(int(elements))
# print(lst)


dic=dict(zip(months,lst))
# print(dic)



sorted_dict=dict(sorted(dic.items(),key=lambda x:x[1]))
# print(sorted_dict)

keys=[]
for i in sorted_dict.keys():
    keys.append(i)
# print(keys)


lst.sort()
print("\nMax Rainfall:",lst[-1],"mm in",keys[lst.index(max(lst))])
print("\nMin Rainfall:",lst[0],"mm in",keys[0])


Sum=0
for i in lst:
    Sum+=i
avg=Sum/len(lst)
print("\nAverage:",avg,"mm")


print("\nStandard Deviation: {}mm\n".format(statistics.stdev(lst)))