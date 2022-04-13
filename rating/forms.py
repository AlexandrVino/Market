from django import forms

from rating.models import Rating


class AddRate(forms.ModelForm):

    star = forms.ChoiceField(
        choices=(
            (1, 'Ненависть'), (2, 'Неприязнь'), (3, 'Нейтрально'),
            (4, 'Обожание'), (5, 'Любовь'), (0, 'Не могу сказать')),
        widget=forms.Select(attrs={
            'class': 'form-control input-field',
            'id': 'select_rate'
        }),
    )

    class Meta:
        model = Rating
        fields = ('star', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

