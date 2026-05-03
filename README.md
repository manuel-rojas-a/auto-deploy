# Auto-Deploy Manager

Herramienta para automatizar el despliegue de aplicaciones en servidores usando Python y Ansible.

## Requisitos

- Python 3.8+
- Ansible 2.9+
- Git

## Uso

```bash
pip install -r requirements.txt
python src/deploy.py
```

## Playbooks

- `playbooks/setup.yml` - Configuracion inicial del servidor
- `playbooks/nginx.yml` - Instalacion y configuracion de Nginx
