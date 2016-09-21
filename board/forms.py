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
                'class': 'form-control',
            }),
            'name': forms.fields.TextInput(attrs={
                'placeholder': '이름',
                'class': 'form-control',
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
        fields = ('name', 'reply', 'password')
        widgets = {
            'name':forms.fields.TextInput(attrs={
                'placeholder':'이름',
                'class': 'form-control',
            }),
            'reply':forms.Textarea(attrs={
                'placeholder':'댓글',
                'class': 'form-control',
                'rows':3,
                'cols':100,
            }),
            'password':forms.PasswordInput(attrs={
                'placeholder': '비밀번호',
                'class': 'form-control',
            })
        }

    def save(self, for_board, ipaddress, depth_id, password):
        self.instance.board = for_board
        self.instance.ipaddress = ipaddress
        self.instance.depth_id = depth_id
        return super().save()