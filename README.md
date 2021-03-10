# Запустить проект:
-- python manage.py runserver (запустится на 8000 порту, либо вручную указать порт)
Также необходимо запустить chromedriver.exe из папки chromedriver, создастся сервис браузера, через который будет происходить обращение к веб-страницам.

Код показан в демонстрационных целях, многие модули не заработают из-за необходимости ключей авторизации.

# Информация о номере телефона (Phone number info)
Идея модуля: получение основных данных о номере телефона
Описание модуля: c каждым из нас бывало, что ему звонили с незнакомого номера и бросали трубку в надежде на то,
что человек перезвонит. Или звонили с предложением преумножить капитал на бинарных опционах. В такие моменты просто необходимо
быстро проверить, откуда был совершён звонок и является ли он одноразовым номером рекламщиков или же им пользуется человек,
в том числе регистрируя на него аккаунты в популярных сервисах. Именно для таких задач предусмотрен этот модуль.

Main idea: getting basic data about a phone number
Module description: It happened to each of us that they called him from an unfamiliar number and hung up in the hope that
that the person will call back. Or they called with a proposal to increase capital on binary options. At such moments, it’s just necessary
quickly check where the call was made from and whether it is a one-time number of advertisers or whether a person uses it
including registering accounts on it in popular services. It is for such tasks that this module is provided.

# Поиск цепочки между аккаунтами Вконтакте (Bonds between Vkontakte accounts)

Идея модуля: получение цепочки друзей соцсети "Вконтакте"
Описание модуля: представьте, что Вам необходимо как-то выйти на человека, может быть списаться с ним или просто понять круг его интересов,
но кроме его аккаунта социальной сети Вконтакте у Вас больше ничего нет. Данный модуль предоставляет возможность
построения искомой цепочки.

Main idea: receiving a chain of friends of the messanger "Vkontakte"
Module description: Imagine that you need to somehow reach a person, maybe write to him or just understand the circle of his interests, but besides his account VKontakte social network you have nothing more. This module provides an opportunity building the desired chain.

# Информация о домене (Domain info)
Идея модуля: получение данных о доменных именах и IP-адресах
Описание модуля: "Я тебя по IP вычислю..." Знакомо, не правда ли? Этим модулем наша команда хотела воплотить эту фразу в жизнь. Прежде всего
эта страница позиционируется как комплексный поисковик в мире IoT. Вам достаточно написать IP-адрес или скопировать url-адрес и вставить в поисковую
строку —-> нажать "Узнать", затем сайт в автоматическом режиме соберет информацию и отобразит еена экране. Стоит отметить, что при отсутствии данных о городе провайдера, на карте отобразится столица страны, где расположен провайдер.

Main idea: receiving data about domain names and IP addresses
Module description: "I'll figure you out by IP ..." It’s familiar, isn't it? With this module, our team wanted to bring this phrase to life. Primarily
This page is positioned as a comprehensive search engine in the world of IoT. You just need to write the IP address or copy the url and paste it into the search the line —-> click "Learn", then the site will automatically collect information and display it on the screen. It is worth noting that in the absence of data on the provider's city, the capital of the country where the provider is located will be displayed on the map.

# Биометрия (Biometry)

Идея модуля: поиск аккаунта в социальной сети по фото.
Описание модуля: Иногда возникает необходимость найти информацию о человеке, либо выйти с ним на связь, имея только его фотографию.
В таких случаях необходимо иметь средство для поиска данных о человеке, изображённом на фотографии - именно такой сервис предоставляет данный модуль:
загрузив фото или передав ссылку на него вы получаете до 20 аккаунтов в социальных сетях с людьми, похожими на предоставленную фотографию.

Nodule idea: social network account searching by profile photo.
Module description: Sometimes yu need to find information about human or contact with him using only his photo.
In these cases it takes service for data searching about human by his photo and this service provided by this module:
When you download photo or enter link to the photo you get 20 social network accounts with humans with profile photo like you search.

# Информация о компании (Info about company)

Идея модуля: получение данных об организации
Описание модуля: данный модуль реализует функционал поиска основных юридических данных об организации из открытых источников. Он может быть полезен для получения первичной ифнормации о юридическом лице, а так же о его руководителе или юридическом адресе.

Main idea: receiving data about the organization
Module description: this module implements the functionality of the search for basic legal data About an organization from open sources. It can be useful for getting primary information about a legal entity, as well as his manager or legal address.

# Информация о никнейме (Info about nickname)

Идея модуля: Получение данных об использовании никнеймов и почтовых адресов на популярных сайтах.
Описание модуля: Данный модуль предоставляет информацию о том используется ли введённое имя или никнейм на популярных сайтах.
Модуль может быть полезен, например, при выборе нового никнейма в сети. Важно отметить, что если происходит поиск по никам, то он не должен состоять только из цифр

Main idea: obtaining data on the use of nicknames and mailing addresses on popular sites.
Module description: this module provides information on whether the entered name or nickname is used on popular sites.
The module can be useful, for example, when choosing a new nickname on the network. It is important to note that if there is a search by nicknames, then it should not consist only of numbers

# Txchain

Идея модуля: поиск потенциального перемещения криптовалюты между двумя аккаунтами.
Описание модуля: Порой необходимо выяснить переводилась ли криптовалюта между двумя пользователями, но выяснить это не так просто из-за неконтролируемого и неограниченного создания кошельков пользователями, а также отсутствия связи между пользователем и его кошельком. Данный сервис позволяет проследить перевод криптовалюты несмотря на множество промежуточных аккаунтов благодаря рекурсивному алгоритму поиска в ширину. В результате пользователь получает поетнциальную цепочку переводов между заданными кошельками.

Module idea: searching of potential cryptocurrency transfer chain between two accounts.
Module description: Sometimes it's needed to know posibility of transfer between two cryptocurrency users, but it's not to find out that, beacuse in crypti ccurrrency users can create new account unlimitable and unlinkable betwenn user and his account. This module allows to trace cryptocurrency transfer despite a lot of intermediate accounts. It's possible thanks recursive BFS. Result of work is potential cryptocurrency transfer chain between entered wallets.