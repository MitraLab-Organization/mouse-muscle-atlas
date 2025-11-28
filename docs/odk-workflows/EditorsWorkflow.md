# Editors Workflow

This guide describes the standard workflow for editing the Mouse Muscle Atlas ontology.

## Prerequisites

- [Protégé](https://protege.stanford.edu/) installed
- Git configured
- Docker installed (for ODK commands)

## Editing Workflow

### 1. Get the Latest Version

```bash
git pull origin main
```

### 2. Create a Branch

```bash
git checkout -b your-feature-branch
```

### 3. Edit in Protégé

1. Open `src/ontology/mma-edit.owl` in Protégé
2. Make your changes
3. Save the file

### 4. Run Quality Checks

```bash
cd src/ontology
sh run.sh make test
```

### 5. Commit and Push

```bash
git add src/ontology/mma-edit.owl
git commit -m "Add new terms for X"
git push origin your-feature-branch
```

### 6. Create Pull Request

Create a pull request on GitHub and wait for automated checks to pass.

## Adding New Terms

When adding new terms, ensure you include:

- **Label**: Human-readable name
- **Definition**: Clear description with source citation
- **Parent class**: Appropriate superclass
- **Synonyms**: Alternative names (if applicable)

## ID Ranges

Each editor should use their assigned ID range. Check `src/ontology/mma-idranges.owl` for your range.

