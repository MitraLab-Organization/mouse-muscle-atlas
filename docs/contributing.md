# Contributing to MMA

Thank you for your interest in contributing to the Mouse Muscle Atlas!

## How to Contribute

### Reporting Issues

1. Check if the issue already exists
2. Create a new issue with a clear description
3. Use appropriate labels

### Requesting New Terms

To request a new anatomical term:

1. Open a [New Term Request](https://github.com/MitraLab-Organization/mouse-muscle-atlas/issues/new)
2. Provide:
   - Preferred term label
   - Definition with citation
   - Parent class suggestion
   - Any relevant synonyms

### Making Changes

1. Fork the repository
2. Create a feature branch
3. Make your changes to `src/ontology/mma-edit.owl`
4. Submit a pull request

## Development Setup

### Prerequisites

- Docker
- Git

### Running ODK Commands

```bash
cd src/ontology
sh run.sh make <target>
```

### Common Targets

| Command | Description |
|---------|-------------|
| `make test` | Run tests |
| `make prepare_release` | Prepare a release |
| `make refresh-imports` | Refresh all imports |

