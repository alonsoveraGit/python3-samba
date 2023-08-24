# Python3 - Samba

We carry out actions with samba through python (upload, download, list, delete).
Using action from .env we can select what we want to do, we have available: upload, download, list, delete

## Requirements
Use [git](https://git-scm.com/) to clone the repository.
We use [docker](https://www.docker.com/) to deploy the service.
It is also compatible with [docker-compose](https://docs.docker.com/compose/).



## 🚀 Getting Started

```bash
git clone https://github.com/alonsoveraGit/python3-samba.git 
cd python3-samba

cp env.example .env

docker-compose up


```
## ⚙️ Configuration
Copy or Rename env.example to .env and fill out the values:
```bash
# SMB connection settings (do not use "" or '' , just plain text)
server_name=NameServer
server_ip=IpServer
share_name=NameOfShareFolder
username=Username
password=SuperSecretPassword
domain_name= #if you do not have a domain leave blank

# upload / download / delete / list 
action=upload

# In case of downloads, upload and delete = file name. To list, directory (If it is root, leave blank)
remote_path=file.txt
local_path=file.txt
```
## 🐬 Docker Configuration
### Docker Run

```bash
docker run -d \
  --name python3-samba \
  --workdir /usr/src/myapp \
  -v ${PWD}/files:/usr/src/myapp/ \
  --env-file .env \
  alonsovera/python3-samba:v1 \
  python samba.py

```

### [Docker Compose](https://github.com/alonsoveraGit/python3-samba/blob/main/docker-compose.yml)

```bash
version: '3'
services:
  python3-samba:
    image: alonsovera/python3-samba:v1
    working_dir: /usr/src/myapp
    volumes:
      - "./files:/usr/src/myapp/"
      
    env_file:
      - .env
    command: python samba.py
    

```

