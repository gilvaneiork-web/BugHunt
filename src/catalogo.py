SERVICOS = [
    {"id": 1, "nome": "Licenciamento", "categoria": "Ambiental", "ativo": True},
    {"id": 2, "nome": "Fiscalização", "categoria": "Ambiental", "ativo": True},
    {"id": 3, "nome": "Protocolo Antigo", "categoria": "Ambiental", "ativo": False},
    {"id": 4, "nome": "Atendimento", "categoria": "Administrativo", "ativo": True},
]

def listar_ativos():
    return [servico for servico in SERVICOS if servico["ativo"]]

def buscar_por_categoria(categoria):
    return [
        servico
        for servico in SERVICOS
        if servico["categoria"] == categoria
    ]
