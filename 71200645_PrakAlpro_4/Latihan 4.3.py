fahrenheit = lambda celcius: "F = " + str(int((9/5) * celcius + 32))
reamur = lambda celcius: "R = " + str(int(0.8 * celcius))

celcius1 = 100
fahrenheit1 = fahrenheit(celcius1)
print("Input C =", celcius1, " Output F =", fahrenheit1)

celcius2 = 80
reamur2 = reamur(celcius2)
print("Input C =", celcius2, " Output R =", reamur2)

celcius3 = 0
fahrenheit3 = fahrenheit(celcius3)
print("Input C =", celcius3, " Output F =", fahrenheit3)