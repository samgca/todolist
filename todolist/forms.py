from django.forms import ModelForm
from .models import Note


class NoteForm(ModelForm):

    class Meta:
        model = Note
        exclude = ['created_at']

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'full-width'})
        self.fields['note_text'].widget.attrs.update({'class': 'full-width'})
        self.fields['status'].widget.attrs.update({'class': 'full-width'})
