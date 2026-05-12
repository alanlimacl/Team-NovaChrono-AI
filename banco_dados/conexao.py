import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# def criar_conexao():
#     try:
#         conexao = engine.connect()
#         print('Conexão com o banco bem-sucedita!')
#         return conexao
    
#     except Exception as e:
#         print(f"Erro ao conectar ao banco: {e}")


# if __name__ == "__main__":
#     criar_conexao()