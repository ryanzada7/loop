tentativa = 1

while tentativa <= 3:
   senha = input("Digite a senha: ")
   if senha == "senha123":
       print("Acesso concedido")
       break
   else:
       print("Senha incorreta, Tente novamente.")
else:
    print("Você execedeu o número maximo de tentativas.")