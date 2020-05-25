from collections import Counter

A = [2,5,1,2,5]

B = [10,5,2,1,5,2]



ca = Counter(A)

cb = Counter(B)

print(ca,cb)

i,j = 0,0

ans = 0

while(i< len(A) and j < len(B)):

	if(A[i] == B[j]):
		ans += 1


	ca[A[i]] -= 1
	cb[A[j]] -= 1
