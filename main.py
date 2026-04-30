from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import Response
import os


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


@app.post("/extract/text")
async def extract_text(file: UploadFile = File(...)):
    """
    Endpoint responsável por receber um ficheiro PDF ou DOCX
    e devolver um ficheiro TXT com o texto extraído.
    """

    # Verifica se foi enviado algum ficheiro
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Nenhum ficheiro foi enviado."
        )

    # Guarda o nome original do ficheiro
    nome_ficheiro = file.filename

    # Obtém a extensão do ficheiro
    extensao = os.path.splitext(nome_ficheiro)[1].lower()

    # Valida se o ficheiro é PDF ou DOCX
    if extensao not in [".pdf", ".docx"]:
        raise HTTPException(
            status_code=400,
            detail="Formato inválido. Apenas são permitidos ficheiros PDF ou DOCX."
        )

    # Lê o conteúdo do ficheiro enviado
    file_bytes = await file.read()

    # Verifica se o ficheiro está vazio
    if not file_bytes:
        raise HTTPException(
            status_code=400,
            detail="O ficheiro enviado está vazio."
        )

    # Texto temporário apenas para testar o endpoint
    texto = f"Ficheiro recebido com sucesso: {nome_ficheiro}\n"
    texto += f"Extensão detetada: {extensao}\n"
    texto += "A extração real do texto será implementada no próximo passo."

    # Cria o nome do ficheiro TXT de resposta
    nome_base = os.path.splitext(nome_ficheiro)[0]
    nome_txt = f"{nome_base}.txt"

    # Devolve um ficheiro TXT ao cliente
    return Response(
        content=texto,
        media_type="text/plain; charset=utf-8",
        headers={
            "Content-Disposition": f'attachment; filename="{nome_txt}"'
        }
    )