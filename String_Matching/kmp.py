#to calculate the lps(longest prefix also suffix)

def lps_(p):
    m = len(p)
    i = 0
    j = 1
    lps = [0]

    while j < m:
        if p[i] == p[j]:
            i += 1
            lps.append(i)
            j += 1
        
        else:
            if i == 0:
                #p[i] != p[j]
                #and we are at index 0
                lps.append(0)
                j += 1
            
            else:
                i = lps[i-1]
            
    return lps


#pattern matching

def search(p, t):
    lps = lps_(p)
    ans = []
    i = 0
    j = 0
    m = len(p)
    n = len(t)
    while i < n:
        if t[i] == p[j]:
            i += 1
            j += 1

            if j == m:
                ans.append(i-m)
                #now where will j go
                j = lps[j-1]
        
        else:
            if j == 0:
                i += 1

            else :
                j = lps[j-1]
    
    return ans

    


output = search(t = "geeksforgeeks",p = "geek" )
print(output)
