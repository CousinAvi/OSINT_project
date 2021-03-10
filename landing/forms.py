from django import forms
from django.forms import TextInput
from .models import *

class  PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [""]

class UserForm(forms.Form):
    name = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Введите ip адрес или домен',
                                    'class': "mt-4 form-control"}))
class UserFormExcept(forms.Form):
    name = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Повторите ввод, введите ip адрес или домен',
                                    'class': "mt-4 form-control",
                                    }))

class UserForm_eng(forms.Form):
    name = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Input IP or domen',
                                    'class': "mt-4 form-control"}))
class UserFormExcept_eng(forms.Form):
    name = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Retry input',
                                    'class': "mt-4 form-control",
                                    }))




class NumberForm(forms.Form):
    formovka = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Введите номер телефона в формате +7-***-**-**-***',
                                    'class': "mt-4 form-control",
                                    'value':'+7',
                                    'maxlength':'16',
                                    }))

class NumberFormExcept(forms.Form):
    formovka = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Повторите ввод, +7-***-**-**-***',
                                    'class': "mt-4 form-control",
                                    'value':'',
                                    'maxlength':'16'}))

class NumberForm_eng(forms.Form):
    formovka = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Input phone number +7-***-**-**-***',
                                    'class': "mt-4 form-control",
                                    'value':'+7',
                                    'maxlength':'16',
                                    }))

class NumberFormExcept_eng(forms.Form):
    formovka = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Retry input +7-***-**-**-***',
                                    'class': "mt-4 form-control",
                                    'value':'',
                                    'maxlength':'16'}))

class OGRNForm(forms.Form):
    name = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Введите ИНН, ОГРН, название организации, ФИО владельца ИП',
                                    'class': "mt-4 form-control",
                                    }))

class OGRNFormExcept(forms.Form):
    name = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Повторите ввод, некорректные данные',
                                    'class': "mt-4 form-control",
                                    }))

class OGRNForm_eng(forms.Form):
    name = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Enter TIN, PSRN, name of organization, name of owner',
                                    'class': "mt-4 form-control",
                                    }))

class OGRNFormExcept_eng(forms.Form):
    name = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Retry input',
                                    'class': "mt-4 form-control",
                                    }))

class BondForm(forms.Form):
    name = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Введите id источника',
                                    'class': "mt-4 form-control",
                                    }))
    age = forms.IntegerField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Введите id цели',
                                    'class': "mt-1 form-control",
                                    }))

class BondFormExcept(forms.Form):
    name = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Повторите ввод id источника',
                                    'class': "mt-4 form-control",
                                    }))
    age = forms.IntegerField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Повторите ввод id цели',
                                    'class': "mt-1 form-control",
                                    }))

class BondForm_eng(forms.Form):
    name = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Input source id',
                                    'class': "mt-4 form-control",
                                    }))
    age = forms.IntegerField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Input destination id',
                                    'class': "mt-1 form-control",
                                    }))

class BondFormExcept_eng(forms.Form):
    name = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Retry input',
                                    'class': "mt-4 form-control",
                                    }))
    age = forms.IntegerField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Retry input',
                                    'class': "mt-1 form-control",
                                    }))


class CarForm(forms.Form):
    formovka = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': "Формат ввода 'А000АА125'" ,
                                    'class': "mt-4 form-control",
                                    }))

class CarFormExcept(forms.Form):
    formovka = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Повторите ввод, используйте русский алфавит',
                                    'class': "mt-4 form-control",
                                    }))


class NicknameForm(forms.Form):
    formovka = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Введите никнейм или email',
                                    'class': "mt-4 form-control",
                                    }))

class NicknameFormExcept(forms.Form):
    formovka = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Повторите ввод',
                                    'class': "mt-4 form-control",
                                    }))

class NicknameForm_eng(forms.Form):
    formovka = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Input nickname or email',
                                    'class': "mt-4 form-control",
                                    }))

class NicknameFormExcept_eng(forms.Form):
    formovka = forms.CharField(label='',
    widget=forms.TextInput(attrs={'placeholder': 'Retry imput',
                                    'class': "mt-4 form-control",
                                    }))



class CryptoForm(forms.Form):
    addresses = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Введите адреса криптокошелька через запятую',
            'class': 'mt-4 form-control'}))

    tokens = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Введите адреса ERC-20 токенов',
            'class': 'mt-4 form-control'}))

class CryptoForm_eng(forms.Form):
    addresses = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter the addresses of the crypto wallet separated by commas',
            'class': 'mt-4 form-control'}))

    tokens = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter ERC-20 Token Addresses',
            'class': 'mt-4 form-control'}))

class BiometryForm_url(forms.Form):
    url = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Введите URL картинки',
            'class': 'mt-4 form-control'}))

class BiometryForm_photo(forms.Form):
    photo = forms.FileField()

class BiometryForm_url_eng(forms.Form):
    url = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Input URL',
            'class': 'mt-4 form-control'}))

class BiometryForm_photo_eng(forms.Form):
    photo = forms.FileField()

class TxchainForm(forms.Form):
    contract = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Введите адрес токена',
            'class': 'mt-4 form-control'}))

    source = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Введите адрес отправителя',
            'class': 'mt-4 form-control'}))

    destination = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Введите адрес получателя',
            'class': 'mt-4 form-control'}))

class TxchainForm_eng(forms.Form):
    contract = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter token address',
            'class': 'mt-4 form-control'}))

    source = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter source address',
            'class': 'mt-4 form-control'}))

    destination = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Enter destination address',
            'class': 'mt-4 form-control'}))

    #widget = {'name' : forms.TextInput(attrs={'placeholder': 'Введите домен или ip адрес'})}

    #age = forms.IntegerField()
  #<input type="text" id="domen" class="mt-4 form-control" name="domen"
#placeholder="Введите номер телефона">
