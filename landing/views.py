from django.shortcuts import render
from .forms import UserForm,NumberForm,OGRNForm,BondForm,CarForm,NumberFormExcept, CryptoForm, BiometryForm_url, TxchainForm, TxchainForm_eng
from .forms import UserFormExcept, OGRNFormExcept, NicknameForm, NicknameFormExcept, CryptoForm_eng, OGRNForm_eng, OGRNFormExcept_eng
from .forms import PostForm, CarFormExcept,BondFormExcept, BondForm_eng, BondFormExcept_eng, BiometryForm_photo
from .forms import NumberForm_eng,NumberFormExcept_eng, NicknameForm_eng, NicknameFormExcept_eng
from .forms import BiometryForm_url_eng, BiometryForm_photo_eng, UserForm_eng, UserFormExcept_eng
from python_base.shodanlike.main import SHODANLIKE
from python_base.phone_number.main import Phone_Number
from python_base.phone_number.google import Google_Search
from python_base.OGRN.main import Econom_org
from python_base.VK_bond.main import VK_bond
from python_base.car.main import CarSearch
from python_base.Biometry.main import Biometry

import requests
from python_base.crypto.main import Crypto
from python_base.txchain.main import Txchain
import geoip2.database
import sys
import socket
import threading
import socket
from multiprocessing import Pool
from googlesearch import search
import subprocess
from pyisemail import is_email

def landing(request):
    #return render_to_response('index.html')
    return render(request, 'landing/index_eng.html', locals())
def rus(request):
    #return render_to_response('index.html')
    return render(request, 'landing/index.html', locals())

def inform(request):
    return render(request, 'landing/inform.html', locals())

def inform_eng(request):
    return render(request, 'landing/eng/inform.html', locals())

def team(request):
    #return render(request, 'landing/work.html')
    return render(request, 'landing/team.html', locals())

def team_eng(request):
    #return render(request, 'landing/work.html')
    return render(request, 'landing/eng/team.html', locals())

def contact(request):
    return render(request, 'landing/post_edit.html')
    #return render(request, 'landing/contact.html', locals())


def post_new(request):

    form = PostForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        #print(form.cleaned_data)
        new_form = form.save()
        form = PostForm(request.POST or None)
        return render(request, 'landing/success.html', locals())
    return render(request, 'landing/post_edit.html', locals())

def post_new_eng(request):

    form = PostForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        #print(form.cleaned_data)
        new_form = form.save()
        form = PostForm(request.POST or None)
        return render(request, 'landing/eng/success.html', locals())
    return render(request, 'landing/eng/post_edit.html', locals())

