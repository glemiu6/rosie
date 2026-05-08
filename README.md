# rosie 🤖

> A ROS2-native AI diagnostic tool powered by a local LLM. Pipe your errors in, get answers out.

```bash
ros2 launch my_robot bringup.launch.py 2>&1 | rosie solve
```

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ROS2](https://img.shields.io/badge/ROS2-Humble%20%7C%20Iron%20%7C%20Jazzy-blue)](https://docs.ros.org)
[![Platform](https://img.shields.io/badge/platform-Linux-lightgrey)](https://www.linux.org)

---

## What is rosie?

Debugging ROS2 is painful. Cryptic error messages, TF tree issues, QoS mismatches, `colcon` build failures that mean three different things depending on your distro. You end up context-switching between your terminal, GitHub issues, and ROS Answers — breaking your flow every time something goes wrong.

rosie keeps you in the terminal. It collects your ROS2 environment, reads your error, and gives you a diagnosis that's aware of your distro, your active nodes, and your workspace — not a generic answer scraped from the internet.

It runs entirely on your machine. No cloud, no API keys required, no sending your robot's internals anywhere.

---

## Features

- **Pipe any error directly into rosie** — works with any ROS2 command output
- **Distro-aware** — knows the differences between Humble, Iron, and Jazzy
- **Local LLM first** — runs on Ollama or llama.cpp, no internet required
- **Modular backends** — swap to Claude or OpenAI when you need more power
- **Context-aware** — collects your active nodes, topics, workspace, and environment before answering
- **Single curl install** — no manual setup

---

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/glemiu6/rosie/master/install.sh | bash
```

Then configure:

```bash
rosie init
```

---

## Requirements

- Linux only (ROS2 requirement)
- ROS2 Humble, Iron, or Jazzy sourced in your shell
- Python 3.10+
- [Ollama](https://ollama.com) running locally (default backend)

---

## Usage

**Solve an error:**
```bash
ros2 launch my_robot bringup.launch.py 2>&1 | rosie solve
```

**Explain a ROS2 concept:**
```bash
rosie explain "QoS reliability policies"
```

**Interactive debug session:**
```bash
rosie debug
```

---

## Configuration

rosie is configured interactively via:

```bash
rosie init
```

This creates `~/.rosie/config.toml`. You can also edit it directly:

```toml
[core]
backend = "ollama"          # ollama | llamacpp | claude | openai

[ollama]
model = "llama3.2"
url = "http://localhost:11434"

[llamacpp]
model = "mistral"
url = "http://localhost:8080"

[claude]
model = "claude-sonnet-4-20250514"
api_key = ""                # or set ROSIE_CLAUDE_API_KEY env var

[openai]
model = "gpt-4o"
api_key = ""                # or set ROSIE_OPENAI_API_KEY env var
```

API keys can be set via environment variables instead of the config file:

```bash
export ROSIE_CLAUDE_API_KEY=sk-ant-...
export ROSIE_OPENAI_API_KEY=sk-...
```

---

## Supported Distros

| Distro | Status | EOL |
|--------|--------|-----|
| Humble Hawksbill | ✅ Full support | May 2027 |
| Iron Irwini | ⚠️ Maintenance only | November 2024 |
| Jazzy Jalisco | ✅ Full support | May 2029 |

---

## Supported Backends

| Backend | Type | Requires |
|---------|------|----------|
| Ollama | Local | Ollama running locally |
| llama.cpp | Local | llama.cpp server running |
| Claude | Cloud | Anthropic API key |
| OpenAI | Cloud | OpenAI API key |

---

## What rosie collects

Before every query rosie gathers:

- `$ROS_DISTRO` and ROS2 environment variables
- Active nodes (`ros2 node list`)
- Active topics (`ros2 topic list`)
- Workspace info (`COLCON_PREFIX_PATH`)
- Installed packages (`colcon list`)

Nothing is sent anywhere except your chosen LLM backend. If you use a local backend, nothing leaves your machine.

---

## Roadmap

rosie is being built in phases — from a focused diagnostic tool to a full ROS2 AI assistant.

Current phase: **Phase 1 — Foundation**

See the full roadmap in [ROADMAP](ROADMAP.md).

---

## Changelog

See [CHANGELOG](CHANGELOG.md) for a full history of releases and changes.

---

## Contributing

rosie is early stage and community knowledge is what makes it better. Distro quirks, new commands, backend improvements — all contributions are welcome.

See [CONTRIBUTING](CONTRIBUTING.md) for how to get started.

---

## License

[Apache License 2.0](https://github.com/glemiu6/komit/blob/master/LICENSE)

---

## Why "rosie"?

ROS2 + AI = rosie. Also, every robot deserves a good assistant.