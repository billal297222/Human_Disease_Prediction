from django import forms

# Symptom choices (should match those used in views.py)
SYMPTOM_CHOICES = [
    ('', 'Select a symptom'),  # Default empty choice
    ('itching', 'Itching'),
    ('skin_rash', 'Skin Rash'),
    ('nodal_skin_eruptions', 'Nodal Skin Eruptions'),
    ('continuous_sneezing', 'Continuous Sneezing'),
    ('shivering', 'Shivering'),
    ('chills', 'Chills'),
    ('joint_pain', 'Joint Pain'),
    ('stomach_pain', 'Stomach Pain'),
    ('acidity', 'Acidity'),
    ('ulcers_on_tongue', 'Ulcers on Tongue'),
    ('cough', 'Cough'),
    ('high_fever', 'High Fever'),
    ('fatigue', 'Fatigue'),
    ('headache', 'Headache'),
    ('nausea', 'Nausea'),
    ('loss_of_appetite', 'Loss of Appetite'),
    ('shortness_of_breath', 'Shortness of Breath'),
    ('throat_irritation', 'Throat Irritation'),
    ('runny_nose', 'Runny Nose'),
]

# Algorithm choices
ALGO_CHOICES = [
    ('DecisionTree', 'Decision Tree'),
    ('RandomForest', 'Random Forest'),
    ('NaiveBayes', 'Naive Bayes'),
]

class DiseasePredictionForm(forms.Form):
    Name = forms.CharField(
        label="Name of Patient",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': "Enter patient's name"})
    )
    
    symptom1 = forms.ChoiceField(choices=SYMPTOM_CHOICES, required=True, label="Symptom 1")
    symptom2 = forms.ChoiceField(choices=SYMPTOM_CHOICES, required=False, label="Symptom 2")
    symptom3 = forms.ChoiceField(choices=SYMPTOM_CHOICES, required=False, label="Symptom 3")
    symptom4 = forms.ChoiceField(choices=SYMPTOM_CHOICES, required=False, label="Symptom 4")
    symptom5 = forms.ChoiceField(choices=SYMPTOM_CHOICES, required=False, label="Symptom 5")
    
    algo = forms.ChoiceField(
        choices=ALGO_CHOICES,
        required=True,
        widget=forms.RadioSelect(),
        label="Which Algorithm You Want To Use"
    )
