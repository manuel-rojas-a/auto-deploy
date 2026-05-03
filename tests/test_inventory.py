#!/usr/bin/env python3
"""Tests para inventory.py."""

import os
import tempfile
import unittest
import yaml

from src.inventory import generate_inventory


class TestGenerateInventory(unittest.TestCase):
    """Tests de la funcion generate_inventory."""

    def setUp(self):
        self.test_servers = {
            "webservers": {
                "hosts": ["web1.example.com"],
                "vars": {"http_port": 80},
            }
        }
        self.temp_dir = tempfile.mkdtemp()
        self.output_path = os.path.join(self.temp_dir, "test_inventory.yml")

    def test_genera_archivo(self):
        """Verifica que el archivo se genera correctamente."""
        generate_inventory(self.test_servers, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_contenido_yaml(self):
        """Verifica que el contenido YAML es correcto."""
        generate_inventory(self.test_servers, self.output_path)
        with open(self.output_path) as f:
            data = yaml.safe_load(f)
        self.assertIn("webservers", data)
        self.assertIn("web1.example.com", data["webservers"]["hosts"])

    def test_vars_en_hosts(self):
        """Verifica que las variables se asignan a cada host."""
        generate_inventory(self.test_servers, self.output_path)
        with open(self.output_path) as f:
            data = yaml.safe_load(f)
        host_vars = data["webservers"]["hosts"]["web1.example.com"]
        self.assertEqual(host_vars["http_port"], 80)

    def test_creacion_directorio(self):
        """Verifica que crea el directorio si no existe."""
        new_path = os.path.join(self.temp_dir, "subdir", "inv.yml")
        generate_inventory(self.test_servers, new_path)
        self.assertTrue(os.path.exists(new_path))


if __name__ == "__main__":
    unittest.main()
