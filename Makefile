.PHONY: help inventory test validate deploy setup ci clean lint \
        vagrant-up vagrant-destroy vagrant-provision vagrant-ssh

help:
	@echo "Comandos disponibles:"
	@echo "  make inventory        - Generar inventario Ansible"
	@echo "  make test             - Ejecutar tests unitarios"
	@echo "  make validate         - Validar playbooks Ansible"
	@echo "  make lint             - Ejecutar linter Ruff"
	@echo "  make deploy           - Ejecutar playbook de Nginx"
	@echo "  make setup            - Ejecutar setup inicial del servidor"
	@echo "  make monitoring       - Instalar monitoreo Node Exporter"
	@echo "  make ci               - Ejecutar pipeline CI completo"
	@echo "  make vagrant-up       - Levantar máquinas virtuales (Vagrant)"
	@echo "  make vagrant-destroy  - Destruir máquinas virtuales"
	@echo "  make vagrant-provision- Provisionar VMs con Ansible"
	@echo "  make clean            - Limpiar archivos generados"

inventory:
	python3 src/inventory.py

test:
	python3 -m unittest discover -s tests -v

validate:
	python3 src/validator.py playbooks

deploy:
	ansible-playbook -i inventory/generated.yml playbooks/nginx.yml

setup:
	ansible-playbook -i inventory/generated.yml playbooks/setup.yml

monitoring:
	ansible-playbook -i inventory/generated.yml playbooks/monitoring.yml

ci: test validate lint

lint:
	ruff check src/ tests/

vagrant-up:
	vagrant up

vagrant-destroy:
	vagrant destroy -f

vagrant-provision:
	python3 src/inventory.py --vagrant
	ansible-playbook -i inventory/generated.yml playbooks/setup.yml
	ansible-playbook -i inventory/generated.yml playbooks/nginx.yml
	ansible-playbook -i inventory/generated.yml playbooks/postgresql.yml
	ansible-playbook -i inventory/generated.yml playbooks/monitoring.yml

vagrant-ssh:
	ssh -i ~/.vagrant.d/insecure_private_key vagrant@192.168.122.10

clean:
	rm -f inventory/generated.yml
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
