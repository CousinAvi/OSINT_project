from django.conf.urls import url
from landing import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.landing, name='landing'),
    path('main', views.rus, name='rus'),
    path('domen', views.detail, name='domen'),
    path('domen_eng', views.detail_eng, name='domen_eng'),
    path('landing', views.landing, name=''),
    path('number', views.number_info, name='number'),
    path('number_eng', views.number_info_eng, name='number_eng'),
    path('org_info', views.ogrn_info, name='org_info'),
    path('org_info_eng', views.ogrn_info_eng, name='org_info_eng'),
    path('bonds', views.vk_bond, name='bonds'),
    path('bonds_eng', views.vk_bond_eng, name='bonds_eng'),
    path('car_search', views.car_search, name='car_search'),
    path('nickname_search', views.nickname_search, name='nickname_search'),
    path('nickname_search_eng', views.nickname_search_eng, name='nickname_search_eng'),
    path('inform', views.inform, name='inform'),
    path('inform_eng', views.inform_eng, name='inform_eng'),
    path('team', views.team, name='team'),
    path('team_eng', views.team_eng, name='team_eng'),
    path('contact', views.post_new, name='contact'),
    path('post_edit', views.post_new, name='post_edit'),
    path('post_edit_eng', views.post_new_eng, name='post_edit_eng'),
    path('crypto', views.crypto, name='crypto'),
    path('crypto_eng', views.crypto_eng, name='crypto_eng'),
    path('txchain', views.txchain, name='txchain'),
    path('txchain_eng', views.txchain_eng, name='txchain_eng'),
    path('biometry', views.biometry, name='biometry'),
    path('biometry_url', views.biometry_url, name='biometry_url'),
    path('biometry_local', views.biometry_local, name='biometry_local'),
    path('biometry_test', views.biometry_test, name='biometry_test'),
    path('biometry_test_eng', views.biometry_test_eng, name='biometry_test_eng'),
    path('biometry_url_eng', views.biometry_url_eng, name='biometry_url_eng'),
    path('biometry_local_eng', views.biometry_local_eng, name='biometry_local_eng'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
