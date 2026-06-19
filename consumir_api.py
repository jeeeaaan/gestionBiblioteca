import requests

BASE_URL = "http://127.0.0.1:8000/api-jean-v1"

# POST
nuevo_autor = {"nombre": "J. K. Rowling", "nacionalidad": "Británica"}

respuesta_post = requests.post(f"{BASE_URL}/Autor/", json=nuevo_autor)

print("\n=== POST AUTOR ===")
print("Código:", respuesta_post.status_code)
print("Respuesta:")
print(respuesta_post.json())

# GET
respuesta_get = requests.get(f"{BASE_URL}/Autor/")

print("=== GET AUTORES ===")
print("Código:", respuesta_get.status_code)
print("Respuesta:")
print(respuesta_get.json())
