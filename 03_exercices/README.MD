# Installation de l'environnement Python

## 1. Créer l'environnement virtuel

### Windows
```bash
python -m venv .venv
````

### Linux / macOS

```bash
python3 -m venv .venv
```

## 2. Activer l'environnement virtuel

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

## 4. Vérifier l'installation

```bash
pip list
```

## 5. Désactiver l'environnement virtuel

```bash
deactivate
```


## 6. VS Code et environnement virtuel

Si VS Code ne trouve pas les dépendances installées, sélectionne l’interpréteur du `venv` :

1. `Ctrl + Shift + P`
2. `Python: Select Interpreter`
3. Choisir le Python dans `.venv`

Exemple :
- Windows : `.venv\Scripts\python.exe`
- Linux / macOS : `.venv/bin/python`

