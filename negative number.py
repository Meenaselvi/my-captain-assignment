#search for usage of negative numbers as index
test_list=[5,7,8,2,3,5,1]
print("the original list is:"+str(test_list))
k=3
res=~test_list[::-1].index(k)
print("the required negative index:"+str(res))