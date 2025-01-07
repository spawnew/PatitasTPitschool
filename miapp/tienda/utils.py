import requests

def get_random_dog():
    """
    Obtiene una imagen aleatoria de un perro.
    """
    url = "https://dog.ceo/api/breeds/image/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("message")  # Devuelve la URL de la imagen
    except requests.exceptions.RequestException as e:
        print(f"Error al consumir la API de perros: {e}")
        return None


