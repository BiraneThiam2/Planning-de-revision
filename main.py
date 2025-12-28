#Genere automatiquement un planning de revision intelligent

from planner import StudyPlanner
import json
from datetime import datetime

def main (): # Fonction principale
    print("=" * 60) 
    print("🎓 Planning de Révision Intelligent")
    print("=" * 60)
    print()

    # Initialisation du planificateur d'étude
    planner = StudyPlanner()

    # chargement des données utilisateur
    print("📚 Chargement des matières")
    try:
        planner.load_subjects("data/subjects.json")
        print(f"✅ {len(planner.subjects)} matières chargées avec succès\n")
    except FileNotFoundError:
        print("❌ Erreur: Le fichier data/subjects.json n'existe pas")
        print("📝 Créez le fichier avec vos matières d'abord")
        return
    except json.JSONDecodeError:
        print ("❌ Erreur: Le fichier JSON est mal formaté")
        return
    # Affichage des matières chargées
    print ("-" * 60)
    print("📋 Matières chargées:")
    print("-" * 60)
    for subject in planner.subjects:
        print(f" • {subject['nom']}")
        print(f"  Date d'examen: {subject['date_examen']}")
        print(f"  Difficulté: {subject['difficulte']}/5")
        print(f"  Priorité: {subject['priorite']}/5")
        print(f"  Heures nécessaires: {subject['heures_necessaires']}h")
        print()
    
    # Configuration du planning
    print("-" * 60)
    print("⚙️  CONFIGURATION DU PLANNING")
    print("-" * 60)
    
    try:
        heures_par_jour = float(input("Combien d'heures pouvez-vous étudier par jour ? (ex: 3): "))
        if heures_par_jour <= 0:
            print("❌ Le nombre d'heures doit être positif")
            return
    except ValueError:
        print("❌ Veuillez entrer un nombre valide")
        return
    
    print()
    
    # Calcul de l'urgence et tri des priorités
    print("🧮 Calcul des priorités et de l'urgence...")
    planner.calculate_urgency()
    planner.sort_by_priority()
    
    # Affichage de l'analyse des priorités
    print()
    print("-" * 60)
    print("📊 ANALYSE DES PRIORITÉS")
    print("-" * 60)
    for i, subject in enumerate(planner.subjects, 1): # Affichage des matières avec priorité
        jours_restants = subject['jours_restants']
        urgence_label = "🔴 URGENT" if jours_restants < 7 else "🟡 Modéré" if jours_restants < 14 else "🟢 Temps suffisant"
        
        print(f"{i}. {subject['nom']}")
        print(f"   Score de priorité: {subject['score']:.2f}")
        print(f"   Jours restants: {jours_restants} ({urgence_label})")
        print(f"   Temps requis: {subject['heures_necessaires']}h")
        print()
    
    # Génération du planning
    print("-" * 60)
    print("📅 GÉNÉRATION DU PLANNING")
    print("-" * 60)
    planning = planner.generate_schedule(heures_par_jour)
    
    if not planning:
        print("❌ Impossible de générer un planning avec les contraintes données")
        return
    
    # Affichage du planning
    print()
    print("=" * 60)
    print("🗓️  VOTRE PLANNING DE RÉVISION")
    print("=" * 60)
    print()
    
    total_jours = 0
    total_heures = 0
    
    for jour, sessions in planning.items():
        total_jours += 1
        heures_jour = sum(s['duree'] for s in sessions)
        total_heures += heures_jour
        
        print(f"📆 {jour.upper()}")
        print(f"   Charge: {heures_jour:.1f}h")
        print()
        
        for session in sessions:
            print(f"   • {session['matiere']}: {session['duree']:.1f}h")
        print()
    
    # Statistiques finales
    print("=" * 60)
    print("📈 STATISTIQUES DU PLANNING")
    print("=" * 60)
    print(f"Durée totale: {total_jours} jours")
    print(f"Volume total: {total_heures:.1f} heures")
    print(f"Moyenne par jour: {total_heures/total_jours:.1f}h")
    print()
    print("✅ Planning généré avec succès!")
    print("=" * 60)

if __name__ == "__main__":
    main()