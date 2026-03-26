import sqlite3

conexao = sqlite3.connect('banco_dados/banco_financas.db')
cursor = conexao.cursor()

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
        query = """INSERT INTO financas (valor, item, categoria, metodo_pagamento, data, id_usuario) 
        VALUES (?, ?, ?, ?, ?, ?)"""
        
        cursor.execute(query, (valor, item, categoria, metodo_pagamento, data, id_usuario),)
        
        conexao.commit()
        conexao.close()
        return f"Gastos '{item}' no valor de R$ {valor:.2f}, adicionado com sucesso!"
    
    except Exception as e:
        return 'Erro ao adicionar gasto no Banco de Dados:', e
        