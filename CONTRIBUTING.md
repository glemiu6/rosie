# Contributing to rosie

Thanks for wanting to help. rosie is early stage and there is a lot of ground to cover — especially around distro-specific knowledge that only comes from real ROS2 experience in the field.

---

## Where help is most needed right now

- **Distro quirks** — known bugs, edge cases, and gotchas for Humble, Iron, and Jazzy that should be injected into prompts
- **Supported commands** — validating which `ros2` and `colcon` commands work reliably across distros
- **Prompt quality** — if rosie gives you a bad diagnosis, open an issue with the error and what the correct answer should have been
- **Backend testing** — testing the Ollama backend with different models and reporting which ones work well for ROS2 diagnostics

---

## Getting started

**1. Fork and clone the repo**

```bash
git clone https://github.com/yourusername/rosie.git
cd rosie
```

**2. Set up the development environment**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

**3. Make sure your ROS2 environment is sourced**

```bash
source /opt/ros/humble/setup.bash
```

**4. Run the tests**

```bash
pytest tests/
```

---

## How to contribute

### Reporting a bug

Open an issue and include:

- Your ROS2 distro (`echo $ROS_DISTRO`)
- The exact command you ran
- The error rosie gave you
- What the correct answer should have been
- Your backend and model (`cat ~/.rosie/config.toml`)

### Adding a distro quirk

Distro quirks live in `rosie/distro.py` inside the profile for each distro. A quirk is a plain English sentence describing a known bug or gotcha that gets injected into the LLM prompt.

Good quirk examples:
- `"TF2 buffer lookup can fail silently when the clock source is misconfigured in Humble"`
- `"colcon build --symlink-install may cause issues with Python packages in workspaces with mixed distro dependencies"`

Bad quirk examples:
- `"TF bug"` — too vague, the LLM can't use this
- `"See issue #1234"` — links don't work in prompts

### Adding a new command to a distro profile

Commands live in `rosie/distro.py` in the `supported_commands` dict. Before adding a command, verify it works on that distro by testing it yourself. If you are unsure, note it in your PR.

### Adding a new backend

1. Create `rosie/backends/yourbackend.py`
2. Implement the `BaseBackend` abstract class from `rosie/backends/base.py`
3. Add it to the backend selection in `rosie/config.py` and `rosie/main.py`
4. Add it to the supported backends table in `README.md`
5. Add tests in `tests/backends/`

---

## Branch naming

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `feat/description` | `feat/llamacpp-backend` |
| Bug fix | `fix/description` | `fix/humble-node-list-parsing` |
| Distro quirk | `quirk/distro-description` | `quirk/jazzy-tf2-clock` |
| Docs | `docs/description` | `docs/update-contributing` |

---

## Commit style

Keep commits small and focused. Use plain English:

```
add llama.cpp backend skeleton
fix ollama backend timeout handling
add jazzy quirk for TF2 buffer issue
update humble supported commands list
```

No need for conventional commits or emoji prefixes — just be clear about what changed.

---

## Pull request checklist

- [ ] Tests pass (`pytest tests/`)
- [ ] New code has tests where appropriate
- [ ] `CHANGELOG.md` updated under `[Unreleased]`
- [ ] If adding a distro quirk, you have personally verified it on that distro

---

## Code style

- Python 3.10+
- `black` for formatting
- `ruff` for linting
- Type hints on all public functions
- Docstrings on all public functions and classes

Run before committing:

```bash
black rosie/
ruff check rosie/
```

---

## Questions

Open an issue with the label `question`. No question is too basic — ROS2 is complicated and so is building tools for it.