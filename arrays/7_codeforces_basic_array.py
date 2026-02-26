import sys
def reverse_array():
    # Read integer N
    n = int(input())

    # Read the array
    arr = list(map(int, input().split()))

    # Print in reverse order using loop
    for i in range(n - 1, -1, -1):
        print(arr[i], end=" ")

def p02():
    sys.stdin = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/input.txt", "r")
    sys.stdout = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/output.txt", "w")

    n = int(input())
    arr = list(map(int, input().split()))
    between = list(map(int, input().split()))
    add = 0
    for i in range(between[0], between[1]+1):
        add += arr[i]
    print(add)

def way_too_long_words():
    sys.stdin = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/input.txt", "r")
    sys.stdout = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/output.txt", "w")

    n = int(input())
    for i in range(n):
        x = input()
        if len(x) > 10:
            print(x[0] + str(len(x)-2) + x[len(x)-1])
        else:
            print(x)

def petya_and_strings():

    sys.stdin = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/input.txt", "r")
    sys.stdout = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/output.txt", "w")
    s1 = input()
    s2 = input()
    s1 = s1.lower()
    s2 = s2.lower()
    i = 0
    z = len(s1)
    while z > i:
        if s1[i] == s2[i]:
            i += 1
        else:
            if ord(s1[i]) > ord(s2[i]):
                return 1
            else:
                return -1
            break
    return 0

def football():
    sys.stdin = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/input.txt", "r")
    sys.stdout = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/output.txt", "w")
    s = input()
    cnt = 1 # at least one exists
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
            if cnt >= 7:
                print("YES")
                return
        else:
            cnt = 1
    print("NO")
    
def helpful_maths():
    sys.stdin = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/input.txt", "r")
    sys.stdout = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/output.txt", "w")
    s = input().strip()
    digit_extract = s.split('+')
    digit_extract.sort()
    print('+'.join(digit_extract))

def helpful_maths_1():
    #using dictionary
    #only 1, 2, 3 are present so calculate the count of those
    sys.stdin = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/input.txt", "r")
    sys.stdout = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/output.txt", "w")

    s = input().strip()
    count1 = 0
    count2 = 0
    count3 = 0

    for i in range(len(s)):
        if s[i] == '1':
            count1 += 1
        elif s[i] == '2':
            count2 += 1
        elif s[i] == '3':
            count3 += 1
    result = ""
    for _ in range(count1):
        if result:
            result += '+'
        result += '1'
    for _ in range(count2):
        if result:
            result += "+"
        result += '2'
    for _ in range(count3):
        if result:
            result += '+'
        result += '3'
    print(result)
    
def string_task():
    sys.stdin = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/input.txt", "r")
    sys.stdout = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/output.txt", "w")
    s = input().strip()
    s = s.lower()
    result = ''
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'u' or s[i] == 'y' or s[i] == 'o':
             continue
        else:
            z = '.' + s[i]
            result += z
             
        
    print(result)

def cashier():
    sys.stdin = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/input.txt", "r")
    sys.stdout = open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@Jay_Bansal/Array/output.txt", "w")
    

cashier()
# string_task()
# helpful_maths_1()
# football()
# print(petya_and_strings())
# way_too_long_words()
# p02()
# reverse_array()
