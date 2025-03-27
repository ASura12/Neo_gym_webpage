from django.urls import path
from . import views
urlpatterns = [
    path('test',views.test),
    
    path('home2',views.home2),
    path('about1',views.about1),
    path('home3',views.home3),    
    path('index',views.index),    
    path('whyus',views.whyus),    
    path('trainer',views.trainer),
    path('add',views.add),  
    path('addcode',views.addcode),
    path('calculator',views.calculator),
    path('cal',views.cal),
    path('contact',views.contact),
    path('insert',views.insert),
    path('ins',views.ins),
    path('reg',views.reg),
    path('enter',views.enter),  
    path('contact',views.contact), 
    path('show',views.show),
    path('del/<int:id>',views.dele),
    path('edit/<int:id>',views.edit),
    path('edcode/<int:id>',views.edcode),
    path('login',views.login),
    path('log2',views.log2),
    path('logout',views.logout),
]