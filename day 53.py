# Python3 program to find Maximum Product Subarray

# Returns the product of max product subarray.


def maxSubarrayProduct(arr, n):
	result = arr[0]
	for i in range(n):
		mul = arr[i]
		for j in range(i + 1, n):
			result = max(result, mul)
			mul *= arr[j]
		result = max(result, mul)
	return result

n = int(input("Enter the size of array: "))
arr = []
print("Enter the array elements: ")
for i in range(0,n):
    p = int(input())
    arr.append(p)
print("Maximum Subarray product: ", maxSubarrayProduct(arr, n))
