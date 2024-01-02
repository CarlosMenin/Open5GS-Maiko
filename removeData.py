import pymongo

# Conexão com o servidor do MongoDB. Alterar a porta específica do serviço do MongoDB
client = pymongo.MongoClient("mongodb://localhost:44857/")

# Acessa a base de dados e seleciona a coleção
db = client["open5gs"]
collection = db["subscribers"]

# Define uma lista de IMSIs a serem removidos
imsis_para_remover = [
    "999700000000003",
    "999700000000002",
    "999700000000001",
]

# Remove os documentos correspondentes aos IMSIs listados
for imsi in imsis_para_remover:
    collection.delete_one({"imsi": imsi})

