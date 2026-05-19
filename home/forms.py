from django import forms

class BookForm(forms.Form):
    name = forms.CharField(label="Ваше имя и фамилия", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    phone = forms.CharField(label="Номер телефона", max_length=18, required=True)
    guests = forms.IntegerField(label="Количество гостей", min_value=1, required=True)