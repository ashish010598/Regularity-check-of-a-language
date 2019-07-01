class Char:
	'''Class which defines any character in the string of a language inclusive of its
	power, whether or not the power is a constant or a variable, etc'''
	def __init__(self, base, exp, isVar, rangeOfVar = None):
		self.base = base
		self.exp = exp
		self.isVar = isVar
		# self.rangeOfVar = rangeOfVar

	def __str__(self):
		return str(self.base) + '^' + str(self.exp)

class VarPow:
	'''Defines variable powers of a Character'''
	def __init__(self,coeff,var):
		self.coeff = coeff
		self.var = var

	def __str__(self):
		if self.coeff == 1:
			return str(self.var)
		return str(self.coeff)+(str(self.var))

'''This will define a language i.e. terminals and what form it takes'''
class Language:
	'''Stores a list of Chars to form a language'''
	def __init__(self):
		self.rep = []		#list of characters
		self.rng = []		#string representation of ranges of variables
		self.vars = dict()	#dict of variables mapped to their range

	def appendChar(self, ch = None):
		if ch is None:
			b = input('Enter a character of input: ')
			e = input('Enter its power; enter 1 for once: ')
			v = input('Is the power a constant Y/N: ')
			if v == 'Y':
				v = False
				ex = int(e)
				r = None
			else:
				v = True
					#this means that the exponent also has a coefficient
				try:
					if len(e) > 1:
						cf,e = int(e[:-1]),e[-1]		#the coefficient and the variable
						ex = VarPow(cf,e)
					else:
						ex = VarPow(1,e)		#no coeff hence it is 1
				except ValueError:
					print('Invalid coefficient for power!')
			
				if e not in self.vars:		#this is a new variable
					x,y = map(int,input('Enter the staring and ending ' + 
						'values of the variable separated by a space ').strip().split())
					x,y = min(x,y),max(x,y)
					r = range(x,y+1)
					self.vars[e] = r 		#add new entry to the dict
					self.rng.append(e + ' in range[' + str(x) + ',' + str(y) + ']')
					# ex = e

			ch = Char(b,ex,v)
			# print(type(ch))
		
		if(isinstance(ch,Char)):
			self.rep.append(ch)
			# print("appended")

	def __str__(self):
		res = []
		for c in self.rep:
			#print all characters
			res.append(str(c))
		if len(self.rng):
			res.append(';')
			res.extend(self.rng)
		return ' '.join(res)


	def isRegular(self):
		'''Tells whether the language is regular or not'''
		if not self.vars:
			return True			#no variables hence must be regular
		seen = set()
		for ch in self.rep:
			#check each character and see if 2 variables are repeated, if they are,
			#then language cannot be regular else it is
			
			ex = ch.exp 		#get exponent of the character

			# print('the character is',ch)
			#if the exponent is a variable 
			if isinstance(ex, VarPow):
				# print('The variable power is',ex.var)
				# print('Checklist',seen)
				
				if(ex.var in seen):
					return False
				seen.add(ex.var)		#add variable to the checkset
		else:
			return True			#all variables are distinct; language is regular

		
		

if __name__ == '__main__':
	#main will ask user to create a language by appending characters and in the end will tell if it is regular or not
	
	import sys
	#input output redirection
	# sys.stdin = open('input','r')
	# sys.stdout = open('output','w')

	#create a new language
	l = Language()

	for t in range(int(input('Enter the number of characters your language has: '))):
		l.appendChar()

	print("\nThe language you entered is:")
	print(l)
	print()
	if l.isRegular():
		print('The language is regular')
	else:
		print('The language is not regular')

