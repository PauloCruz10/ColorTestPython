conta = 0
class Funct:
	"""simple example class"""
	i=1234

	def incrementConta(self):
		self.i =10
		return self.i


def main():
	first = Funct()
	ola = first.incrementConta()
	print("O resultado é : %s" %ola)

if __name__ == '__main__':
	main()