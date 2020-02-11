# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        print(s[::2], s[1::2])
        
