#!/usr/bin/env python3
"""Genera inventario dinamico para Ansible."""

import yaml
import os

# Configuración por defecto (Servidores remotos)
SERVERS = {
    "webservers": {
        "hosts": ["web1.example.com", "web2.example.com"],
        "vars": {
            "http_port": 80,
            "max_clients": 200,
        },
    },
    "dbservers": {
        "hosts": ["db1.example.com"],
        "vars": {
            "db_port": 5432,
            "db_name": "appdb",
        },
    },
}

# Configuración para Vagrant (Local)
VAGRANT_SERVERS = {
    "webservers": {
        "hosts": ["192.168.122.10", "192.168.122.11"],
        "vars": {
            "http_port": 80,
            "max_clients": 200,
            "ansible_user": "vagrant",
            "ansible_ssh_private_key_file": "~/.vagrant.d/insecure_private_key",
        },
    },
    "dbservers": {
        "hosts": ["192.168.122.20"],
        "vars": {
            "db_port": 5432,
            "db_name": "appdb",
            "ansible_user": "vagrant",
            "ansible_ssh_private_key_file": "~/.vagrant.d/insecure_private_key",
        },
    },
}


def generate_inventory(servers, output_path, use_vagrant=False):
    """Genera archivo YAML de inventario Ansible."""
    inventory = {}
    target_servers = VAGRANT_SERVERS if use_vagrant else servers

    for group, config in target_servers.items():
        inventory[group] = {
            "hosts": {host: config.get("vars", {}) for host in config["hosts"]}
        }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        yaml.dump(inventory, f, default_flow_style=False, sort_keys=False)

    print(f"Inventario generado en {output_path}")
    return output_path


if __name__ == "__main__":
    OUTPUT = "inventory/generated.yml"
    # Modo Vagrant si se pasa el argumento --vagrant
    use_vagrant = "--vagrant" in __import__("sys").argv
    generate_inventory(SERVERS, OUTPUT, use_vagrant=use_vagrant)
