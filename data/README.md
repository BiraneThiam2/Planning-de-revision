# 🎓 Smart Study Planner

> Un générateur de planning de révision intelligent basé sur l'aide à la décision

Application Python qui génère automatiquement un planning de révision optimisé en fonction des contraintes de temps, des priorités personnelles et des dates d'examen.

---

## 📋 Table des matières

- [Aperçu](#-aperçu)
- [Fonctionnalités](#-fonctionnalités)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Structure du projet](#-structure-du-projet)
- [Algorithme](#-algorithme)
- [Exemple](#-exemple)
- [Technologies](#-technologies)
- [Limites](#-limites)
- [Améliorations futures](#-améliorations-futures)
- [Contribution](#-contribution)
- [Licence](#-licence)

---

## 🎯 Aperçu

### Problème

Les étudiants font face à plusieurs défis lors de la préparation de leurs examens :
- ⏰ Gestion du temps limitée
- 🎯 Difficulté à prioriser les matières
- 😰 Stress face aux examens qui approchent
- 🧠 Surcharge cognitive de la planification manuelle

### Solution

**Smart Study Planner** résout ces problèmes en :
1. Calculant automatiquement l'urgence de chaque examen
2. Établissant un score de priorité multi-critères
3. Générant un planning optimisé jour par jour
4. Respectant les contraintes de temps quotidien

---

## ✨ Fonctionnalités

- ✅ **Calcul intelligent de l'urgence** basé sur les dates d'examen
- ✅ **Scoring multi-critères** (priorité, difficulté, urgence)
- ✅ **Génération automatique de planning** jour par jour
- ✅ **Optimisation de la charge de travail** (sessions de 0.5h à 2h)
- ✅ **Statistiques détaillées** (volume total, charge moyenne)
- ✅ **Interface en ligne de commande** simple et intuitive
- ✅ **Configuration JSON** facile à modifier

---

## 🚀 Installation

### Prérequis

- Python 3.7 ou supérieur
- Aucune dépendance externe requise (utilise uniquement la bibliothèque standard)

### Étapes

1. **Cloner le dépôt**
```bash
git clone https://github.com/votre-username/smart-study-planner.git
cd smart-study-planner
```

2. **Créer le dossier de données**
```bash
mkdir data
```

3. **Créer le fichier de configuration**

Créez `data/subjects.json` avec vos matières :

```json
{
  "matières": [
    {
      "nom": "Intelligence Artificielle",
      "date_examen": "2025-01-15",
      "difficulte": 5,
      "priorite": 5,
      "heures_necessaires": 20
    },
    {
      "nom": "Mathématiques",
      "date_examen": "2025-01-20",
      "difficulte": 4,
      "priorite": 4,
      "heures_necessaires": 15
    }
  ]
}
```

4. **Lancer le programme**
```bash
python main.py
```

---

## 💻 Utilisation

### Commande de base

```bash
python main.py
```

### Interaction

```
🎓 SMART STUDY PLANNER
============================================================

📚 Chargement des matières depuis data/subjects.json...
✅ 6 matières chargées avec succès

⚙️  CONFIGURATION DU PLANNING
Combien d'heures pouvez-vous étudier par jour ? (ex: 3): 3

🗓️  VOTRE PLANNING DE RÉVISION
============================================================

📆 LUNDI 2024-12-23
   Charge: 3.0h
   
   • Intelligence Artificielle: 2.0h
   • Mathématiques: 1.0h

📆 MARDI 2024-12-24
   Charge: 3.0h
   
   • Intelligence Artificielle: 2.0h
   • Mathématiques: 1.0h
   
...

📈 STATISTIQUES DU PLANNING
============================================================
Durée totale: 28 jours
Volume total: 83.0 heures
Moyenne par jour: 3.0h

✅ Planning généré avec succès!
```

---
 
## 📁 Structure du projet

```
smart-study-planner/
│
├── main.py              # Point d'entrée du programme
├── planner.py           # Logique de planification intelligente
├── data/
│   └── subjects.json    # Configuration des matières et examens
├── README.md            # Documentation
└── LICENSE              # Licence du projet
```

### Description des fichiers

| Fichier | Description |
|---------|-------------|
| `main.py` | Interface utilisateur et affichage des résultats |
| `planner.py` | Classe `StudyPlanner` contenant toute la logique décisionnelle |
| `subjects.json` | Données d'entrée (matières, dates, priorités) |

---

## 🧮 Algorithme

### 1. Calcul de l'urgence

```
urgence_inverse = 30 / nombre_de_jours_restants
```

**Principe** : Plus l'examen est proche, plus l'urgence augmente de façon exponentielle.

**Exemple** :
- Examen dans 3 jours → urgence = 10.0 (🔴 critique)
- Examen dans 15 jours → urgence = 2.0 (🟡 modéré)
- Examen dans 30 jours → urgence = 1.0 (🟢 confortable)

### 2. Score de priorité

```
score = (priorité × 2) + difficulté + urgence_inverse
```

**Justification** :
- **Priorité × 2** : Respecte les objectifs personnels (poids le plus important)
- **Difficulté** : Les matières difficiles nécessitent plus de temps
- **Urgence** : Les examens imminents deviennent critiques

### 3. Génération du planning

**Algorithme glouton** :
1. Trier les matières par score décroissant
2. Pour chaque jour :
   - Allouer du temps aux matières prioritaires
   - Respecter la limite d'heures quotidienne
   - Sessions de 0.5h à 2h (éviter la fatigue)
3. Continuer jusqu'à allocation complète

---

## 📊 Exemple

### Configuration d'entrée

```json
{
  "matières": [
    {
      "nom": "Intelligence Artificielle",
      "date_examen": "2025-01-15",
      "difficulte": 5,
      "priorite": 5,
      "heures_necessaires": 20
    },
    {
      "nom": "Marketing Digital",
      "date_examen": "2025-01-30",
      "difficulte": 2,
      "priorite": 3,
      "heures_necessaires": 10
    }
  ]
}
```

### Résultat de l'analyse

| Matière | Score | Jours restants | Urgence |
|---------|-------|----------------|---------|
| Intelligence Artificielle | 21.0 | 18 | 🔴 Élevée |
| Marketing Digital | 10.0 | 33 | 🟢 Faible |

### Planning généré

**Semaine 1** :
- Lundi à Vendredi : Focus sur IA (2h/jour) + Maths (1h/jour)
- Weekend : Révision IA

**Semaine 2** :
- Lundi à Mercredi : Fin IA + Début Marketing
- Jeudi-Vendredi : Marketing intensif

---

## 🛠️ Technologies

| Technologie | Version | Usage |
|-------------|---------|-------|
| **Python** | 3.7+ | Langage principal |
| **json** | Standard | Lecture/écriture des données |
| **datetime** | Standard | Calcul des dates et de l'urgence |

**Aucune installation de bibliothèque externe nécessaire** ✅

---

## ⚠️ Limites

### Limites actuelles

- ❌ **Pas d'adaptation dynamique** : Le planning ne s'ajuste pas selon les performances
- ❌ **Contraintes basiques** : Ne gère pas les indisponibilités personnelles
- ❌ **Interface textuelle** : Pas de visualisation graphique
- ❌ **Pas de persistance** : Pas de sauvegarde du planning généré

### Hypothèses du modèle

- ⚙️ Temps quotidien fixe (pas de variation)
- ⚙️ Disponibilité tous les jours (pas de jours de repos)
- ⚙️ Efficacité constante (même niveau de concentration)
- ⚙️ Estimation fiable des heures nécessaires

---

## 🚀 Améliorations futures

### Court terme
- [ ] Export du planning en PDF/CSV
- [ ] Gestion des jours de repos (weekends, vacances)
- [ ] Visualisation avec matplotlib
- [ ] Interface graphique (Tkinter/PyQt)

### Moyen terme
- [ ] Base de données SQLite pour persistance
- [ ] Suivi de progression (validation des sessions)
- [ ] Recommandations de méthodes d'apprentissage
- [ ] API REST pour intégration externe

### Long terme
- [ ] Machine Learning : prédiction du temps nécessaire
- [ ] Application web (Flask/Django)
- [ ] Synchronisation multi-appareils
- [ ] Algorithmes d'optimisation avancés (programmation linéaire)

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment participer :

1. **Fork** le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une **Pull Request**

### Guidelines

- Respecter le style de code existant
- Ajouter des docstrings pour les nouvelles fonctions
- Tester vos modifications avant de soumettre

---

## 📚 Contexte académique

**Programme** : Intelligence Artificielle & Stratégie des Affaires  
**Objectif pédagogique** : Démontrer la capacité à concevoir un système d'aide à la décision

**Compétences mobilisées** :
- 🧠 Algorithmique et programmation
- 📊 Modélisation de problèmes décisionnels
- 🎯 Optimisation sous contraintes
- 📝 Documentation technique

---

## 📄 Licence

Ce projet est sous licence de Swiss UMEF University Campus Dakar

---

## 👤 Auteur

El Hadji Birane Cisse THIAM
- Email: biranethiam916@gmail.com.com

---

## 🙏 Remerciements

- Inspiré par les principes d'aide à la décision et d'optimisation
- Développé dans le cadre d'un projet académique en IA & Stratégie

---
