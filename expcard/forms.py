from django.contrib.auth.models import User
from django import forms
from .models import ExpCards


class ExpCardsForm(forms.ModelForm):
    class Meta:
        model = ExpCards
        fields = ('MO_expert', 'FIO_expert', 'Name_Org_expert', 'Position_expert', 'Level_expert', 'MO_att', 'FIO_att',
                  'Name_Org_att', 'Position_att', 'Category', 'Result')


class CokoExpCardsForm(forms.ModelForm):
    class Meta:
        model = ExpCards
        fields = ('MO_att', 'FIO_att', 'Name_Org_att', 'Position_att', 'Category', 'Result')
