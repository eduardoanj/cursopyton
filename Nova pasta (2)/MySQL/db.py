import MySQLdb 

conexao_mysql = MySQLdb.connect(host='localhost', database='invest', user='root', passwd='')
nome_da_aplicação = 'suco de abacaxi'

cursor = conexao_mysql.cursor()
                #usar aspas duplas quando interpolar strings  
                
#cursor.execute("insert into bebidas(tipo) values({})".format(nome_da_bebida))
#necessario o commit para as atualizações na tabelo do my sql sejam atualizadas
#conexao_mysql.commit()
cursor.execute('select * from tipo where id=5')

for b in cursor.fetchall():
    print(b) 