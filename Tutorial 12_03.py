class shape:
	def no_of_sides(self):
		print('Sides of shape class')
	def two_dim(self):
		print('2 dim of shape class')

class square(shape):
	def no_of_sides(self):
		print('4 Sides of square class')
	def color(self):
		print('Color of square class')

sq=square() 
sq.no_of_sides() 
sq.two_dim() 
sq.color()

sh=shape() 
sh.no_of_sides() 
sh.two_dim()