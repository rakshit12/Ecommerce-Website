from django.urls import path
from . import views
urlpatterns = [
    path("", views.index ,name='shopHome'),
    path("about/", views.about ,name='about'),
    path("products/<int:myid>", views.productView , name='productviews'),
    path("contact/", views.contact ,name='contact'),
    path("search/", views.search ,name='search'),
    path("tracker/", views.tracker ,name='tracker'),
    path("checkout/", views.checkout ,name='checkout'),
     path("handlerequest/", views.handlerequest, name="HandleRequest"),
     path('signup/',views.signupuser, name='signupuser'),
    path('logout/',views.logoutuser, name='logoutuser'),
    path('login/',views.loginuser, name='loginuser'),
]
