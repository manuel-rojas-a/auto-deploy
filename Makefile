.PHONY: help inventory test deploy setup clean

help:
	@echo "Comandos disponibles:"
	@echo "  make inventory  - Generar inventario Ansible"
	@echo "  make test       - Ejecutar tests unitarios"
	@echo "  make deploy     - Ejecutar playbook de Nginx"
	@echo "  make setup      - Ejecutar setup inicial del servidor"
	@echo "  make clean      - Limpiar archivos generados"

inventory:
	python3 src/inventory.py

test:
	python3 -m unittest discover -s tests -v

deploy:
	ansible-playbook -i inventory/generated.yml playbooks/nginx.yml

setup:
	ansible-playbook -i inventory/generated.yml playbooks/setup.yml

clean:
	rm -f inventory/generated.yml
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
