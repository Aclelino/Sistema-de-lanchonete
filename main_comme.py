import sqlite3
import time
from ecomme import *
import getpass

conn = sqlite3.connect('banco.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS usuario( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,user TEXT NOT NULL ,senha TEXT NOT NULL)')

def criar_user(x,y):
    c.execute("INSERT INTO usuario(user,senha)VALUES(?,?)",(x,y))
    conn.commit()
    print("criado com sucesso")
    sistem()
    
def entrar(x,y):
    a = c.execute("SELECT * FROM usuario")
    for i in a:
        user =  i[1]
        pss = i[2]
        
        d = x in user
        e = y in pss
        
        if "" != x and y != "" :
        
    
            if d == True and e == True:
                print("\n👮‍♂️Usuario:\033[1;31m ${} Conectado🔵 \033[1;97m".format(user))
                c.close()
                menu()
                
                
            else:
                print("⚠️ Usuario ou Senha inválido ⚠️")
                
        else:
            print("Digite um Usuario e Senha")
            sistem()
            
def sistem():
    
    menu = str(input("______________________________\n\n \033[1;104m SISTEM LANCHE 1.0 \033[1;40m \n\n[1]➡️Entrar \n[2]👮‍♂️Criar conta\n\n______________________________\n[ENTER]SAIR\n"))
    if menu =='1':
        x = str(input("Usuario: "))
        y = getpass.getpass(prompt ="Senha: ",stream=None)
        print("\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n")
        entrar(x,y)
        
    elif menu =='2':
        x = str(input("Usuario: "))
        y = getpass.getpass(prompt ="Senha: ",stream=None)
        criar_user(x,y)
        
    elif menu =="":
        print("Bye")
        exit()
        

if sistem() == True:
    sistem()
