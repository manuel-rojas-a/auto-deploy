#!/usr/bin/env python3
"""Validador de playbooks Ansible."""

import os
import sys
import yaml


def validate_playbook(filepath):
    """Valida un playbook Ansible y retorna lista de errores."""
    errors = []

    if not os.path.exists(filepath):
        return [f"Archivo no encontrado: {filepath}"]

    try:
        with open(filepath) as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [f"Error de sintaxis YAML: {e}"]

    if data is None:
        return ["El playbook esta vacio"]

    if not isinstance(data, list):
        return ["El playbook debe ser una lista de plays"]

    for i, play in enumerate(data):
        if play is None:
            errors.append(f"Play {i}: bloque vacio")
            continue

        if "hosts" not in play:
            errors.append(f"Play {i}: falta el campo 'hosts'")

        if "tasks" not in play:
            errors.append(f"Play {i}: no tiene tareas")

        if "tasks" in play:
            for j, task in enumerate(play["tasks"]):
                if not task:
                    errors.append(f"Play {i}, Task {j}: tarea vacia")
                elif "name" not in task and "ansible.builtin.command" not in task:
                    errors.append(f"Play {i}, Task {j}: falta 'name'")

    return errors


def validate_all_playbooks(directory="playbooks"):
    """Valida todos los playbooks en un directorio."""
    results = {}

    if not os.path.exists(directory):
        print(f"Directorio '{directory}' no encontrado")
        sys.exit(1)

    for filename in sorted(os.listdir(directory)):
        if filename.endswith((".yml", ".yaml")):
            filepath = os.path.join(directory, filename)
            errors = validate_playbook(filepath)
            results[filepath] = errors

    return results


def main():
    """Ejecuta la validacion."""
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isdir(target):
            results = validate_all_playbooks(target)
        else:
            results = {target: validate_playbook(target)}
    else:
        results = validate_all_playbooks()

    has_errors = False
    for filepath, errors in results.items():
        if errors:
            has_errors = True
            print(f"❌ {filepath}")
            for error in errors:
                print(f"   - {error}")
        else:
            print(f"✅ {filepath}")

    if has_errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
