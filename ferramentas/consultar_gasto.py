import sqlite3
from typing import Optional

def consultar(data_inicial: str, data_final: str, categoria: Optional[str] = None) -> str:
    """
    Consulta os gastos do usuário em um período específico, com filtro opcional de categoria.
    
    REGRA DE DATAS PARA O AGENTE:
    - O formato OBRIGATÓRIO é 'YYYY-MM-DD'.
    - Se o usuário pedir apenas um dia específico (ex: "hoje" ou "ontem"), passe a MESMA data em 'data_inicial' e 'data_final'.
    - Se o usuário pedir "este mês", calcule o primeiro e o último dia do mês atual.
    
    Args:
        data_inicial (str): A data de início no formato 'YYYY-MM-DD'.
        data_final (str): A data de fim no formato 'YYYY-MM-DD'.
        categoria (str, optional): A categoria do gasto. Deixe em branco se o usuário quiser o geral.
        
    Returns:
        str: Um relatório formatado com os gastos encontrados ou um aviso se estiver vazio.
    """
    try:
        conexao = sqlite3.connect('banco_dados/banco_financas.db')
        cursor = conexao.cursor()
        
        query = "SELECT * FROM financas WHERE data BETWEEN ? AND ?"
        parametros = [data_inicial, data_final]
        
        if categoria:
            query += " AND categoria LIKE ?"
            parametros.append(f'%{categoria}%')
        
        query += " ORDER BY data DESC"
        
        cursor.execute(query, tuple(parametros))
        registros = cursor.fetchall()
        conexao.close()
        
        if not registros:
            if categoria:
                return f"Nenhum gasto encontrado na Categoria '{categoria}' entre {data_inicial} e {data_final}."
            
            return f"Nenhum gasto encontrado entre {data_inicial} e {data_final}."
    
        total_gasto = 0
        resposta = f'💸 Relatório de Gastos ({len(registros)} encontrados):\n\n'
        
        for linha in registros:
            id_gasto, valor, item, categoria_item, metodo_pagamento, data, id_usuario = linha
            
            total_gasto += valor
            
            resposta += f'- {item} | R$ {valor:.2f} | {categoria_item} | {metodo_pagamento} | {data}\n'

        resposta += f'\n💰 Total no período: R$ {total_gasto:.2f}'
        
        return resposta

    except Exception as e:
        return f"Erro interno ao consultar o Banco de Dados: {str(e)}"