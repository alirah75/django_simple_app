from django import forms
from.models import Todo


class TodoCreatedForm(forms.Form):
    title = forms.CharField(label='Subject', required=True)
    content = forms.CharField()
    created = forms.DateTimeField()


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = {'title', 'content', 'created'}
