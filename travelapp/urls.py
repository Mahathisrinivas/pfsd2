from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from .forms import UserLoginForm
from django.conf.urls.static import static
from django.urls import path
from .views import logout
from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView, name="home"),
    path('payment/',views.payment,name="payment"),
    path('feedback/', views.feedback, name="feedback"),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',views.logout,name="logout.html"),
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
    path('logout/', views.logout_view, name='logout'),
    path('package/',views.PackageView,name="package"),
    path('flights/',views.FlightView,name="flights"),
    path('hotels/',views.HotelView,name="hotels"),
    path('places/',views.PlacesView,name="places"),
    path('bookflight/<str:flight_num>/<str:date>',views.Flightbook,name="bookflight"),
    path('userflight/<str:flight_num>/<str:date>/<int:seat>',views.FlightSubmit,name='userflight'),
    path('bookhotel/<str:hotel>/<str:date>',views.Hotelbook,name="bookflight"),
    path('userhotel/<str:hotel>/<str:date>/<int:room>',views.HotelSubmit,name='userflight'),
    path('bookpackage/<str:source>/<str:city>/<str:date>',views.PackageBook,name="bookpackage"),
    path('userpackage/<str:flight>/<str:hotel>/<str:date>/<int:room>/<int:seat>',views.PackageSubmit,name='userpackage'),
    path('accounts/profile/',views.Dashboard,name='dashboard'),
    path('cancelflight/<str:flight>/<str:date>/<int:seat>',views.CancelFlight,name='CancelFlight'),
    path('concanflight/<str:flight>/<str:date>/<int:seat>',views.ConfirmCancelFlight,name='ConfirmCancelFlight'),
    path('cancelhotel/<str:hotel>/<str:date>/<int:room>',views.CancelHotel,name='CancelHotel'),
    path('concanhotel/<str:hotel>/<str:date>/<int:room>',views.ConfirmCancelHotel,name='ConfirmCancelHotel'),
    path('cancelpackage/<str:flight>/<int:seat>/<str:hotel>/<str:date>/<int:room>',views.CancelPackage,name='CancelPackage'),
    path('concanpackage/<str:flight>/<int:seat>/<str:hotel>/<str:date>/<int:room>',views.ConfirmCancelPackage,name='ConfirmCancelPackage'),
    path('book/',views.book,name="booking"),
    path('dashboard/',views.Dashboard,name="dash"),
    path('maps',views.Maps,name='maps'),
    path('booking/', views.booking_view, name='booking'),
    ]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)