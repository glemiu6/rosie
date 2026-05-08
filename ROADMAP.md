# rosie — Roadmap

This document outlines the development plan for rosie. It is organized into phases, each building on the previous one. The goal is to start focused and expand based on community feedback.

---

## Phase 1 — Foundation
*The core diagnostic tool. Pipe errors in, get answers out.*

- [ ] `rosie init` — interactive setup wizard
- [x] `config.py` — load and validate `~/.rosie/config.toml`
- [ ] `distro.py` — Humble, Iron, Jazzy profiles
- [ ] `context.py` — collect ROS2 environment, nodes, topics, workspace
- [ ] `backends/base.py` — abstract backend interface
- [ ] `backends/ollama.py` — Ollama local LLM backend
- [ ] `prompt_builder.py` — distro-aware prompt assembly
- [ ] `commands/solve.py` — pipe errors into rosie
- [ ] `main.py` — CLI entry point, wire everything together
- [ ] `install.sh` — curl install for Linux
- [ ] `scripts/shell_integration.sh` — PATH setup, bash/zsh completion

---

## Phase 2 — Backend Expansion
*Let the user choose their LLM.*

- [ ] `backends/llamacpp.py` — llama.cpp local backend
- [ ] `backends/claude.py` — Anthropic Claude backend
- [ ] `backends/openai.py` — OpenAI backend
- [ ] Environment variable support for API keys (`ROSIE_CLAUDE_API_KEY`, `ROSIE_OPENAI_API_KEY`)
- [ ] `rosie init` backend switching — re-run init to change backend without losing config
- [ ] Backend availability check at startup — warn if Ollama is not running

---

## Phase 3 — Richer Commands
*More ways to interact with rosie beyond error solving.*

- [ ] `commands/explain.py` — `rosie explain <concept>` for ROS2 concepts
- [ ] `commands/debug.py` — interactive debug session
- [ ] Streaming responses — print LLM output token by token instead of waiting
- [ ] `--verbose` flag — show what context was collected before the answer
- [ ] `--no-context` flag — skip environment collection, just send the error
- [ ] `--distro` flag — manually override distro detection

---

## Phase 4 — Live Graph Introspection
*rosie understands your running system, not just your error text.*

- [ ] `ros2 node info` per active node — collect publisher/subscriber details
- [ ] TF tree snapshot — `ros2 run tf2_tools view_frames`
- [ ] QoS mismatch detection — compare publisher and subscriber QoS policies
- [ ] `ros2 doctor` output parsing — structured diagnosis from built-in ROS2 tool
- [ ] `ros2 wtf` support — Jazzy and later distros
- [ ] Active parameter collection — `ros2 param list` per node

---

## Phase 5 — Colcon & Build Diagnostics
*Diagnose workspace and build failures, not just runtime errors.*

- [ ] `colcon list` — workspace package inventory
- [ ] `colcon graph` — dependency graph analysis
- [ ] `colcon info` — per-package dependency details
- [ ] Build log parsing — structured colcon build failure analysis
- [ ] Missing dependency detection — suggest `apt install` or `pip install` fixes
- [ ] Workspace sanity check — detect common workspace setup mistakes

---

## Phase 6 — Bag File Analysis
*Analyze recorded ROS2 data without replaying it.*

- [ ] `ros2 bag info` parsing — extract topic list, message counts, duration
- [ ] Topic frequency analysis — detect dropped messages or unexpected rates
- [ ] Basic message inspection — summarize message contents for a given topic
- [ ] Anomaly detection — flag unusual gaps or spikes in recorded data

---

## Phase 7 — Distribution
*Make rosie easy to install everywhere.*

- [ ] `pip` package — `pip install rosie-ros2`
- [ ] `apt` package — `apt install rosie` for Ubuntu/Debian
- [ ] GitHub Releases — versioned binary releases via Rust rewrite of core
- [ ] Rust rewrite — single distributable binary, no Python runtime dependency
- [ ] Docker image — for air-gapped or containerized robot systems
- [ ] Automatic update check — notify user when a new version is available

---

## Phase 8 — Community & Ecosystem
*Grow beyond a single tool.*

- [ ] Distro profile contributions — community-maintained quirks and command lists
- [ ] Plugin system — let users add custom commands and context collectors
- [ ] ROS2 package-specific knowledge — known issues per popular package (Nav2, MoveIt2, micro-ROS)
- [ ] `rosie feedback` — send anonymized diagnostic sessions to improve prompts (opt-in)
- [ ] Web dashboard — optional local web UI for non-terminal users

---

## Known Limitations

- Linux only — ROS2 on Windows and macOS is not supported
- Requires ROS2 to be sourced in the shell before running
- LLM quality depends on the model chosen — local models may miss niche ROS2 issues
- Iron is EOL as of November 2024 — support will not be expanded for this distro

---

## Contributing to the Roadmap

If you want to propose a feature or change the priority of an item, open an issue on GitHub with the label `roadmap`. Community feedback directly shapes what gets built next.