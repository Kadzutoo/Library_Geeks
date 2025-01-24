from django import forms
from . import models, parser_kinogo

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('kinoogo', 'kinoogo'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type'
        ]
    def parser_data(self):
        if self.data['media_type'] == 'kinoogo':
            kinoogo_file = parser_kinogo.parsing()
            for i in kinoogo_file:
                models.KinoogoParser.objects.create(**i)