from django import forms
from .models import Pokemon, Trainer

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name', 'type', 'weight', 'height', 'picture', 'trainer']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Charmander'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fuego'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id' : 'image_field'
            }),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
        }
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'birth_date', 'level', 'picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ash Ketchum'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'level': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id' : 'image_field'
            }),
        }