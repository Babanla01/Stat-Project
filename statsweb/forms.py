from django import forms

class NumbersForm(forms.Form):
    numbers = forms.CharField(
        label="Enter numbers separated by commas",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. 10, 20, 30', 'size': 100})
    )
