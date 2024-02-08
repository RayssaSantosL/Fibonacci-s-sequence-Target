#definindo a sequencia de Fibonnacci
def fib(x):
  seq_fib = [0, 1]
  while seq_fib[-1] < x:
    seq_fib.append(seq_fib[-1] + seq_fib[-2])
  return seq_fib


#definindo se o número em questão pertence ou não a sequencia 
def pertence (num):
  seq_fib = fib(num)
  if num in seq_fib:
    return True
  else:
    return False

#usuário quem irá definir valores:
num_user = int(input("Digite um valor: "))

#processo de verificação:
if pertence (num_user):
  print("O numero ", num_user, "pertence sim a sequencia de Fibonacci.")
else:
  print("O numero ", num_user, "não pertence a sequencia de Fibonacci.")
