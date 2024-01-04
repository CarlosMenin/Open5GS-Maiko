import pymongo

# Conexão com o servidor do MongoDB. Alterar a porta específica do serviço do MongoDB
client = pymongo.MongoClient("mongodb://localhost:41087/")

# Acessa a base de dados e seleciona a coleção
db = client["open5gs"]
collection = db["subscribers"]

# Define o valor inicial para o imsi e a quantidade de UEs que foram cadastrados
valor_inicial = "999700000000000"
qtd_UE = 2

# Cria uma lista contendo os IMSIs dos documentos a serem removidos
imsis_para_remover = [str(int(valor_inicial) + num_UE) for num_UE in range(qtd_UE)]

# Cria um filtro para encontrar documentos com os IMSIs especificados
filtro = {"imsi": {"$in": imsis_para_remover}}

# Remove os documentos que correspondem ao filtro
resultado = collection.delete_many(filtro)

# Verifica quantos documentos foram removidos
print(f"Documentos removidos: {resultado.deleted_count}")
