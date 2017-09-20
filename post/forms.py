from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 5,
        'cols': 50,
        'placeholder': '256자까지 등록 가능합니다. \n#태그명 을 통해서 검색 태그를 등록할 수 있습니다. \n예시 : I #love #coding!',}))

    class Meta:
        model = Post
        fields = ['photo', 'content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={
        'size': '80px',
        'placeholder': '댓글 달기...',
        'maxlength': '255',
    }))

    class Meta:
        model = Comment
        fields = ['content']
