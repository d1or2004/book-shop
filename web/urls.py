from django.urls import path
from .views import IndexView, AboutView, BlogView, BlogDetailView, BlogLeftView, BlogNoView, CartView, \
    ContactView, CheckoutView, ErrorView, FAQView, HomeBoxView, HomeTwoView, PortfolioView, AccountView, \
    PortfolioThreeView, PortfolioDetailView, ShopGridView, ShopLeftView, ShopNoView, ShopRightView, \
    ShopListView, SingleProductView, TeamView, WishlistView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-detail/', BlogDetailView.as_view(), name='blog-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('error/', ErrorView.as_view(), name='error'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('account/', AccountView.as_view(), name='account'),
    path('shop-list/', ShopListView.as_view(), name='shop-list'),
    path('single-product/', SingleProductView.as_view(), name='single-product'),
    path('team/', TeamView.as_view(), name='team'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
]
