# Collection of git hooks for Yamale to be used with [pre-commit framework](http://pre-commit.com/)

[![Github tag](https://img.shields.io/github/tag/k-ogawa-1988/pre-commit-yamale.svg)](https://github.com/k-ogawa-1988/pre-commit-yamale/releases)

## How to install

### 1. Install dependencies

* [`pre-commit`](https://pre-commit.com/#install)
* [`yamale`](https://github.com/23andMe/Yamale)
* [`pyyaml`](https://github.com/yaml/pyyaml) or [`ruamel`](https://yaml.readthedocs.io/en/latest/)

### 2. Add configs and hooks
Step into the repository you want to have the pre-commit hooks installed and edit `.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/k-ogawa-1988/pre-commit-yamale
  rev: <VERSION> # Get the latest from: https://github.com/k-ogawa-1988/pre-commit-yamale/releases
  hooks:
    - id: yamale-validate
```

with options:

```yaml
repos:
- repo: https://github.com/k-ogawa-1988/pre-commit-yamale
  rev: <VERSION> # Get the latest from: https://github.com/k-ogawa-1988/pre-commit-yamale/releases
  hooks:
    - id: yamale-validate
      args:  # Describe below
        - '--exclude=venv'
        - '--exclude=node_modules'
```

### 3. Run

After pre-commit hook has been installed you can run it manually on all files in the repository

```bash
pre-commit run -a
```

## Arguments

### Arguments from Yamale

* `--schema=SCHEMA` `-s=SCHEMA`  
  File path of schema. Both absolute path and relative path can be accepted.
* `--parser={pyyaml,ruamel}` `-p={pyyaml,ruamel}`  
  YAML library to load files. Choices are "ruamel" or "pyyaml" (default).
* `--no-strict`  
  Disable strict mode, unexpected elements in the data will be accepted.

### Arguments from pre-commit-yamale

* `PATH`  (required)  
  Files to validate.
* `--no-recursive`  
  Disable recursive scan under specified path.
* `--exclude=EXCLUDE`  
  Folder to exclude from validation. Multiple options can be accepted.
* `--debug`  
  Output debug logs.

## Authors

This repository is managed by [Ken'ichi Ogawa](https://github.com/k-ogawa-1988).  
Any forks or pull requests are welcome!

## License

MIT licensed. See LICENSE for full details.
