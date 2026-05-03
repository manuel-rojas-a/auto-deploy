#!/usr/bin/env python3
"""Tests para validator.py."""

import os
import tempfile
import unittest

from src.validator import validate_playbook


class TestValidatePlaybook(unittest.TestCase):
    """Tests del validador de playbooks."""

    def test_archivo_no_existe(self):
        errors = validate_playbook("no_existe.yml")
        self.assertEqual(len(errors), 1)
        self.assertIn("no encontrado", errors[0])

    def test_playbook_valido(self):
        valid = """
- name: Test play
  hosts: all
  tasks:
    - name: Test task
      ansible.builtin.debug:
        msg: "hello"
"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            f.write(valid)
            f.flush()
            errors = validate_playbook(f.name)
            self.assertEqual(errors, [])
            os.unlink(f.name)

    def test_falta_hosts(self):
        no_hosts = """
- name: Test play
  tasks:
    - name: Test task
      ansible.builtin.debug:
        msg: "hello"
"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            f.write(no_hosts)
            f.flush()
            errors = validate_playbook(f.name)
            self.assertTrue(any("hosts" in e for e in errors))
            os.unlink(f.name)

    def test_sin_tareas(self):
        no_tasks = """
- name: Test play
  hosts: all
"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            f.write(no_tasks)
            f.flush()
            errors = validate_playbook(f.name)
            self.assertTrue(any("tareas" in e for e in errors))
            os.unlink(f.name)

    def test_tarea_sin_nombre(self):
        no_name = """
- name: Test play
  hosts: all
  tasks:
    - ansible.builtin.debug:
        msg: "hello"
"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            f.write(no_name)
            f.flush()
            errors = validate_playbook(f.name)
            self.assertTrue(any("name" in e for e in errors))
            os.unlink(f.name)

    def test_yaml_invalido(self):
        invalid = "  - bad yaml: [\n\n"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            f.write(invalid)
            f.flush()
            errors = validate_playbook(f.name)
            self.assertTrue(any("sintaxis" in e for e in errors))
            os.unlink(f.name)


if __name__ == "__main__":
    unittest.main()
