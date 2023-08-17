from smb.SMBConnection import SMBConnection
import os

server_name = os.getenv('server_name')
server_ip = os.getenv('server_ip')
share_name = os.getenv('share_name')
username = os.getenv('username')
password = os.getenv('password')
domain_name = os.getenv('domain_name')

remote_path = os.getenv('remote_path')
local_path = os.getenv('local_path')

action = os.getenv('action')

# Función para conectar al servidor SMB
def connect_to_smb():
    conn = SMBConnection(username, password, "client", server_name, domain=domain_name, use_ntlm_v2=True)
    conn.connect(server_ip, 139)
    return conn

# Función para subir un archivo al servidor SMB
def upload_file(conn, local_path, remote_path):
    with open(local_path, 'rb') as local_file:
        conn.storeFile(share_name, remote_path, local_file)

# Función para descargar un archivo desde el servidor SMB
def download_file(conn, remote_path, local_path):
    with open(local_path, 'wb') as local_file:
        conn.retrieveFile(share_name, remote_path, local_file)

# Función para eliminar un archivo en el servidor SMB
def delete_file(conn, remote_path):
    try:
        conn.deleteFiles(share_name, remote_path)
        print("Archivo borrado")
    except Exception as e:
        print('Fallo al borrar el archivo')
        print(f"Ocurrió un error: {e}")

def list_file(conn, remote_path):
    file_list = conn.listPath(share_name, remote_path)

# Mostrar la lista de archivos
    for file_info in file_list:
        if file_info.isDirectory:
            print(f"Directorio: {file_info.filename}")
        else:
            print(f"Archivo: {file_info.filename}")


def perform_upload():
    print("Realizando la operación de subida (upload)...")
    # Agrega aquí las instrucciones para la operación de subida
    
    upload_file(smb_conn, local_path, remote_path)
    print("Archivo subido")


def perform_download():
    print("Realizando la operación de descarga (download)...")
    # Agrega aquí las instrucciones para la operación de descarga
    download_file(smb_conn, remote_path, "descarga_local.txt")
    print("Archivo descargado")

def perform_delete():
    print("Realizando la operación de eliminación (delete)...")
    # Agrega aquí las instrucciones para la operación de eliminación
    delete_file(smb_conn, remote_path)
    

def perform_list():
    print("Realizando la operación de eliminación (list)...")
    # Agrega aquí las instrucciones para la operación de eliminación
    list_file(smb_conn, remote_path)
    print("Archivo listado")

def default_action():
    print("La acción no coincide con ninguna operación conocida...")

#action = "upload"  # Cambia esto según la acción que desees realizar (DEFINIDO en .env)

actions = {
    "upload": perform_upload,
    "download": perform_download,
    "delete": perform_delete,
    "list": perform_list
}


# Obtén la función asociada con la acción o la función default_action si no coincide
selected_action = actions.get(action, default_action)


# Conexión al servidor SMB
smb_conn = connect_to_smb()



# Ejecutamos acción
selected_action()


# Desconexión del servidor SMB
smb_conn.close()