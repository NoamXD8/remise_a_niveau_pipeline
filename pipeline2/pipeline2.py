import json
from datetime import datetime, date
import shutil
import os

def load_sample(path) -> list[str]:
    with open(path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

def generate_json(lignes: list[str]) -> list[dict]:
    donnees = {}
    for ligne in lignes:
        nom_emetteur, date, montant = ligne.split()
        montant = float(montant.replace('€', ''))
        if nom_emetteur in donnees:
            donnees[nom_emetteur] += montant
        else:
            donnees[nom_emetteur] = montant
    resultat = [{"name": nom_emetteur, "total_sent": total_envoye} for nom_emetteur, total_envoye in donnees.items()]

    return resultat

def save_result(path, result):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as json_file:
        json.dump(result, json_file, indent=4)
    print(f"Résultat sauvegardé dans {path}")


def archive_file(path: str, archive_dir: str):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    shutil.move(path, os.path.join(archive_dir, os.path.basename(path)))
    print(f"Fichier {path} archivé dans {archive_dir}")

def process_files(directory_source, directory_target):
    archive_dir = 'archived'
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    if not os.path.exists(directory_target):
        os.makedirs(directory_target)

    for file in os.listdir(directory_source):
        if file.endswith('.txt'):
            file_path = os.path.join(directory_source, file)
            print(f"Traitement du fichier : {file_path}")

            result_filename = f"result_{file[:-4]}_{date.today().strftime('%Y%m%d')}.json"
            result_path = os.path.join(directory_target, result_filename)

            lines = load_sample(file_path)
            result = generate_json(lines)

            save_result(result_path, result)
            archive_file(file_path, archive_dir)

if __name__ == '__main__':
    process_files('source', 'result')


