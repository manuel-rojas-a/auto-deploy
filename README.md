# Auto-Deploy Manager

End-to-end infrastructure automation project featuring **Ansible** playbooks, **CI/CD** with GitHub Actions, and a full observability stack (**Prometheus + Grafana**) provisioned via **Vagrant**.

## 🚀 Architecture

This project deploys a complete 3-tier architecture with monitoring:

| Role | Services | IP |
|------|----------|----|
| **Web Server 1** | Nginx (80), Flask App (5000), Node Exporter | 192.168.122.10 |
| **Web Server 2** | Nginx (80), Flask App (5000), Node Exporter | 192.168.122.11 |
| **Database** | PostgreSQL (5432), Node Exporter | 192.168.122.20 |
| **Monitoring** | Prometheus, Grafana (3000) | 192.168.122.30 |

## 📋 Prerequisites

- **Vagrant** + **Libvirt** (KVM) or VirtualBox
- **Python 3.8+**
- **Ansible 2.9+**
- **Git**

## 🛠️ Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/manuel-rojas-a/auto-deploy.git
   cd auto-deploy
   ```

2. **Start Virtual Machines:**
   ```bash
   make vagrant-up
   ```

3. **Provision Infrastructure:**
   ```bash
   make vagrant-provision
   ```

4. **Access the Application:**
   - **Flask App**: http://192.168.122.10:5000
   - **Grafana Dashboard**: http://192.168.122.30:3000 (admin/admin)
   - **Prometheus Metrics**: http://192.168.122.30:9090

## 📚 Makefile Commands

| Command | Description |
|---------|-------------|
| `make help` | Show available commands |
| `make vagrant-up` | Start all VMs |
| `make vagrant-provision` | Provision all services via Ansible |
| `make deploy-stack` | Deploy Flask App + Monitoring Stack |
| `make test` | Run Python unit tests |
| `make lint` | Run Ruff linter |
| `make validate` | Validate Ansible playbooks syntax |
| `make ci` | Run full local CI pipeline |
| `make vagrant-destroy` | Destroy all VMs |

## 🧩 Project Structure

```
auto-deploy/
├── .github/workflows/    # CI/CD pipelines (Tests, Lint, Release)
├── inventory/            # Ansible inventory (generated)
├── playbooks/            # Ansible playbooks (Setup, Nginx, Flask, DB, Monitoring)
│   └── templates/        # Jinja2 templates
├── src/                  # Python scripts (Inventory generator, Flask App, Validator)
├── tests/                # Python unit tests
├── Vagrantfile           # VM definitions
└── Makefile              # Automation entry point
```

## ⚙️ Configuration

### 🔑 Database Password
For security reasons, the default database password in `playbooks/postgresql.yml` is a placeholder:
```yaml
db_password: "CHANGE_ME_USE_ANSIBLE_VAULT"
```
**To use your own password:**
1. Open `playbooks/postgresql.yml`.
2. Change the value of `db_password` to your desired secret.
3. Re-run provisioning.

## 🔒 Security

- **Passwords**: Database passwords are placeholders (`CHANGE_ME_USE_ANSIBLE_VAULT`).
- **Production**: For real environments, use **Ansible Vault** for secrets and manage keys securely.
- **Keys**: Vagrant uses default insecure keys for local dev only.

## 🤝 Contributing

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Commit changes: `git commit -m 'Add new feature'`
3. Push to branch: `git push origin feature/my-feature`
4. Open a Pull Request

## 📝 License

MIT License
