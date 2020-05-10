from django import forms
from froala_editor.widgets import FroalaEditor
from comment.models import Comment


class CommentForm(forms.ModelForm):
    message = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Comment
        fields = ('message',)
