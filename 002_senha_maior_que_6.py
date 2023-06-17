# Criar uma função para verificar se a senha é maior do que 6 caracteres:

# O parâmetro da função é uma string a função vai retornar verdadeiro ou falso:

def is_acceptable_password(password: str) -> bool:
    if len(password) > 6: # Usando len pra contar quantos caracteres a senha possui.
        return True
    else:
        return False
      # Sendo mais de 6 caracteres retorna True, senão False.

# Aqui testamos, chamando a função com senha curta, longa e média:

assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

# E aqui imprimimos o resultado na tela:

print(is_acceptable_password("short"))
print(is_acceptable_password("muchlonger"))
print(is_acceptable_password("ashort"))

