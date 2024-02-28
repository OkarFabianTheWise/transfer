import psycopg2
import time
from typing import Any, Dict
import psycopg2
from typing import List
from database import Database
db = Database()

DATABASE_URL = "postgres://ue29je0st80hu7:pd6a85fd8fc47b43589f8ad6bd6a932cdada5ccdcca76b26adc457cd40c9a2264@ec2-54-145-119-10.compute-1.amazonaws.com:5432/d9vv09t3miqm8d"

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

projdata = """CREATE TABLE "project_data" (
    chat_id BIGINT PRIMARY KEY,
    token TEXT,
    key TEXT,
    gif TEXT,
    min_buy NUMERIC,
    islive TEXT
);"""

bnb = """CREATE TABLE "BN" (
    asset TEXT PRIMARY KEY,
    direction TEXT,
    amount NUMERIC,
    positionSide TEXT
);"""

funded = 'ALTER TABLE "project_data" ADD COLUMN isFunded TEXT;'
addtime = 'ALTER TABLE "Route" ADD COLUMN last_time TIMESTAMP;'
alter = 'ALTER TABLE "Route" ALTER COLUMN last_time TYPE NUMERIC USING EXTRACT(EPOCH FROM last_time);'
altertime = 'ALTER TABLE "Route" ALTER COLUMN last_time TYPE TIMESTAMP USING to_timestamp(duration)'

def create(dat):
    cursor.execute(dat)
    conn.commit()
    print("done")

#create(funded)
'''try:
    #db.save_key(666111, '0x22c6d598b3ca6dfd175ef72028255b95d880e4881f8f444b8af6fbe260cd9d3e')
    #print(db.get_user_key(666111))
    #db.delete_users(-1001950984691)
    print(db.get_token_listeners("0x597981EaC8A293054A1826c7b60cBF92972A36C1"))
except Exception as x:
    print(x)'''
#print(db.get_all_chat_id())


'''ids = db.get_all_chat_id()
total = len(ids) - 1
if total > 0:
    print("total:", total)
    winning_num = random.randint(0,total)
    print("winning_num:", winning_num)
    winning_group = ids[winning_num]
    print("winning_group:", winning_group)
    address = db.get_group_token(winning_group)
    print("winning_group:", winning_group)
else:
    print('epmty')'''
    
token_data = db.get_all_tokens()
print("token_data:", token_data)

'''for token_info in token_data:
    chat_id = token_info[0]
    token_address = token_info[1]
    token_key = token_info[2]
    act = token_info[-1]
    if token_address and act == 'YES':
        print("chat_id:", chat_id)
        print("token_address:", token_address)
        print("token_key:", token_key)
        print("act:", act)'''
