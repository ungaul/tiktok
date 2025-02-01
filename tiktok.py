import requests
import schedule
import time
import os

# Configuration
CLIENT_KEY = "1488awz0gbd2c4krpzv3"
CLIENT_SECRET = "1488mDTuSzBWzSXPpBquW8nNl7vQl99OAtdA"
VIDEO_FILENAME = "Weewee Cat.mp4"

# Remplace cette URL par celle fournie par TikTok si nécessaire.
API_ENDPOINT = "https://open-api.tiktok.com/video/upload/"

def post_video_to_tiktok():
    # Vérifier si le fichier vidéo existe
    if not os.path.isfile(VIDEO_FILENAME):
        print(f"Le fichier {VIDEO_FILENAME} n'existe pas.")
        return

    try:
        with open(VIDEO_FILENAME, "rb") as video_file:
            files = {
                "video": video_file
            }
            # Selon la documentation de l'API, d'autres paramètres peuvent être requis
            data = {
                "client_key": CLIENT_KEY,
                "client_secret": CLIENT_SECRET,
                # Ajoute ici d'autres paramètres requis par l'API, par exemple le titre, la description, etc.
            }

            print("Tentative d'envoi de la vidéo sur TikTok...")
            response = requests.post(API_ENDPOINT, files=files, data=data)

            if response.status_code == 200:
                print("Vidéo envoyée avec succès !")
            else:
                print(f"Erreur lors de l'envoi de la vidéo (code {response.status_code}) : {response.text}")

    except Exception as e:
        print("Une exception est survenue lors de l'envoi de la vidéo :", e)

# Planifier l'exécution de la fonction à 17h chaque jour
schedule.every().day.at("17:00").do(post_video_to_tiktok)

print("Le script est lancé. En attente de l'exécution programmée...")

while True:
    schedule.run_pending()
    # Pause de 60 secondes entre chaque vérification
    time.sleep(60)
