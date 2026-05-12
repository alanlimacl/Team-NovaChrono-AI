from banco_dados.conexao import engine
from sqlalchemy import text

def adicionar(valor: float, item: str, categoria: str, metodo_pagamento: str, data: str, id_usuario: int = 1):
    """
    Adiciona um novo registro de gasto na tabela 'financas' do banco de dados.

    A função insere um gasto contendo valor, descrição do item, categoria,
    método de pagamento, data e o identificador do usuário responsável.

    Args:
        valor (float): Valor do gasto.
        item (str): Nome ou descrição do item comprado.
        categoria (str): Categoria do gasto (ex: alimentação, transporte, lazer).
        metodo_pagamento (str): Forma de pagamento utilizada (ex: dinheiro, crédito, pix).
        data (str): Data do gasto no formato definido pela aplicação (ex: 'YYYY-MM-DD').
        id_usuario (int, optional): Identificador do usuário no sistema. Padrão é 1.

    Returns:
        str | tuple: Retorna mensagem de sucesso caso o gasto seja adicionado corretamente.
        Em caso de erro, retorna uma tupla contendo a mensagem de erro e a exceção.
    """
    
    try:
        query = text(
            """INSERT INTO financas (valor, item, categoria, metodo_pagamento, data, id_usuario) 
        VALUES (:valor, :item, :categoria, :metodo_pagamento, :data, :id_usuario)""")
        
        with engine.begin() as conexao:
            conexao.execute(
                query, {
                    'valor':valor,
                    'item': item,
                    'categoria': categoria,
                    'metodo_pagamento': metodo_pagamento,
                    'data':data,
                    'id_usuario': id_usuario
                }
            )
        
        return f"Gastos '{item}' no valor de R$ {valor:.2f}, adicionado com sucesso!"
    
    except Exception as e:
        return 'Erro ao adicionar gasto no Banco de Dados:', e
    

if __name__ == "__main__":
    print(adicionar(valor=7, item="Beiju", categoria='Alimentação', metodo_pagamento='Pix', data='2026-04-14'))
        