
import time
#from main_comme import sistem
import sqlite3
import pandas as pd

conn = sqlite3.connect('banco.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS dados(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,preco INTEGER NOT NULL)')


def inserir(x,y):
    
    c.execute("INSERT INTO dados(nome,preco)VALUES(?,?)",(x,y))
    conn.commit()
    print('Salvo com Sucesso !')
    
    print("\n[q]SAIR\n[ENTER]RETORNA\n")
    q =str(input(": ").upper())
    print(q)
    if q =="q":
 
        exit()
    else:
        
        menu()
    
    
def consulta():
    
    #print("_____________________\nID  | NOME | PREÇO ")
    v = c.execute("SELECT * FROM dados")
    dados = []
    for i in v:
        
        b = str(i[0])
        d = str(i[1])
        p = str(i[2])
        #dados.append(b,'  ',d.upper(),' ',p)
        
        dados.append({"Codigo":b,"Nome":d,"Valor" : p})
        
        
    print(pd.DataFrame(dados),columns=False)
    
    print("\n[ENTER]🚪SAIR\n[R]↩RETORNA AO MENU\n")
    q =str(input(": "))
    
    if q =="":
 
        exit()
    else:
        
        menu()  
        
def excluir():
    s = c.execute("SELECT * FROM dados")
    for i in s:
        a = str(i[0])
    ex = input("Qual id do item a exclui ")
    if ex in a:
    
        c.execute("DELETE FROM dados WHERE id={}".format(ex))
        print("excluído com Sucessor!")
        conn.commit()
    else:
         print("Esse id não existe")
     
    print("\n[Q]🚪SAIR\n[R]↩RETORNA AO MENU\n")
    q =str(input(": "))
    
    if q =="q":
 
        exit()
    else:
        
        menu()  
         
    
def editar():
    consulta()
    new = str(input("Nome"))
    n = str(input("Novo nome"))
    
    
    v = c.execute("UPDATE dados SET nome = ? WHERE nome = ?",(n,new))
    conn.commit()
    print("ATUALIZADO COM SUCESSO!") 
    
    print("\n[Q]🚪SAIR\n[R]↩RETORNA AO MENU\n")
    q =str(input(": "))
    
    if q =="q":
 
        exit()
    else:
        
        menu()
     
def menu():
    
    print(" ESCOLHA UMA DAS OPÇOÊS A BAIXO \n")
    print("________________________________\n\n")
         
    while True:
        menu = input("[1]➕ Adicionar  \n[2]🧾 Cardapio \n[3]❌ Excluir\n[4]🔄 Atualizar \n[Q]🚪 Sair \n\n ________________________________\n\n->")
        if menu =="1":
            x = str(input("Nome :"))
            y = float(input("Valor :"))
            inserir(x,y)
        elif menu =="2":
            consulta()
            print("_____________________\n\n")
        elif menu =="3":
            excluir()
        
        elif menu =="4":
            editar()
            print("Alterado com sucesso!")
        
        elif menu =="q":
            break
            
    

