from odf.opendocument import OpenDocumentText
from odf.text import P, H, Span
from odf.style import Style, TextProperties, ParagraphProperties
import sys

doc = OpenDocumentText()

# Helper to add paragraphs
def add_heading(doc, text, level=1):
    h = H(outlinelevel=level, text=text)
    doc.text.addElement(h)

def add_paragraph(doc, text, bold=False):
    p = P()
    if bold:
        span = Span(text=text, stylename=None) # Simplification, usually requires style definition
        # For simplicity in this script, just add text node
        p.addElement(text)
    else:
        p.addText(text)
    doc.text.addElement(p)

# Title
add_heading(doc, "Auto-Deploy Manager: Proyecto Completo", level=1)

# Introduction
add_paragraph(doc, "Este documento resume el desarrollo del proyecto 'Auto-Deploy Manager', una herramienta de automatización de infraestructura creada desde cero para aprender y aplicar prácticas modernas de DevOps.")

# Summary of phases
add_heading(doc, "Fases del Proyecto", level=2)

phases = [
    ("Fase 1: Inicio y Git", "Inicialización del repositorio, estructura de directorios (src, playbooks, inventory), configuración de .gitignore y README.md. Aprendizaje de commits, branches y tags."),
    ("Fase 2: Python y Ansible", "Creación de 'inventory.py' para generar inventarios dinámicos. Desarrollo de playbooks para instalar Nginx (Web), PostgreSQL (BD) y configurar servidores (Firewall, Timezone). Uso de templates Jinja2."),
    ("Fase 3: Testing y Calidad", "Implementación de pruebas unitarias con 'unittest' en Python para validar la generación de inventarios y la sintaxis de playbooks ('validator.py')."),
    ("Fase 4: CI/CD y GitHub Actions", "Configuración de pipelines automatizados que corren al hacer push. Includes jobs de testing, validación y linting (Ruff). Configuración de Release automático al crear tags."),
    ("Fase 5: Infraestructura Local (Vagrant)", "Integración con Vagrant y Libvirt para levantar 3 VMs (Ubuntu 22.04). Solución de problemas de redes, SSH keys y permisos. Provisionamiento exitoso de toda la infraestructura."),
    ("Fase 6: Observabilidad", "Despliegue de Node Exporter en todos los servidores. Creación de una 4ta VM para instalar Prometheus (recolección de métricas) y Grafana (visualización en Dashboards)."),
    ("Fase 7: Aplicación Real", "Despliegue de una aplicación Flask ('app.py') en los servidores web, exponiendo el puerto 5000. Integración de métricas de la app en Prometheus.")
]

for title, desc in phases:
    add_heading(doc, title, level=3)
    add_paragraph(doc, desc)

# Architecture
add_heading(doc, "Arquitectura Final", level=2)
arch_details = [
    "Web Servers (x2): Nginx (80), Flask App (5000), Node Exporter (9100).",
    "DB Server (x1): PostgreSQL (5432), Node Exporter (9100).",
    "Monitor Server (x1): Prometheus (9090), Grafana (3000).",
    "Network: Private subnet via Libvirt (192.168.122.x)."
]
for detail in arch_details:
    add_paragraph(doc, "• " + detail)

# Command Reference
add_heading(doc, "Comandos Principales (Makefile)", level=2)
commands = [
    "make vagrant-up       : Levantar VMs",
    "make vagrant-provision: Configurar todo desde cero",
    "make test             : Ejecutar tests",
    "make lint             : Revisar calidad de código",
    "make ci               : Pipeline local completo"
]
for cmd in commands:
    add_paragraph(doc, cmd)

# Save
doc.save("/home/redman/opencode/cursoopencode/auto-deploy/Resumen_Proyecto.odt")
print("ODT creado exitosamente.")
