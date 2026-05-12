from typing import Optional
from banco_dados.conexao import engine
from sqlalchemy import text


def consultar(data_inicial: str, data_final: str, categoria: Optional[str] = None) -> str:
    """
    Consulta os gastos do usuário em um período específico, com filtro opcional de categoria.
    
    REGRA DE DATAS PARA O AGENTE:
    - O formato OBRIGATÓRIO é 'YYYY-MM-DD'.
    - Se o usuário pedir apenas um dia específico, passe a MESMA data.
    - Se o usuário pedir "este mês", calcule o primeiro e o último dia.
    """
    try:
        if categoria:
            query = text("SELECT * FROM financas WHERE data BETWEEN :data_inicial AND :data_final AND categoria = :categoria ORDER BY data DESC")
            parametros = {'data_inicial': data_inicial, 'data_final': data_final, 'categoria': categoria}
            
        else:
            query = text("SELECT * FROM financas WHERE data BETWEEN :data_inicial AND :data_final ORDER BY data DESC")
            parametros = {'data_inicial': data_inicial, 'data_final': data_final}
            
        # engine.connect() é o ideal para SELECTs. engine.begin() é mais usado para INSERT/UPDATE
        with engine.connect() as conexao:
            resultado = conexao.execute(query, parametros)
            # Extrai todas as linhas para uma lista do Python
            linhas_resultado = resultado.fetchall()
            
        if not linhas_resultado:
            if categoria:
                return f"Nenhum gasto encontrado na Categoria '{categoria}' entre {data_inicial} e {data_final}."
            return f"Nenhum gasto encontrado entre {data_inicial} e {data_final}."

        total_gasto = 0.0
        # Usamos uma lista para armazenar as strings (é mais eficiente que concatenar strings grandes com +)
        resposta = [f"💸 Relatório de Gastos ({len(linhas_resultado)} encontrados):\n"]
        
        for linha in linhas_resultado:
            linha_valor_numerico = float(linha.valor)
            total_gasto += linha_valor_numerico 
            
            resposta.append(f"- {linha.item} | R$ {linha_valor_numerico:.2f} | {linha.categoria} | {linha.metodo_pagamento} | {linha.data}")
            
        resposta.append(f"\n💰 Total no período: R$ {total_gasto:.2f}")
        
        return "\n".join(resposta)

    except Exception as e:
        return f"Erro interno ao consultar o Banco de Dados: {str(e)}"



if __name__ == "__main__":
    print(consultar('2026-04-14', '2026-04-14'))