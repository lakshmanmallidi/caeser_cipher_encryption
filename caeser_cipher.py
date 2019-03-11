import sqlite3
def getdata(db_file):
    data=[]
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute(sqlite_query_create_table)
        cur.execute(sqlite_query_Get_data)
        rows = cur.fetchall()
        for row in rows:
            #row = ('somevalue',)
            #row[0] = 'somevalue'
            data.append(row[0])
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()
    return data

def decrypt_level_1(encrypt2,key2):
    decrypt1 = []
    for e in encrypt2:
        if(e>96 and e<123):
            if(e-key2>96):
                decrypt1.append(e-key2)
            else:
                diff = 96 -(e-key2)
                decrypt1.append(122-diff)
        elif(e>64 and e<91):
            if(e-key2>64):
                decrypt1.append(e-key2)
            else:
                diff = 64 -(e-key2)
                decrypt1.append(90-diff)
    return decrypt1

def decrypt_level_2(decrypt1,key1):
    decrypt2 = ""
    for e in decrypt1:
        if(e>96 and e<123):
            if(e-key1>96):
                decrypt2 = decrypt2+chr(e-key1)
            else:
                diff = 96 -(e-key1)
                decrypt2 = decrypt2+chr(122-diff)
        elif(e>64 and e<91):
            if(e-key1>64):
                decrypt2 = decrypt2+chr(e-key1)
            else:
                diff = 64 -(e-key1)
                decrypt2 = decrypt2+chr(90-diff)    

    return decrypt2

def encrypt_level_1(text,key1):
    encrypt1 = ""
    for e in text:
        if(ord(e)>96 and ord(e)<123):
            if(ord(e)+key1<123):
                encrypt1 = encrypt1+chr(ord(e)+key1)
            else:
                diff = ord(e)+key1-122
                encrypt1 = encrypt1+chr(96+diff)
        elif(ord(e)>64 and ord(e)<91):
            if(ord(e)+key1<91):
                encrypt1 = encrypt1+chr(ord(e)+key1)
            else:
                diff = ord(e)+key1-90
                encrypt1 = encrypt1+chr(64+diff)
    return encrypt1

def encrypt_level_2(encrypt1,key2):
    encrypt2 = []
    for e in encrypt1:
        if(ord(e)>96 and ord(e)<123):
            if(ord(e)+key2<123):
                encrypt2.append(ord(e)+key2)
            else:
                diff = ord(e)+key2-122
                encrypt2.append(96+diff)
        elif(ord(e)>64 and ord(e)<91):
            if(ord(e)+key2<91):
                encrypt2.append(ord(e)+key2)
            else:
                diff = ord(e)+key2-90
                encrypt2.append(64+diff)
    return encrypt2

sqlite_query_create_table = """CREATE TABLE IF NOT EXISTS DataTable(Id INTEGER PRIMARY KEY AUTOINCREMENT,MsgText TEXT NOT NULL);"""
sqlite_query_Get_data = """SELECT MsgText from DataTable;"""
db_file="msgData.db"
data = getdata(db_file)
key1 = int(input("Enter key for level 1 encryption:"))
key2 = int(input("Enter key for level 2 encryption:"))
for msg in data:
    print("\n-----------------------------------------------------------\n")
    print("Message data:", msg)
    #encryption level 1 which returns encryted string with key1
    encrypt1 = encrypt_level_1(msg, key1)
    print( "encryption level 1:", encrypt1)
    #encryption level 2 which returns encryted string ascii array values with key2
    encrypt2 = encrypt_level_2(encrypt1, key2)
    print( "encryption level 2:", encrypt2)
    #decryption level 1 which returns decryted string ascii array values with key2
    decrypt1 = decrypt_level_1(encrypt2, key2)
    print ("decrypt level 1:", decrypt1)
    #decryption level 2 which returns decrypted string ascii arrray values with key1
    decrypt2 = decrypt_level_2(decrypt1, key1)
    print ("decrypt level 2:", decrypt2)
    print("\n-----------------------------------------------------------\n")
