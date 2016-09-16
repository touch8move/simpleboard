from django import forms
from board.models import Board
class BoardForm(forms.models.ModelForm):
    class Meta:
        model = Board
    #     id = models.IntegerField(primary_key=True)
    # subject = models.CharField(max_length=50, blank=True)
    # name = models.CharField(max_length=50, blank=True)
    # created_date = models.DateField(null=True, blank=True)
    # mail = models.CharField(max_length=50, blank=True)
    # memo = models.CharField(max_length=200, blank=True)
    # hits = models.IntegerField(null=True, blank=True) 
        fields = ('subject','name','contents',)
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
        # error_messages = {
        #     'subject': {'required': EMPTY_ITEM_ERROR}
        # }
        # def save():
    # def save(self):
        # return super().save()
