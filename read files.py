import json

with open('Chemistry.txt', 'rb') as json_file:  
    d = json.load(json_file)

e={}
for j in d:
#    try: print(j)
#    except: print(j.encode("utf-8"))
#    try: print(d[j],end='\n\n')
#    except:
#        for item in d[j]:
#            print(item.encode("utf-8"))
#        print('\n')
    e[j]=len(d[j])
        

e=sorted(e, reverse=True)

print(e[:5])
