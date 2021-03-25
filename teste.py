from models.cliente import Cliente
from models.conta import Conta


abc: Cliente = Cliente('abc', 'abc@d.com', '123.123.123-12', '01/01/0001')
defg: Cliente = Cliente('defg', 'defg@h', '456.745.674-56', '02/02/0002')

# print(abc)
# print(defg)

contaa: Conta = Conta(abc)
contad: Conta = Conta(defg)

# print(contaa)
# print(contad)
