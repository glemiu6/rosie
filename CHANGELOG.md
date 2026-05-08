# Changelog

All notable changes to rosie will be documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/). rosie uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### In progress
- `rosie init` — interactive setup wizard
- `config.py` — load and validate `~/.rosie/config.toml`
- `distro.py` — Humble, Iron, Jazzy distro profiles
- `context.py` — ROS2 environment collection
- `backends/ollama.py` — Ollama local LLM backend
- `commands/solve.py` — pipe errors into rosie
- `install.sh` — curl install for Linux

---

## [0.1.0] — TBD

### Added
- Initial release
- `rosie solve` — pipe ROS2 errors for diagnosis
- `rosie init` — interactive configuration wizard
- Ollama backend support
- Distro-aware prompts for Humble, Iron, and Jazzy
- ROS2 environment context collection
- curl install via `install.sh`
- bash/zsh shell integration

---

*Older releases will be listed here as the project grows.*