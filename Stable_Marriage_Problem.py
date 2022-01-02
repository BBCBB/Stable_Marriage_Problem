pref_m = [[4, 2, 3, 1], [2, 1, 3, 4],       # preferences of each male                                         
          [1, 2, 3, 4], [1, 2, 2, 4]]       # pref_m[0][0]=4 means that the firs person (female)
pref_f = [[1, 2, 3, 4], [1, 2, 3, 4],       # from the pref_f list is the last priority of the first male
          [1, 2, 3, 4], [1, 2, 3, 4]]       # preferences of each female
n=len(pref_m)                               # number of couples
class individuals:                          # we form a class for each individual
    def __init__(self,array,gender,label):
        self.array=array                    # the preferences of each individual
        self.gender=gender                  # the gender of each individual
        self.label=label                    # the index of each person in the preferences matrix
memb_m=[0]*n
memb_f=[0]*n
for i in range(len(memb_m)):
    memb_m[i]=individuals(pref_m[i],'male',str(i))  
    memb_f[i]=individuals(pref_f[i],'female',str(i))
    
class Matching:
    def __init__(self):
        self.couples=[]
            
    def update(self,candid):
        cpl=str(candid.gender)+' '+str(candid.label)
        self.couples.append(cpl)
            
q=Matching()
counter=0
while len(memb_m)!=0:
    counter+=1
    for i,r in enumerate(memb_m):
        for j,k in enumerate(memb_f):
            if r.array[j]==min(r.array) and k.array[i]==min(k.array):
                
                q.update(r)
                q.update(k)
                memb_m.pop(i)
                memb_f.pop(j)
                   
                for u in range(len(memb_m)):
                    memb_m[u].array.pop(j)
                    memb_f[u].array.pop(i)
    if counter>n**2:
        print("No matching is made")
        break           
for y in range(0,len(q.couples)-1,2):
    print(q.couples[y]+ '  ' +q.couples[y+1])