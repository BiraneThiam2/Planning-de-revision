# Contient la logique de calcul de priorités et de génération de planning

import json
from datetime import datetime, timedelta

class StudyPlanner:
    """
    Classe principale pour la gestion intelligente du planning de révision
    """
    
    def __init__(self):
        self.subjects = []
        self.today = datetime.now()
    
    def load_subjects(self, filepath):
        """
        Charge les matières depuis un fichier JSON
        
        Args:
            filepath (str): Chemin vers le fichier JSON
        
        Raises:
            FileNotFoundError: Si le fichier n'existe pas
            JSONDecodeError: Si le JSON est mal formaté
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.subjects = data.get('matières', [])
    
    def calculate_urgency(self):
        """
        Calcule l'urgence pour chaque matière en fonction de la date d'examen
        
        Logique:
        - Plus l'examen est proche, plus l'urgence est élevée
        - urgence_inverse = 1 / nombre de jours (pour donner plus de poids aux dates proches)
        """
        for subject in self.subjects:
            exam_date = datetime.strptime(subject['date_examen'], '%Y-%m-%d')
            days_remaining = (exam_date - self.today).days
            
            # Éviter la division par zéro
            if days_remaining <= 0:
                days_remaining = 1
            
            subject['jours_restants'] = days_remaining
            # Plus l'examen est proche, plus l'urgence_inverse est grande
            subject['urgence_inverse'] = 30 / days_remaining
    
    def calculate_priority_score(self, subject):
        """
        Calcule le score de priorité d'une matière
        
        Formule: score = (priorité × 2) + difficulté + urgence_inverse
        
        Justification:
        - priorité × 2 : La priorité personnelle a le plus de poids
        - difficulté : Les matières difficiles nécessitent plus de temps
        - urgence_inverse : Les examens proches deviennent critiques
        
        Args:
            subject (dict): Matière avec ses attributs
        
        Returns:
            float: Score de priorité calculé
        """
        priority = subject.get('priorite', 3)
        difficulty = subject.get('difficulte', 3)
        urgency = subject.get('urgence_inverse', 1)
        
        score = (priority * 2) + difficulty + urgency
        return score
    
    def sort_by_priority(self):
        """
        Trie les matières par ordre décroissant de score de priorité
        Les matières les plus prioritaires apparaissent en premier
        """
        for subject in self.subjects:
            subject['score'] = self.calculate_priority_score(subject)
        
        self.subjects.sort(key=lambda x: x['score'], reverse=True)
    
    def generate_schedule(self, hours_per_day):
        """
        Génère un planning de révision optimisé
        
        Algorithme:
        1. Distribuer les heures de chaque matière sur plusieurs jours
        2. Respecter la limite d'heures par jour
        3. Prioriser les matières avec score élevé
        
        Args:
            hours_per_day (float): Nombre d'heures d'étude quotidiennes
        
        Returns:
            dict: Planning organisé par jour
        """
        schedule = {}
        current_day = self.today
        day_names = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        
        # Copie des heures restantes pour chaque matière
        remaining_hours = {
            subject['nom']: subject['heures_necessaires'] 
            for subject in self.subjects
        }
        
        # Génération du planning jour par jour
        max_days = 60  # Limite de sécurité
        day_count = 0
        
        while any(h > 0 for h in remaining_hours.values()) and day_count < max_days:
            day_name = day_names[current_day.weekday()]
            date_str = current_day.strftime('%Y-%m-%d')
            day_label = f"{day_name} {date_str}"
            
            daily_sessions = []
            hours_allocated = 0
            
            # Allouer du temps aux matières selon leur priorité
            for subject in self.subjects:
                subject_name = subject['nom']
                
                if remaining_hours[subject_name] <= 0:
                    continue
                
                # Temps restant dans la journée
                available_time = hours_per_day - hours_allocated
                
                if available_time <= 0:
                    break
                
                # Allouer du temps (minimum 30 min, maximum 2h par session)
                time_to_allocate = min(
                    remaining_hours[subject_name],
                    available_time,
                    2.0  # Maximum 2h par session pour éviter la fatigue
                )
                
                if time_to_allocate >= 0.5:  # Sessions minimum de 30 minutes
                    daily_sessions.append({
                        'matiere': subject_name,
                        'duree': time_to_allocate
                    })
                    
                    remaining_hours[subject_name] -= time_to_allocate
                    hours_allocated += time_to_allocate
            
            # Ajouter la journée au planning si elle contient des sessions
            if daily_sessions:
                schedule[day_label] = daily_sessions
            
            current_day += timedelta(days=1)
            day_count += 1
        
        return schedule
    
    def get_statistics(self):
        """
        Calcule des statistiques sur le planning
        
        Returns:
            dict: Statistiques (heures totales, nombre de matières, etc.)
        """
        total_hours = sum(s['heures_necessaires'] for s in self.subjects)
        avg_difficulty = sum(s['difficulte'] for s in self.subjects) / len(self.subjects)
        
        return {
            'total_heures': total_hours,
            'nombre_matieres': len(self.subjects),
            'difficulte_moyenne': avg_difficulty
        }