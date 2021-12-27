saláriot = float(input("Qual o salário do trabalhador?"))
reajuste1 = 20 / 100
reajuste2 = 15 / 100
reajuste3 = 10 / 100
reajuste4 = 5 / 100
if saláriot <= 280:
    saláriot + reajuste1*saláriot
elif 280 <= saláriot <= 700:
    saláriot + reajuste2*saláriot
elif 700 <= saláriot <= 1500:
    saláriot + reajuste3*saláriot
elif saláriot >= 1500:
    saláriot + reajuste4*saláriot

print(saláriot)
print(reajuste1)
print(reajuste2)
print(reajuste3)
print(reajuste4)
aumento1 = saláriot*reajuste1
aumento2 = saláriot*reajuste2
aumento3 = saláriot*reajuste3
aumento4 = saláriot*reajuste4
print(aumento1, aumento2, aumento3, aumento4)

novo_salário1 = saláriot + aumento1
novo_salário2 = saláriot + aumento2
novo_salário3 = saláriot + aumento3
novo_salário4 = saláriot + aumento4

print(novo_salário1, novo_salário2, novo_salário3, novo_salário4)