from fastapi import FastAPI
import psycopg

DB_URL = "postgres://admin:admin@db:5432/main"


app = FastAPI()


@app.get("/")
def read_root():
    try:
        with psycopg.connect("dbname=main user=admin password=admin") as conn:
            print(conn)
            with conn.cursor() as cur:
                cur.execute("""
            CREATE TABLE IF NOT EXISTS pessoa (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                idade INT CHECK (idade >= 0)
            );
            """)
                conn.commit() 
                conn.close()

    except Exception as e:
        print(e)
        return "Exceção: ", e

    
    return {"Table Pessoa criada"}

@app.post("/asa")
def add_person(name: str, email: str, age: int):
    pass
