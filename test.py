#função que codifica em delta um array de inteiros
#buffer: array de inteiros
#length: tamanho do array
#retorna o ultimo valor do array


def delta_encode(list):
  last = 0
  array = []
  for i in list:
    if last == 0:
      array.append(i)
      last = i
    else:
      array.append(last - i)
      last = last - i
  return array


print(delta_encode([13, 10, 5, 1, 32]))


def delta_decode(lista):
  last = 0
  array = []
  lista = list(lista)
  # lista.reverse()
  for i in lista:
    if last == 0:
      array.append(i)
      last = i
    else:
      array.append(last + i)
      last = last + i
  return array


print(delta_decode([13, 3, -2, -3, -35]))
