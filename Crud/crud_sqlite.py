import sqlite3

conexao_global = None
cursor = None

def conecta_db():
    conexao = sqlite3.connect("Crud/db_teste.db")

    if conexao:
        print ("Conectado com sucesso!")
       
        global cursor
        cursor = conexao.cursor()
        
        global conexao_global
        conexao_global = conexao
        return conexao

def desconecta_db(con):
    con.close()



def cadastra_cliente(nome, email):
   
    cursor.execute(f"INSERT INTO contatos(nome,email) VALUES ('{nome}','{email}')")
    conexao_global.commit()
    
def seleciona_todos_clientes():
    cursor.execute("Select * from contatos;")
    contatos_cadastrados = cursor.fetchall()


    print(contatos_cadastrados)

    conexao_global.commit()

def apagar_por_id(id):
    cursor.execute(f"DELETE FROM contatos where id={id}")
    conexao_global.commit()

def atualiza_por_id(id,valor):
    cursor.execute(f"UPDATE contatos SET nome= '{valor}' where id = {id}")

if __name__ == "__main__":
    conecta_db()
    #cadastra_cliente("Owaldo", "daniel@daniel.com")
    #apagar_por_id(1)
    #atualiza_por_id(2,'Wilson')
    #seleciona_todos_clientes()
   # desconecta_db(con)