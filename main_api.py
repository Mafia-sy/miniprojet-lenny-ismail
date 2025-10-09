from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from aesgestion import AesGestion
from hashgestion import HashGestion
from rsagestion import RsaGestion
import uvicorn

app = FastAPI()

aes = AesGestion()
hash_gestion = HashGestion()
rsa = RsaGestion()

# ================= AES ====================

@app.post("/aes/generate_key")
def generate_aes_key():
    try:
        aes.generate_aes_key()
        return {"status": "AES key generated."}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/aes/save_key")
def save_key(filename: str = Form(...)):
    try:
        aes.save_aes_key_to_file(filename)
        return {"status": f"AES key saved to {filename}"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/aes/load_key")
def load_key(filename: str = Form(...)):
    try:
        aes.load_aes_key_from_file(filename)
        return {"status": f"AES key loaded from {filename}"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/aes/encrypt_string")
def encrypt_string(data: str = Form(...)):
    try:
        result = aes.encrypt_string_to_base64(data)
        return {"encrypted": result}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/aes/decrypt_string")
def decrypt_string(data: str = Form(...)):
    try:
        result = aes.decrypt_string_from_base64(data)
        return {"decrypted": result}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# ================= HASH ====================

@app.post("/hash/sha256")
def sha256_string(data: str = Form(...)):
    try:
        result = hash_gestion.calculate_sha256(data)
        return {"sha256": result}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# ================= RSA ====================

@app.post("/rsa/generate_keys")
def generate_rsa_keys(public_file: str = Form(...), private_file: str = Form(...), size: int = Form(...)):
    try:
        rsa.generation_clef(public_file, private_file, size)
        return {"status": "RSA keys generated."}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/rsa/load_keys")
def load_rsa_keys(pub_file: str = Form(...), priv_file: str = Form(...)):
    try:
        rsa.chargement_clefs(pub_file, priv_file)
        return {"status": "RSA keys loaded."}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/rsa/encrypt")
def rsa_encrypt(data: str = Form(...)):
    try:
        encrypted = rsa.chiffrement_rsa(data)
        return {"encrypted": encrypted}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/rsa/decrypt")
def rsa_decrypt(data: str = Form(...)):
    try:
        decrypted = rsa.dechiffrement_rsa(data)
        return {"decrypted": decrypted}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    uvicorn.run("main_api:app", host="0.0.0.0", port=8000, reload=True)
