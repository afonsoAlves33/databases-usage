from fastapi import FastAPI
import psycopg

DB_URL = "postgres://admin:admin@postgres:5432/main"


app = FastAPI()

def execute_sql_script(script: str, params: tuple = None):
    try:
        with psycopg.connect(DB_URL) as conn:
            print(conn)
            try: 
                with conn.cursor() as cur:
                    cur.execute(script, params)
                    conn.commit()
                    conn.close()
                    return "Success"
            except Exception as e:
                print(e)
                return "Could not execute the script: ", e
    except Exception as e:
        print(e)
        return "Could not connect to the database: ", e
    

@app.get("/")
def read_root():
    try:
        create_table = execute_sql_script( """
        CREATE TABLE IF NOT EXISTS person (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            age INT CHECK (age >= 0)
        );
        """)
        print(create_table)
    except Exception as e:
        print(e)
        return {"Exception": f"{e}"}
    return {"Table Person created"}

@app.post("/insert_person/")
def add_person(name: str, email: str, age: int):
    try:
        insert = execute_sql_script("""
            INSERT INTO person(name, email, age)
            VALUES (%s, %s, %s);
            """, (name, email, age))
        print(insert)
        if insert == "Sucess":
            return {"Sucess"}
        else: 
            return {"Error": str(insert)}
    except Exception as e:
        return {"Exception": f"{e}"}
