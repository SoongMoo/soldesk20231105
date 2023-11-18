val = 10
PI = 3.141592

def f1(x):
	return 3 * x + 5

class Calculator:
	def setData(self, first, second): # 멤버필드를 초기화 메소드
		self.first = first
		self.second = second
	def add(self ):
		self.result = self.first + self.second
		return self.result
	def div(self):
		self.result = self.first / self.second
		return self.result

calc = Calculator() # 객체