class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        work = [0]
        ans = []
        if (False):
            b = L0238(nums,ans,work,"Brute Force")
        if (False):
            b = L0238(nums,ans,work,"Use Division")
        if (True):
            b = L0238(nums,ans,work,"n time n space")
        if (False):
            b = L0238(nums,ans,work,"n time 1 space")
        return ans

class L0238:
    def __init__(self,a: List[int],ans: List[int], work:'list of size 1', alg:'string') -> None:
        self._a = a ## Data
        self._ans = ans ## answer
        self._work = work
        self._l = len(a)
        for i in range(self._l):
            self._ans.append(0) ## Data is allocated and initialized to 0
        Algorithm(self,alg)

    def __len__(self):
        return self._l;

    def getdata(self,i:'int')->'int':
        assert(i >= 0 and i < self._l)
        self._work[0] = self._work[0]+1 
        return self._a[i]

    def getans(self,i:'int')->'int':
        assert(i >= 0 and i < self._l)
        self._work[0] = self._work[0]+1 
        return self._ans[i]

    def setans(self,i:'int',v:'int')->'None':
        assert(i >= 0 and i < self._l)
        self._work[0] = self._work[0]+1 
        self._ans[i] = v 

class Algorithm:
    def __init__(self,s:'L0238', alg:'string') -> None: 
        self._s = s
        if (alg == "Brute Force"):
            self._nsquare_time_constant_space()
        elif (alg == "Use Division"):
            self._n_time_constant_space_with_divison()
        elif (alg == "n time n space"):
            self._n_time_n_space()
        elif (alg == "n time 1 space"):
            self._n_time_1_space()
        else:
            assert(False)
    
    def _nsquare_time_constant_space(self):
        n = len(self._s)
        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= self._s.getdata(j)
            self._s.setans(i, product)
        
    def _n_time_constant_space_with_divison(self)->'None':
        n = len(self._s)
        total_product = 1
        zero_count = 0
    
        for i in range(n):
            val = self._s.getdata(i)
            if val == 0:
                zero_count += 1
            else:
                total_product *= val

        for i in range(n):
            val = self._s.getdata(i)
            if zero_count > 1:
                self._s.setans(i, 0)
            elif zero_count == 1:
                self._s.setans(i, total_product if val == 0 else 0)
            else:
                self._s.setans(i, total_product // val)

    def _n_time_n_space(self)->'None':
        n = len(self._s)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * self._s.getdata(i - 1)

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * self._s.getdata(i + 1)

        for i in range(n):
            self._s.setans(i, left[i] * right[i])
        
    def _n_time_1_space(self)->'None':
        n = len(self._s)
        # First pass: compute prefix products
        prefix = 1
        for i in range(n):
            self._s.setans(i, prefix)
            prefix *= self._s.getdata(i)

        # Second pass: compute suffix products and multiply
        suffix = 1
        for i in range(n - 1, -1, -1):
            val = self._s.getans(i)
            self._s.setans(i, val * suffix)
            suffix *= self._s.getdata(i)