from fastapi import FastAPI

app = FastAPI(
    title="Web Service de Extração de Texto",
    description="Serviço REST para extração de texto de documentos PDF e DOCX.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Web Service de Extração de Texto ativo."
    }