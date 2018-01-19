import psycopg2

cnx = psycopg2.connect(user='postgres', password='123',
                              host='localhost', database='teste')
cur = cnx.cursor()

def makeMedia():
    count = 0
    valor = 0
    query = "select id_customer, vl_total from tb_customer_account"
    cur.execute(query)
    resu = cur.fetchall()
    for res in resu:
        if res[1] > 560 and (res[0] > 1500 and res[0] < 2700):
            count += 1
            valor += res[1]
            
    return str(valor/count)

def SelectTabela():
    query = "select * from tb_customer_account where vl_total > 560 and id_customer > 1500 and id_customer < 2700 order by vl_total desc;"
    cur.execute(query)
    return cur.fetchall()

def InsertBanco(idc,cpf,nomec,acti,vlt):
    query = 'INSERT INTO tb_customer_account (id_customer, cpf_cnpj, nm_customer,is_active,vl_total) VALUES (%s,%s,%s,%s,%s)'
    query_d = (idc,cpf,nomec,acti,vlt)
    cur.execute(query,query_d)
    cnx.commit()


print("Teste Backend - Willian Inocencio")

op = input("Deseja cadastrar? (Sim = 1)")
while op == "1":
    
    idc = input("Insira o id do cliente:")
    cpf = input("Insira o CPF ou CNPJ do cliente:")
    nomec = input("Insira o nome do cliente:")
    acti = input("Cliente ativo? (True/False)")
    vlt = input("Saldo do cliente:")
    InsertBanco(idc,cpf,nomec,acti,vlt)
    op = input("Deseja cadastrar mais um? (Sim = 1)") #Arrumar 

       
print("Media Final: " + makeMedia())

resu = SelectTabela()
print("----------------------------------------------------")

for res in resu:
    print("| " , res[0] , " | " , res[1] , " | " , res[2] , " | " , res[3] , " | " , res[4] , " |")
    
print("----------------------------------------------------")
cnx.close()




