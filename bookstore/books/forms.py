from django import forms

class BookAdd(forms.Form):
    bookname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    author=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    availablility=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data["price"]
        if price<0:
            msg='invalid price'

            self.add_error('price',msg)