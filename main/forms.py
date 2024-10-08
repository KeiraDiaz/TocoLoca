from django.forms import ModelForm
from main.models import ItemEntry
from django.utils.html import strip_tags

class ItemEntryForm(ModelForm):
    class Meta:
        model = ItemEntry
        fields = ["name", "price", "desc"]

    def clean_mood(self):
        mood = self.cleaned_data["name"]
        return strip_tags(mood)

    def clean_feelings(self):
        feelings = self.cleaned_data["desc"]
        return strip_tags(feelings)