peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = peso / (altura*altura)
if imc <18.5:
    print ("O seu IMC é:","%.2f" % imc)
    print ("Você está abaixo do peso!")
elif imc >= 18.5 or imc <= 24.9:
    print ("O seu IMC é:","%.2f" % imc)
    print ("Você está com o peso normal!")
elif imc >= 18.5 or imc <= 24.9:
    print ("O seu IMC é:","%.2f" % imc)
    print ("Você está com o peso normal!")
elif imc >= 25 or imc <= 29.9:
    print ("O seu IMC é:","%.2f" % imc)
    print ("Você está com sobrepeso!")
elif imc >= 30 or imc <= 39.9:
    print ("O seu IMC é:","%.2f" % imc)
    print ("Você está obeso(a)!")
else:
    print ("O seu IMC é:","%.2f" % imc)
    print ("Você está muito obeso(a)!")