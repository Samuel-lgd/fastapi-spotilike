# Spotilike doc
---

## Installation

### Pré-requis
- Python 3.10
- MySQL
- Virtualenv

### Étapes

1. **Installer les dépendances backend**
```
cd backend
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. **Initialiser la base de données**

Peut se faire avec les script dans backend/ressources ou alors avec
```
mysql -u root -p < backend\ressources\database_creation.sql.sql
```

Puis ajouter des données de test
```
mysql -u root -p spotilike_db < backend\ressources\test_data.sql
```

3. **lancement du serveur FastAPI**
```
uvicorn backend.app.main:app --reload
```

4. **frontend**

Simplement ouvrir le fichier index.html