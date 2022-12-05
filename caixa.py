
import time
import sqlite3
from ecomme import consulta

log = []
conn = sqlite3.connect('banco.db')
c = conn.cursor()

def caixa1(x):
    b = c.execute("SELECT * FROM dados WHERE id = {}".format(x))
    for i in b:
        id = i[0]
        pd = i[1].upper()
        pc = float(i[2])
        print(f'PRODUTO: {pd}\nPREÇO: R${pc}')
        log.append(pc)
        
def somar(self,*args):
    valor = self.pc
    return valor
while True:
    menu = int(input("Código: "))     
    caixa1(menu)
    if menu ==0:
        
        print("Total: R${:.2f}".format(sum(log)))
        receb = float(input("Valor recebido: "))
        troco = sum(log) - receb
        print("Troco R${:.2f}".format(-troco))
        break