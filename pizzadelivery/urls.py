from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import shop.views
import cart.views
import orders.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/<int:id>/', cart.views.remove_from_cart, name='remove_from_cart'),
    path('cart/<slug:slug>/', cart.views.update_cart, name='update_cart'),
    path('cart/', cart.views.view, name='cart'),
    path('checkout/', orders.views.checkout, name='checkout'),
    path('orders/', orders.views.orders, name='user_orders'),
    path('', shop.views.home, name='home'),
    path('<slug:slug>/', shop.views.detail, name='detail'),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
