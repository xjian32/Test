# coding:utf-8

def test_1():
    '''
    1,2,3,4组成无重复的三位数
    '''
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                if (a!=b) and (b!=c) and (a!=c):
                    print(a,b,c)
    print('\n------------test_1 END---------------\n')

def test_2():
    '''
	企业发放的奖金根据利润提成
	利润(I)低于或等于10万元时，奖金可提10%；利润(I)≤10万 ————10%
	利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
	20万到40万之间时，高于20万元的部分，可提成5%；
	40万到60万之间时高于40万元的部分，可提成3%；
	60万到100万之间时，高于60万元的部分，可提成1.5%
	高于100万元时，超过100万元的部分按1%提成
	从键盘输入当月利润I，求应发放奖金总数
	'''

    x = int(input('请输入当月利润：'))
    bonus = 0
    if x <= 100000:
        bonus = 0.1*x
        print('应发奖金总数:', bonus, '元')
    elif 100000<x<=200000:
        bonus = 10000+0.075*(x-100000)
        print('应发奖金总数:', bonus, '元')
    elif 200000<x<=400000:
        bonus = 10000+7500+0.05*(x-200000)
        print('应发奖金总数:', bonus, '元')
    elif 400000<x<=600000:
        bonus = 10000+7500+10000+0.03*(x-400000)
        print('应发奖金总数:', bonus, '元')
    elif 600000<x<=1000000:
        bonus = 10000+7500+10000+6000+0.015*(x-600000)
        print('应发奖金总数:', bonus, '元')
    elif x>1000000:
        bonus = 10000+7500+10000+6000+6000+0.01*(x-1000000)
        print('应发奖金总数:', bonus, '元')

    print('\n------------test_2 END---------------\n')


def test_3():
    '''
    输入三个整数x,y,z，请把这三个数由小到大输出
    '''
    list1 = []
    for i in range(3):
        x = int(input('请输入整数: \n'))
        list1.append(x)
    list1.sort()
    print(list1)

def test_4():
    '''
    斐波那契数列
    '''
    a = 1
    b = 1
    for i in range(10):
        a, b = b, a+b
        print(a)

'''

'''

def main():
    for i in range(1, 4):
       func = 'test_{0}()'.format(i)
       exec (func)

if __name__ == "__main__":
    main()
