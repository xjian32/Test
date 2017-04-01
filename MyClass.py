#coding=utf-8

mystr = input("请输入你想查询的对象：")

class MyWorld:
	#定义人
	def person(self):
		self.mytalk='可以用语言表达'
		self.mylimbs='可以用肢体语言来表达'
		self.myeyes='可以眉目传情'
		print('因为我是人，所以我%s,%s,%s'%(self.mytalk,self.mylimbs,self.myeyes))
	
	#定义猪
	def pig(self):
		self.mytalk='哼，哼，哼~~'
		self.myspecialty='吃饭&睡觉'
		self.mymaster='谁对我好，谁是我的主人'
		print('我是猪，我的特点是：%s,%s,%s'%(self.mytalk,self.myspecialty,self.mymaster))
		
	#定义公鸡
	def rooster(self):
		self.mywork='天亮时打鸣'
		self.mymotto='闻鸡起舞'
		print('我是公鸡，我可以%s,%s'%(self.mywork,self.mymotto))
	
if __name__=='__main__':
	myworld = MyWorld()
	if mystr=='人':
		myworld.person()
	elif mystr=='猪':
		myworld.pig()
	elif mystr=='公鸡':
		myworld.rooster()
	else:
		print('类中没有该对象')