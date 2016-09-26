from django import forms
from board.models import Board, Reply

class BoardForm(forms.models.ModelForm):
    
    class Meta:
        model = Board 
        fields = ('id', 'subject','name','contents',)
        # attrs={novalidate:'novalidate'}
        widgets = {
            'subject': forms.fields.TextInput(attrs={
                'placeholder': '제목',
                'class': 'form-control input-sm',
            }),
            'name': forms.fields.TextInput(attrs={
                'placeholder': '이름',
                'class': 'form-control input-sm',
            }),
            'contents': forms.Textarea(attrs={
                'rows': 20,
                'placeholder': '글',
                'class': 'form-control',
            }),
        }


class ReplyForm(forms.models.ModelForm):
    class Meta:
        model = Reply
        fields = ('name', 'comment', 'password')
        widgets = {
            'name':forms.fields.TextInput(attrs={
                'placeholder':'이름',
                'class': 'form-control input-sm',
            }),
            'comment':forms.Textarea(attrs={
                'placeholder':'댓글',
                'class': 'form-control',
                'rows':3,
                'cols':90,
            }),
            'password':forms.PasswordInput(attrs={
                'placeholder': '비밀번호',
                'class': 'form-control input-sm',
            })
        }

    def save(self, for_board, ipaddress, parent, depth):
        self.instance.board = for_board
        self.instance.ipaddress = ipaddress
        self.instance.parent = parent
        self.instance.depth = depth
        return super().save()