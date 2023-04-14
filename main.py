import os
import time
import clipboard
from notion_client import Client

# Initialisez le client Notion avec votre clé API
notion = Client(auth="secret_lFOmk2DQGCKf8jB2ZIX83PpWTIvnVVlItkKBDg1VB4O")

# Remplacez ceci par l'ID de la base de données que vous avez obtenu précédemment
database_id = "a02dae719f754df28d882f2088f8f3b5"

def add_to_notion(title, content):
    current_time = time.ctime()
    new_page = {
        "Titre": {"title": [{"text": {"content": f"{title} - {current_time}"}}]},
        "Contenu": {"rich_text": [{"text": {"content": content}}]},
    }
    notion.pages.create(parent={"database_id": database_id}, properties=new_page)



def save_clipboard_to_file(history_path=os.path.join(os.path.expanduser("~"), 'clipboard_history.txt')):
    last_clipboard_content = ""
    
    while True:
        current_clipboard_content = clipboard.paste()
        if current_clipboard_content != last_clipboard_content:
            last_clipboard_content = current_clipboard_content
            with open(history_path, 'a') as history_file:
                history_file.write(f"{time.ctime()}: {current_clipboard_content}\n")
            
            # Sauvegardez le contenu du presse-papiers sur Notion
            add_to_notion("Clipboard entry", current_clipboard_content)

            # Afficher le contenu mis à jour du fichier dans le terminal
            print("Clipboard history updated:")
            with open(history_path, 'r') as history_file:
                print(history_file.read())
        time.sleep(1)

if __name__ == "__main__":
    save_clipboard_to_file()
