from django import forms
from .models import CommentModel, ReplyCommentModel


class NewCommentForm(forms.ModelForm):
    comment_text = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is in your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = CommentModel
        fields = ['comment_text', ]




class ReplyForm(forms.ModelForm):
    class Meta:
        model = ReplyCommentModel
        fields = ['reply_comment_text', ]
