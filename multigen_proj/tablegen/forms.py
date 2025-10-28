# tablegen/forms.py
from django import forms

class TableForm(forms.Form):
    base = forms.IntegerField(
        label="Base number",
        min_value=-1000000, max_value=1000000,
        widget=forms.NumberInput(attrs={'placeholder':'e.g. 7', 'autocomplete':'off'})
    )
    start = forms.IntegerField(
        label="Start multiplier",
        initial=1,
        widget=forms.NumberInput(attrs={'placeholder':'start (e.g. 1)'})
    )
    end = forms.IntegerField(
        label="End multiplier",
        initial=10,
        widget=forms.NumberInput(attrs={'placeholder':'end (e.g. 10)'})
    )
    step = forms.IntegerField(
        label="Step",
        initial=1,
        min_value=1,
        widget=forms.NumberInput(attrs={'placeholder':'step (e.g. 1)'})
    )

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get('start')
        end = cleaned.get('end')
        step = cleaned.get('step')
        if start is not None and end is not None and step is not None:
            if step <= 0:
                raise forms.ValidationError('Step must be positive.')
            # Allow start > end (descending ranges) — no error; handle in view.
        return cleaned
