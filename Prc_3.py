# coding:utf-8
# 二分法

def sqrt_func(x, small):
	
	assert x>=0
	assert small>0

	loops = 0
	low = 0.0
	high = max(x, 1)

	while True and loops<=100:
		guess = (high + low)/2

		if abs(guess**2-x)<small:
			break
		elif guess**2<x:
			low = guess
		else: 
			high = guess

		print (low, high, guess,x)
		loops += 1

	return guess

if __name__ == '__main__':
	
	small_value = 0.00001
	test_date = [10,0.5,32,5,20]

	for x in test_date:
		y = sqrt_func(x, small_value)
		assert abs(y**2-x)<small_value, "Error"


	print ("Pass")