import sys

counterc = 0
counterl = 0
counterv = 0
countert = 0

for c in sys.stdin.read():
	counterc += 1
	

	if c == '\n':
		counterl += 1
	if c in 'aeiouAEIOUàèéíóü':
		counterv += 1
	if c == ' ':
		countert += 1
		
		



print(counterc)
print(counterl)
print(countert)
print(counterv)

	
