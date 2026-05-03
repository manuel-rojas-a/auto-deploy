#!/usr/bin/env python3
"""Genera inventario dinamico para Ansible."""

import yaml
import os

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


def generate_inventory(servers, output_path):
    """Genera archivo YAML de inventario Ansible."""
    inventory = {}

    for group, config in servers.items():
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
    generate_inventory(SERVERS, OUTPUT)
