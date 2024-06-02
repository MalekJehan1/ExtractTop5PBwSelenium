import requests
import json

link = "https://discord.com/api/v10/webhooks/1236210120816463945/iBOcwTljq_907JxRrLydpE4EojHjsDd6FjMq0n0wYpbBfT8DuH7fd9vG9-gjfEnfBYml?wait=true"

data = {
    "username": "Teste",
    "content": "Teste xis",
    "embeds": [{
        "title": "TESTE",
        "description": "Testando 123" 
    }]
}

#dicionario_ajus = json.dumps(dicionario)

requests.post(link, json=data)