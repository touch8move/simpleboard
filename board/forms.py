from django import forms
from board.models import Board
class BoardForm(forms.models.ModelForm):
    
    class Meta:
        model = Board 
        fields = ('subject','name','contents',)
        # attrs={novalidate:'novalidate'}
        widgets = {
            'subject': forms.fields.TextInput(attrs={
                'placeholder': '제목',
                'class': 'form-control input-lg',
            }),
            'name': forms.fields.TextInput(attrs={
                'placeholder': '이름',
                'class': 'form-control input-lg',
            }),
            'contents': forms.Textarea(attrs={
                'cols': 80, 
                'rows': 20,
                'placeholder': '글',
                'class': 'form-control input-lg',
            }),
        }