def detail(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_get = x_forwarded_for.split(',')[-1].strip()
    else:
        ip_get = request.META.get('REMOTE_ADDR')


    if request.method == "POST":
        name = request.POST.get("name").rstrip()

        name = name.replace('https://','')
        name = name.replace('http://','')
        index = name.find('/')
        if index != -1:
            name = name[:index]
        temp = name
        if name.find('.') == -1:
            exceptform = UserFormExcept()
            info_all = {
            'city': ' '
            }
            context = {'info': info_all, 'form': exceptform}
            return render(request, 'landing/domen2.html', context)

        ip = SHODANLIKE('%s'%name)
        try:
            all_info = (ip.func(ip.main()[1]))
        except:
            exceptform = UserFormExcept()
            info_all = {
            'city': ' '
            }
            context = {'info': info_all, 'form': exceptform}
            return render(request, 'landing/domen2.html', context)


        info_all = {
        'input': temp,
        'domen': all_info[0],
        'ip': all_info[1],
        'podset': all_info[2],
        'country': all_info[3],
        'city': all_info[4],
        'company': all_info[5],
        'ASN': all_info[6],
        'connection_type': all_info[7],
        'specific': all_info[8],
        'latitude': all_info[9],
        'longitude': all_info[10]
        }
    else:
        try:
            ip = SHODANLIKE('%s'%ip_get)
            all_info = (ip.func(ip.main()[1]))
            info_all = {
            'input': 'Ваш ip: '+ip_get,
            'domen': all_info[0],
            'ip': all_info[1],
            'podset': all_info[2],
            'country': all_info[3],
            'city': all_info[4],
            'company': all_info[5],
            'ASN': all_info[6],
            'connection_type': all_info[7],
            'specific': all_info[8],
            'latitude': all_info[9],
            'longitude': all_info[10]
            }
        except:
            info_all = {
            'city': ' '
            }
    exceptform = UserFormExcept()
    userform = UserForm()
    context = {'info': info_all, 'form': userform}
    return render(request, 'landing/domen2.html', context)

def detail_eng(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_get = x_forwarded_for.split(',')[-1].strip()
    else:
        ip_get = request.META.get('REMOTE_ADDR')


    if request.method == "POST":
        name = request.POST.get("name").rstrip()

        name = name.replace('https://','')
        name = name.replace('http://','')
        index = name.find('/')
        if index != -1:
            name = name[:index]
        temp = name
        if name.find('.') == -1:
            exceptform = UserFormExcept_eng()
            info_all = {
            'city': ' '
            }
            context = {'info': info_all, 'form': exceptform}
            return render(request, 'landing/eng/domen2.html', context)

        ip = SHODANLIKE('%s'%name)
        try:
            all_info = (ip.func(ip.main()[1]))
        except:
            exceptform = UserFormExcept()
            info_all = {
            'city': ' '
            }
            context = {'info': info_all, 'form': exceptform}
            return render(request, 'landing/eng/domen2.html', context)


        info_all = {
        'input': temp,
        'domen': all_info[0],
        'ip': all_info[1],
        'podset': all_info[2],
        'country': all_info[3],
        'city': all_info[4],
        'company': all_info[5],
        'ASN': all_info[6],
        'connection_type': all_info[7],
        'specific': all_info[8],
        'latitude': all_info[9],
        'longitude': all_info[10]
        }
    else:
        try:
            ip = SHODANLIKE('%s'%ip_get)
            all_info = (ip.func(ip.main()[1]))
            info_all = {
            'input': 'Your ip: '+ip_get,
            'domen': all_info[0],
            'ip': all_info[1],
            'podset': all_info[2],
            'country': all_info[3],
            'city': all_info[4],
            'company': all_info[5],
            'ASN': all_info[6],
            'connection_type': all_info[7],
            'specific': all_info[8],
            'latitude': all_info[9],
            'longitude': all_info[10]
            }
        except:
            info_all = {
            'city': ' '
            }
    exceptform = UserFormExcept_eng()
    userform = UserForm_eng()
    context = {'info': info_all, 'form': userform}
    return render(request, 'landing/eng/domen2.html', context)


def number_info(request):
    if request.method == "POST":
        cifri = request.POST.get("formovka").rstrip()
        cifri = cifri.replace("-","")
        temp = cifri
        cifri = cifri.replace("+7","8")
        #rint(cifri[:2])
        exceptform = NumberFormExcept()

        if len(cifri) != 11 or ( (cifri[:2] != '+7') and (cifri[0] != '8')) or cifri[2:].isdigit() == False:
            info_all = {
            'VK': ' '
            }
            context = {'info': info_all, 'form': exceptform}
            return render(request, 'landing/number2.html', context)

        #номер подается в формате +7.........

        if temp[0] == '8':
            temp = '+7' + temp[1:]
        number = Phone_Number('%s'%temp)
        all_info = number.main()
        part = Google_Search('%s'%temp)

        massiv_VK = part.VK_func()
        if massiv_VK == []:
            VK_info = '-'
        else:
            VK_info = '+'
        print(massiv_VK)
        info_all = {
        'Номер': temp,
        'Оператор': all_info[0],
        'Локация': all_info[1],
        'Whatsapp': all_info[2],
        'VK': VK_info,
        'massiv': massiv_VK,
        'OK': all_info[4],
        'Facebook': all_info[5],
        #'Twitter': all_info[6],
        #'connection_type': all_info[7],
        }
    else:
        info_all = {
        'VK': ' '
        }

    phoneform = NumberForm()
    exceptform = NumberFormExcept()
    context = {'info': info_all, 'form': phoneform}
    return render(request, 'landing/number2.html', context)

def number_info_eng(request):
    if request.method == "POST":
        cifri = request.POST.get("formovka").rstrip()
        cifri = cifri.replace("-","")
        temp = cifri
        cifri = cifri.replace("+7","8")
        #rint(cifri[:2])
        exceptform = NumberFormExcept_eng()

        if len(cifri) != 11 or ( (cifri[:2] != '+7') and (cifri[0] != '8')) or cifri[2:].isdigit() == False:
            info_all = {
            'VK': ' '
            }
            context = {'info': info_all, 'form': exceptform}
            return render(request, 'landing/eng/number2.html', context)

        #номер подается в формате +7.........

        if temp[0] == '8':
            temp = '+7' + temp[1:]
        number = Phone_Number('%s'%temp)
        all_info = number.main()
        part = Google_Search('%s'%temp)

        massiv_VK = part.VK_func()
        if massiv_VK == []:
            VK_info = '-'
        else:
            VK_info = '+'
        info_all = {
        'Номер': temp,
        'Оператор': all_info[0],
        'Локация': all_info[1],
        'Whatsapp': all_info[2],
        'VK': VK_info,
        'massiv': massiv_VK,
        'OK': all_info[4],
        'Facebook': all_info[5],
        #'Twitter': all_info[6],
        #'connection_type': all_info[7],
        }
    else:
        info_all = {
        'VK': ' '
        }

    phoneform = NumberForm_eng()
    exceptform = NumberFormExcept_eng()
    context = {'info': info_all, 'form': phoneform}
    return render(request, 'landing/eng/number2.html', context)


def ogrn_info(request):
    if request.method == "POST":
        inform = request.POST.get("name").rstrip()
        try:
            part = Econom_org('%s'%inform)
            mould = part.main()
            mould = mould[1:]
        except:
            exceptform = OGRNFormExcept()
            mould = [{
            'инн': ' '
            }]
            context = {'all_info': mould, 'form': exceptform}
            return render(request, 'landing/credit2.html', context)

    else:
        mould = [{
        'инн': ' '
        }]
    exceptform = OGRNFormExcept()
    phoneform = OGRNForm()
    context = {'all_info': mould, 'form': phoneform}
    return render(request, 'landing/credit2.html', context)



def ogrn_info_eng(request):
    if request.method == "POST":
        inform = request.POST.get("name").rstrip()
        try:
            part = Econom_org('%s'%inform)
            mould = part.main()
            mould = mould[1:]
        except:
            exceptform = OGRNFormExcept_eng()
            mould = [{
            'инн': ' '
            }]
            context = {'all_info': mould, 'form': exceptform}
            return render(request, 'landing/eng/credit2.html', context)

    else:
        mould = [{
        'инн': ' '
        }]
    exceptform = OGRNFormExcept_eng()
    phoneform = OGRNForm_eng()
    context = {'all_info': mould, 'form': phoneform}
    return render(request, 'landing/eng/credit2.html', context)



def vk_bond(request):

    def get_friends(id_number):
        token = 'YOUR_TOKEN'
        response = requests.get('https://api.vk.com/method/users.get?v=5.89&access_token=%s&fields=photo_200_orig&user_id=%s'%(token,id_number)).json()
        return response


    if request.method == "POST":
        inform = request.POST.get("name").rstrip()
        inform = inform.replace('https://','')
        inform = inform.replace('http://','')
        index = inform.find('/')
        inform = inform[index+1:]
        print(inform)

        second = request.POST.get("age").rstrip()
        second = second.replace('https://','')
        second = second.replace('http://','')
        index = second.find('/')
        second = second[index+1:]
        print(second)
        try:
            a = VK_bond(inform,second)
            mould = a.main()
        except:
            exceptform = BondFormExcept()
            info_all = {
            'bond': ''
            }
            context = {'info':info_all, 'form': exceptform}
            return render(request, 'landing/bonds2.html',context)
        print(mould)
        massiv = []
        cep = ""
        flag = 0
        try:
            for otvet in mould:
                    first = get_friends(otvet)
                    print('#'*50)
                    print(otvet)
                    print('#'*50)
                    name_vk = first['response'][0]['first_name']+" "+first['response'][0]['last_name']
                    if 14<len(name_vk)<20:
                        otstup = 2
                    elif 10<len(name_vk)<=14:
                        otstup = 3
                    elif len(name_vk)<8:
                        otstup = 4
                    else:
                        otstup = 1
                    if otstup == 0:
                        otstup = 1
                    cep = "Цепочка найдена!"
                    massiv.append({
                    'otstupneed': otstup,
                    'link': first['response'][0]['photo_200_orig'],
                    'fio':  first['response'][0]['first_name']+" "+first['response'][0]['last_name'],
                    'linkvk' : 'https://vk.com/id%s'%first['response'][0]['id']
                    })
                    #cep = 'Цепочки найти не удалось. Оба пользователя ограничили доступ к странице'

        except:
            #cep = 'Цепочку найти не удалось. Оба пользователя ограничили доступ к странице'
            flag = 1
            pass
        if mould == []:
            cep = "Цепочка не обнаружена"
            cvet = 'alert alert-danger'
        elif mould == ['Block']:
            cep += 'Цепочка не обнаружена. Оба пользователя ограничили доступ к просмотру личной информации.'
            cvet = 'alert alert-danger'
        else:
            cep = "Цепочка обнаружена!"
            cvet = 'alert alert-success'
        info_all = {
        'connect': cep,
        'bond': massiv,
        'color': cvet,
        }
    else:
        info_all = {
        'bond': ''
        }
    phoneform = BondForm()
    context = {'info':info_all, 'form': phoneform}
    return render(request, 'landing/bonds2.html', context)

def vk_bond_eng(request):

    def get_friends(id_number):
        token = 'YOUR_TOKEN'
        response = requests.get('https://api.vk.com/method/users.get?v=5.89&access_token=%s&fields=photo_200_orig&user_id=%s'%(token,id_number)).json()
        return response


    if request.method == "POST":
        inform = request.POST.get("name").rstrip()
        inform = inform.replace('https://','')
        inform = inform.replace('http://','')
        index = inform.find('/')
        inform = inform[index+1:]
        print(inform)

        second = request.POST.get("age").rstrip()
        second = second.replace('https://','')
        second = second.replace('http://','')
        index = second.find('/')
        second = second[index+1:]
        print(second)
        try:
            a = VK_bond(inform,second)
            mould = a.main()
        except:
            exceptform = BondFormExcept_eng()
            info_all = {
            'bond': ''
            }
            context = {'info':info_all, 'form': exceptform}
            return render(request, 'landing/eng/bonds2.html',context)
        massiv = []
        cep = ""
        flag = 0
        try:
            for otvet in mould:
                    first = get_friends(otvet)
                    name_vk = first['response'][0]['first_name']+" "+first['response'][0]['last_name']
                    if 14<len(name_vk)<20:
                        otstup = 2
                    elif 10<len(name_vk)<=14:
                        otstup = 3
                    elif len(name_vk)<8:
                        otstup = 4
                    else:
                        otstup = 1
                    if otstup == 0:
                        otstup = 1
                    cep = "Chain detected!"
                    massiv.append({
                    'otstupneed': otstup,
                    'link': first['response'][0]['photo_200_orig'],
                    'fio':  first['response'][0]['first_name']+" "+first['response'][0]['last_name'],
                    'linkvk' : 'https://vk.com/id%s'%first['response'][0]['id']
                    })

        except:
            flag = 1
            pass
        if mould == []:
            cep = "Chain detected!"
            cvet = 'alert alert-danger'
        elif mould == ['Block']:
            cep += 'Сhain not found. Both users have restricted access to view personal information.'
            cvet = 'alert alert-danger'
        else:
            cep = "Chain detected!"
            cvet = 'alert alert-success'
        info_all = {
        'connect': cep,
        'bond': massiv,
        'color': cvet,
        }

    else:
        info_all = {
        'bond': ''
        }
    phoneform = BondForm_eng()
    context = {'info':info_all, 'form': phoneform}
    return render(request, 'landing/eng/bonds2.html', context)

def car_search(request):
    if request.method == "POST":
        inform = request.POST.get("formovka").rstrip()
        exceptform = CarFormExcept()

        if len(inform)>9 or len(inform)<8:
            info_all = {
            'bond': '',
            }
            context = {'info':info_all, 'form': exceptform}
            return render(request, 'landing/cars2.html', context)
            #return render(request, 'landing/cars.html', context)

        text = inform[0]+inform[4:6]
        print(text)
        if text.isalpha() == False:
            info_all = {
            'bond': '',
            }
            context = {'info':info_all, 'form': exceptform}
            return render(request, 'landing/cars2.html', context)
        cifri = inform[1:4]+inform[6:]
        print(cifri)
        if cifri.isdigit() == False:
            info_all = {
            'bond': '',
            }
            context = {'info':info_all, 'form': exceptform}
            return render(request, 'landing/cars2.html', context)


        dopusk = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х',
        'а','в','е','к','м','н','о','р','с','т','у','х','0',
        '1','2','3','4','5','6','7','8','9']
        stroka = ''
        for part in dopusk:
            stroka += part
        bookvy = inform[0]+inform[4:6]
        for bookva in inform:
            if stroka.find(bookva) == -1:
                info_all = {
                'bond': '',
                }
                context = {'info':info_all, 'form': exceptform}
                return render(request, 'landing/cars2.html', context)

        car = CarSearch(inform)
        mould = car.main()
        if mould == []:
            info_all = {
            'connect': 'Информация не обнаружена',
            'color' : 'alert alert-danger',
            'bond': {''},
            }
        else:
            info_all = {
            'connect': 'Информация найдена',
            'color' : 'alert alert-success',
            'bond': mould,
            }

    else:
        info_all = {
        'bond': '',
        }

    phoneform = CarForm()
    context = {'info':info_all, 'form': phoneform}
    return render(request, 'landing/cars2.html', context)

def nickname_search(request):
    s_for_nick = '''GitHub
GitLab
Lastfm
Pastebin
Reddit
Twitter
Yahoo
Instagram'''

    s_for_email = """Lastfm
Pastebin
Pinterest
Spotify
Twitter
GitHub
Instagram"""

    if request.method == "POST":
        nick = str(request.POST.get("formovka"))
        if len(nick) < 5:
            info_all = []
            exceptform = NicknameFormExcept()
            context = {'info': info_all, 'form': exceptform}
            return render(request, 'landing/nickname2.html', context)

        if nick.find('@') ==-1 and nick.isdigit() == True:
            info_all = []
            exceptform = NicknameFormExcept()
            context = {'info': info_all, 'form': exceptform}
            return render(request, 'landing/nickname2.html', context)

        d = {}
        if is_email(nick):
            for i in s_for_email.split():
                d[i] = "+"
        else:
            for i in s_for_nick.split():
                d[i] = "+"

        result = subprocess.run(['socialscan', '-a', nick], stdout=subprocess.PIPE)

        r = result.stdout.split()[3:-9]
        info_all = list(map(lambda x: x.decode("utf-8"), r))
    else:
        info_all = []
        d = {}

    for i in info_all:
        d[i] = "-"

    info_all = d
    phoneform = NicknameForm()

    context = {'info': info_all, 'form': phoneform}
    return render(request, 'landing/nickname2.html', context)


def nickname_search_eng(request):
    s_for_nick = '''GitHub
GitLab
Lastfm
Pastebin
Reddit
Twitter
Yahoo
Instagram'''

    s_for_email = """Lastfm
Pastebin
Pinterest
Spotify
Twitter
GitHub
Instagram"""

    if request.method == "POST":
        nick = str(request.POST.get("formovka"))
        if len(nick) < 5:
            info_all = []
            exceptform = NicknameFormExcept_eng()
            context = {'info': info_all, 'form': exceptform}
            return render(request, 'landing/eng/nickname2.html', context)

        if nick.find('@') ==-1 and nick.isdigit() == True:
            info_all = []
            exceptform = NicknameFormExcept_eng()
            context = {'info': info_all, 'form': exceptform}
            return render(request, 'landing/eng/nickname2.html', context)

        d = {}
        if is_email(nick):
            for i in s_for_email.split():
                d[i] = "+"
        else:
            for i in s_for_nick.split():
                d[i] = "+"

        result = subprocess.run(['socialscan', '-a', nick], stdout=subprocess.PIPE)

        r = result.stdout.split()[3:-9]
        info_all = list(map(lambda x: x.decode("utf-8"), r))
    else:
        info_all = []
        d = {}

    for i in info_all:
        d[i] = "-"

    info_all = d
    phoneform = NicknameForm_eng()

    context = {'info': info_all, 'form': phoneform}
    return render(request, 'landing/eng/nickname2.html', context)



def crypto(request):
    balances = {}
    if request.method == "POST":
        addresses = str(request.POST.get("addresses")).replace(" ", "").split(",")
        tokens = str(request.POST.get("tokens")).replace(" ", "").split(",")

        for token in tokens:
            result = Crypto(token, addresses).main()
            balances[result[0]] = str(result[1])

    else:
        chain = []

    form = CryptoForm()
    context = {'balances': balances, 'form': form}

    return render(request, 'landing/crypto2.html', context)

def crypto_eng(request):
    balances = {}
    if request.method == "POST":
        addresses = str(request.POST.get("addresses")).replace(" ", "").split(",")
        tokens = str(request.POST.get("tokens")).replace(" ", "").split(",")

        for token in tokens:
            result = Crypto(token, addresses).main()
            balances[result[0]] = str(result[1])

    else:
        chain = []

    form = CryptoForm_eng()
    context = {'balances': balances, 'form': form}

    return render(request, 'landing/eng/crypto2.html', context)

def biometry(request):
    def load_image(url):
        r = requests.get(url)
        b = b""
        for i in r:
            b = b + i
        return b

    if request.method == "POST":
        form = BiometryForm_url(request.POST, request.FILES)

        if form.is_valid():
            r = Biometry(load_image(request.POST.get("url"))).main()
            if r is None:
                link = ""
            else:
                link = r.json()["result"]["profiles"]
        else:
            link = ""
        url = str(request.POST.get("url"))
    else:
        link = ""
    form = BiometryForm_url()
    context = {'link_info': link, 'form': form}
    return render(request, 'landing/biometry2.html', context)

def biometry_url(request):
    def load_image(url):
        r = requests.get(url)
        b = b""
        for i in r:
            b = b + i
        return b

    if request.method == "POST":
        form = BiometryForm_url(request.POST, request.FILES)

        if form.is_valid():

            #print(len(load_image(request.POST.get("url"))))
            #print(len(request.FILES['photo'].read()))
            r = None
            try:
                r = Biometry(load_image(request.POST.get("url"))).main()
            except:
                r = None
            
            #r = Biometry(request.FILES['photo'].read()).main()
            if r is None:
                link = ""
            else:
                link = r.json()["result"]["profiles"]
        else:
            link = ""
        url = str(request.POST.get("url"))
    else:
        link = ""
    form = BiometryForm_url()
    context = {'link_info': link, 'form': form}
    print(context)
    #return render(request, 'landing/work.html')
    return render(request, 'landing/biometry2_url.html', context)



def biometry_local(request):
    def load_image(url):
        r = requests.get(url)
        b = b""
        for i in r:
            b = b + i
        return b

    if request.method == "POST":
        form = BiometryForm_photo(request.POST, request.FILES)

        if form.is_valid():
            #print(len(load_image(request.POST.get("url"))))
            #print(len(request.FILES['photo'].read()))
            #r = Biometry(load_image(request.POST.get("url"))).main()
            r = Biometry(request.FILES['photo'].read()).main()
            if r is None:
                link = ""
            else:
                link = r.json()["result"]["profiles"]
        else:
            link = ""
        #url = str(request.POST.get("url"))
    else:
        link = ""
    form = BiometryForm_photo()
    context = {'link_info': link, 'form': form}
    return render(request, 'landing/biometry2_local.html', context)


def biometry_test(request):

    return render(request, 'landing/test.html', locals())


def biometry_url_eng(request):
    def load_image(url):
        r = requests.get(url)
        b = b""
        for i in r:
            b = b + i
        return b

    if request.method == "POST":
        form = BiometryForm_url_eng(request.POST, request.FILES)

        if form.is_valid():

            #print(len(load_image(request.POST.get("url"))))
            #print(len(request.FILES['photo'].read()))
            r = None
            try:
                r = Biometry(load_image(request.POST.get("url"))).main()
            except:
                r = None
            #r = Biometry(request.FILES['photo'].read()).main()
            if r is None:
                link = ""
            else:
                link = r.json()["result"]["profiles"]
        else:
            link = ""
        url = str(request.POST.get("url"))
    else:
        link = ""
    form = BiometryForm_url_eng()
    context = {'link_info': link, 'form': form}
    print(context)
    #return render(request, 'landing/work.html')
    return render(request, 'landing/eng/biometry2_url.html', context)



def biometry_local_eng(request):
    def load_image(url):
        r = requests.get(url)
        b = b""
        for i in r:
            b = b + i
        return b

    if request.method == "POST":
        form = BiometryForm_photo_eng(request.POST, request.FILES)

        if form.is_valid():
            r = Biometry(request.FILES['photo'].read()).main()
            if r is None:
                link = ""
            else:
                link = r.json()["result"]["profiles"]
        else:
            link = ""
    else:
        link = ""
    form = BiometryForm_photo_eng()
    context = {'link_info': link, 'form': form}
    return render(request, 'landing/eng/biometry2_local.html', context)


def biometry_test_eng(request):

    return render(request, 'landing/eng/test.html', locals())




def txchain(request):
    if request.method == "POST":
        contract = str(request.POST.get("contract"))
        source = str(request.POST.get("source"))
        destination = str(request.POST.get("destination"))

        try:
            txchain = Txchain(contract, source, destination)
            chain = txchain.main()
            print(chain) # Debug printing here.
        except:
            print("1")
            chain = []
    else:
        chain = []

    form = TxchainForm()
    context = {'chain': chain, 'form': form}

    return render(request, 'landing/txchain.html', context)

def txchain_eng(request):
    if request.method == "POST":
        contract = str(request.POST.get("contract"))
        source = str(request.POST.get("source"))
        destination = str(request.POST.get("destination"))

        try:
            txchain = Txchain(contract, source, destination)
            chain = txchain.main()
            print(chain)
        except:
            print(2)
            chain = []
    else:
        chain = []

    form = TxchainForm_eng()
    context = {'chain': chain, 'form': form}

    return render(request, 'landing/eng/txchain.html', context)
