import os
import datetime
import glob

def backup_database(host, user, password, database, backup_dir, port, max_backups=5):
    # Assicurati che la cartella di backup esista
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Definisci il nome del file di backup
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"{database}_backup_{current_time}.sql"
    backup_filepath = os.path.join(backup_dir, backup_filename)

    # Crea il comando mysqldump con la porta inclusa
    command = f"mysqldump -h {host} -P {port} -u {user} -p{password} {database} > {backup_filepath}"

    # Esegui il comando
    os.system(command)
    print(f"Backup completato: {backup_filepath}")

    # Gestisci i vecchi file di backup
    manage_old_backups(backup_dir, max_backups)

def manage_old_backups(backup_dir, max_backups):
    # Trova tutti i file di backup nella cartella di backup
    backup_files = sorted(glob.glob(os.path.join(backup_dir, "*.sql")))

    # Se ci sono più file di backup rispetto a max_backups, elimina i più vecchi
    while len(backup_files) > max_backups:
        oldest_file = backup_files.pop(0)
        os.remove(oldest_file)
        print(f"File eliminato: {oldest_file}")

# Parametri di connessione e configurazione
host = "localhost"
user = "root"
password = "password"
database = "mydbristorante"
backup_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "BackupSql")
port = 3360

# Esegui il backup
backup_database(host, user, password, database, backup_dir, port)