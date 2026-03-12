#string matching
def zarr(s):
    L = 0
    R = 0
    n = len(s)
    z = [0] * n
    for i in range(1,n):
        if i > R:
            L = R = i
            while(R < n and s[R-L] == s[R]):
                R += 1
            z[i] = R - L
            R -= 1
        
        else:
            if z[i - L] + i <= R:
                z[i] = z[i-L]
            
            else:
                L = i
                while(R < n and s[R - L] == s[R]):
                    R += 1
                z[i] = R - L
                R -= 1
    return z

output = zarr("geek#geeksforgeeks")
print(output)
pattern = "geek"
stri = "geeksforgeeks"
ns = pattern + "#" + stri
z = zarr(ns)

ans = []

for i in range(0,len(z)):
    if z[i] == len(pattern):
        ans.append(i-len(pattern)-1)
print(ans)


