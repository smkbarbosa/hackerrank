
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())

    p = dict(str(input()).split() for _ in range(n))

    for k, v in p.items(): 
        if str(input()) in p.keys():
            print(k + '=' + v) 
        else:
            print('Not found')
        continue