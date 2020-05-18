def checkInclusion(s1, s2):
    A = [ord(x) - ord('a') for x in s1]
    B = [ord(x) - ord('a') for x in s2]
    
    
    target = [0] * 26
    for x in A:
        target[x] += 1
    
    window = [0] * 26
    
    print(A,B,window)
    for i, x in enumerate(B):
        window[x] += 1
        if i >= len(A):
            print(i,len(A),B[i - len(A)])
            window[B[i - len(A)]] -= 1
        if window == target:
            return True
    return False


print(checkInclusion("ab","bdfdfddfba"))