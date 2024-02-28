import psycopg2
import time
from datetime import datetime, timedelta
from typing import Any, Dict
import psycopg2
from typing import List
from database import Database
db = Database()

DATABASE_URL = 'postgres://u7otnm13nnd4qk:pfd93246f9d588bdb2b72388658106129b3764ba94225d194615dcacb54c4f57b@ec2-18-211-151-217.compute-1.amazonaws.com:5432/dbqa84q6ucs4j3'

#'postgres://u7otnm13nnd4qk:pfd93246f9d588bdb2b72388658106129b3764ba94225d194615dcacb54c4f57b@ec2-18-211-151-217.compute-1.amazonaws.com:5432/dbqa84q6ucs4j3'
#'postgres://u1kj5hat49juka:p4fb05fccb4f3d517071fe75eebe5058088ab58eed5854383632e38923a14076e@ec2-44-217-180-173.compute-1.amazonaws.com:5432/d38i356r9ap828'

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

base = """CREATE TABLE "base" (
    chat_id BIGINT PRIMARY KEY,
    id BIGINT
);"""

trend_data = """CREATE TABLE "trend_data" (
    chat_id BIGINT PRIMARY KEY,
    address TEXT,
    symbol TEXT,
    timer TIMESTAMP,
    position BIGINT
);"""

booktrending = """CREATE TABLE "book" (
    chat_id BIGINT PRIMARY KEY,
    address TEXT,
    duration BIGINT,
    grouplink TEXT,
    lastsession TIMESTAMP,
    position BIGINT,
    value NUMERIC
);"""

buybot = """CREATE TABLE "buybot" (
    chat_id BIGINT PRIMARY KEY,
    token TEXT,
    pair TEXT,
    name TEXT,
    min NUMERIC,
    gifs TEXT,
    emojis TEXT,
    islive TEXT,
    step BIGINT
);"""

payment = 'ALTER TABLE "book" ADD COLUMN value NUMERIC;'
addurl = 'ALTER TABLE "trend_data" ADD COLUMN grouplink TEXT;'
addstep = 'ALTER TABLE "buybot" ADD COLUMN step BIGINT;'
alter = 'ALTER TABLE "Route" ALTER COLUMN last_time TYPE NUMERIC USING EXTRACT(EPOCH FROM last_time);'
altertime = 'ALTER TABLE "Route" ALTER COLUMN last_time TYPE TIMESTAMP USING to_timestamp(duration)'

def create(dat):
    cursor.execute(dat)
    conn.commit()
    print("done")

#create(payment)

def check_expiration():
    try:
        # Get data from the database
        db_data = db.get_all_trending_sub()
        if db_data:
            for db_item in db_data:
                timer = db_item[3]
                date_format = "%Y-%m-%d %H:%M:%S.%f"
                date = datetime.strptime(str(timer), date_format)
                current_date = datetime.now()
                if current_date > date:
                    print("yes it's time")
                    index = db_item[-1]
                    db.del_trend(index)
                else:
                    print("not time")
                    print("")
                    pass
        else:
            pass
    except Exception as B:
        print("exp", B)



active_tokens = {}
     
def run_main():
    with Database() as db:
        token_data = db.get_all_tokens()
        #db.del_by_address(None)
                    
        print(f"token_data: {token_data}")
        if len(token_data) > 0:
            for token_info in token_data:
                chat_id, token, pair, act = token_info[0], token_info[1], token_info[2], token_info[7]
                #if token and act == 'YES' and pair is not None:
                    #active_tokens[token] = pair  # Initialize with None
                db.delete_(chat_id)
                
                print('deleted')
                time.sleep(1)
                

                
                           
run_main()
