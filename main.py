import os
import time
import clipboard

def save_clipboard_to_file(history_path=os.path.join(os.path.expanduser("~"), 'clipboard_history.txt')):
    last_clipboard_content = ""
    
    while True:
        current_clipboard_content = clipboard.paste()
        if current_clipboard_content != last_clipboard_content:
            last_clipboard_content = current_clipboard_content
            with open(history_path, 'a') as history_file:
                history_file.write(f"{time.ctime()}: {current_clipboard_content}\n")
            
            # Afficher le contenu mis à jour du fichier dans le terminal
            print("Clipboard history updated:")
            with open(history_path, 'r') as history_file:
                print(history_file.read())
        time.sleep(1)

if __name__ == "__main__":
    save_clipboard_to_file()

