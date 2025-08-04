l = ['a','b','cd']

def rm_list(l,word):
    for word in l:
        
        l.remove(word)
        return l
    

print(rm_list(l,'a'))
    