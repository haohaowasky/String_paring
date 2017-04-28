
def isIsomorphic(s, t):
    check_index = []
    check_index2 = []
    k = 0
    j = 0
    counter = 0
    ref = len(s)
    while counter != ref:
        if s[counter] in s[0:(counter)]:
            print(s[0:(counter)])
            check_index.append(check_index[s.index(s[counter])])
        else:
            k += 1
            check_index.append(k)
            print(check_index)
            
        if t[counter] in t[0:(counter)]:
            print(t[0:(counter)])

            check_index2.append(check_index2[t.index(t[counter])])
        else:
            j +=1
            check_index2.append(j)
            print(check_index2)
            
        if check_index != check_index2:
            return False
        counter += 1
    return True

s = "apple"
t = "pipul"

isIsomorphic(s, t)
