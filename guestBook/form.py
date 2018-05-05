from django import forms


class CommentForm(forms.Form):
    # Also we have to set css propeties here.
    name_input = forms.CharField(max_length=20,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'})
                                 )
    comment_input = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}))
