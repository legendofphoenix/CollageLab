#Question 1
class pairs:
    def zerosum(self,a,n):
        result =[]
        for i in range (0,n-1):
            for j in range (i+1,n):
                if(a[i]+a[j]==0):
                    {
                        result.append([a[i],a[j]])
                    }
        return result
a=[-25,-10,-7,7,10,-3,8,3]
n=len(a)
print(sum().zerosum(a,n))
