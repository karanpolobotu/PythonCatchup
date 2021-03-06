# duplicate zeroes with in-place operations (Arrays 101)

class Solution:
    # in place solution Accepted by compiler
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        newArr = []
        for i in arr:
            if i == 0:
                newArr.append(i)
                newArr.append(i)
            else:
                newArr.append(i)

        for i in range(len(arr)):
            arr[i] = newArr[i]


        return arr


if __name__ == "__main__":
    test_arr = [1,0,2,3,0,4,5,0]
    test_obj = Solution()
    print(test_obj.duplicateZeros(test_arr))
