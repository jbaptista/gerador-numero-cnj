from random import randint

def aleatorio_ndigitos(n):
  return ("{:0"+str(n)+"d}").format(randint(0,int("9"*n)))


def init():
  numero = aleatorio_ndigitos(11) + "819" + aleatorio_ndigitos(4)
  sem_dv = int(numero)*100
  dv = 97 - ((sem_dv-1)%97)
  print(numero[:7] + "{:02d}".format(dv) + numero[7:])

init()
