def main():
  num1 = int(input("digite um número: "))
  num2 = int(input("digite outro número: "))
  soma = num1 + num2
  sub = num1 - num2 
  mult = num1 * num2
  if num2 == 0:
    div = "impossível dividir por zero"
  else:
    div = num1 / num2
  
  print("soma de ", num1, " + ", num2, " = ", soma)
  print("A subtração de ", num1, " - ", num2, " = ", sub)
  print("A multiplicação de ", num1, " * ", num2, " = ", mult)
  print("A divisão de ", num1, " / ", num2, " = ", div)

  return 0
main()

