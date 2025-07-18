# 🛣️ Roadmap

## 🔹 Fase 1: Núcleo funcional (MVP)

**Objetivo:** Herramienta CLI robusta para extraer contenido de archivos de texto recursivamente.

* [x] Leer archivos de texto recursivamente desde el directorio actual.
* [ ] Excluir archivos y carpetas por patrón (`.moleignore`).
* [x] Soporte para múltiples extensiones de texto (`.py`, `.ts`, `.md`, etc).
* [ ] Soporte para excluir carpetas ocultas.
* [ ] CLI con flags: `--output`, `--blacklist`, `--watch`.
* [ ] Modo `watch` para regenerar el output en cambios (Linux/macOS).
* [ ] Tests unitarios y de integración básicos.
* [ ] Versión en Bash y Python funcional.

## 🔹 Fase 2: CLI avanzada y modularidad

**Objetivo:** Facilitar su extensión y portabilidad.

* [ ] Modularización en comandos: `mole extract`, `mole watch`, `mole config`.
* [ ] Soporte multiplataforma completo (Windows incluido).
* [ ] CLI con `argparse` o `click`.
* [ ] Instalación como paquete (`pip install mole`).
* [ ] Documentación clara y concisa en `README.md`.

## 🔹 Fase 3: Integración IA local

**Objetivo:** Interacción con LLMs locales o remotos.

* [ ] Enviar contenido del output a una IA (por CLI).
* [ ] CLI: `mole analyze --provider openai/ollama/huggingface`.
* [ ] Prompt base configurable (`.moleconfig`).
* [ ] Módulos de análisis (e.g. `architecture`, `naming`, `doc coverage`).
* [ ] Soporte para OpenAI API con clave local.

## 🔹 Fase 4: Integraciones

**Objetivo:** Llevar Mole a más entornos y flujos de trabajo.

* [ ] Extensión para VSCode:

    * Botón “Run Mole”
    * Panel de análisis con recomendaciones
* [ ] GitHub Action:

    * Detecta cambios y ejecuta `mole extract && mole analyze`
    * Publica output y sugerencias en un PR
* [ ] Exporte en formatos alternativos (JSON, Markdown estructurado).

## 🔹 Fase 5: Plataforma y comunidad

**Objetivo:** Escalabilidad, feedback y contribuciones.

* [ ] Sitio web oficial con documentación y demos.
* [ ] Sistema de plugins para análisis personalizados.
* [ ] Comunidad en GitHub Discussions o Discord.
* [ ] Integración con repositorios públicos para análisis masivos.

