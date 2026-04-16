from fastapi import FastAPI

app = FastAPI()

# Rota principal (GET)
@app.get("/saudar/{nome}")
def ler_nome(nome: str):
    return {"mensagem": f"Olá, {nome}! Bem-vindo ao mundo onde tudo acontece."}