'''Converting Fahrenheit and Celsius'''

def celsius(n):
	return str((n*(9/5))+32)+"°F"
def fahrenheit(n):
	return str((n-32)*(5/9))+"°C"

n=int(input("Value: "))
temp={
	"Celsius":celsius(n),
	"Fahrenheit":fahrenheit(n)
}
print(temp[input("Celsius or Fahrenheit? ")])
