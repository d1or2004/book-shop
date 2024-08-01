from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'web/index.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'web/about.html')


class BlogView(View):
    def get(self, request):
        return render(request, 'web/blog.html')


class BlogDetailView(View):
    def get(self, request):
        return render(request, 'web/blog-details.html')


class BlogLeftView(View):
    def get(self, request):
        return render(request, 'web/blog-left-sidebar.html')


class BlogNoView(View):
    def get(self, request):
        return render(request, 'web/blog-no-sidebar.html')


class CartView(View):
    def get(self, request):
        return render(request, 'web/cart.html')


class CheckoutView(View):
    def get(self, request):
        return render(request, 'web/checkout.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'web/contact.html')


class ErrorView(View):
    def get(self, request):
        return render(request, 'web/error404.html')


class FAQView(View):
    def get(self, request):
        return render(request, 'web/faq.html')


class HomeTwoView(View):
    def get(self, request):
        return render(request, 'web/index-2.html')


class HomeBoxView(View):
    def get(self, request):
        return render(request, 'web/index-box.html')


class AccountView(View):
    def get(self, request):
        return render(request, 'web/my-account.html')


class PortfolioView(View):
    def get(self, request):
        return render(request, 'web/portfolio.html')


class PortfolioDetailView(View):
    def get(self, request):
        return render(request, 'web/portfolio-details.html')


class PortfolioThreeView(View):
    def get(self, request):
        return render(request, 'web/portfolio-three-column.html')


class ShopGridView(View):
    def get(self, request):
        return render(request, 'web/shop-grid.html')


class ShopLeftView(View):
    def get(self, request):
        return render(request, 'web/shop-left-sidebar.html')


class ShopListView(View):
    def get(self, request):
        return render(request, 'web/shop-list.html')


class ShopNoView(View):
    def get(self, request):
        return render(request, 'web/shop-no-sidebar.html')


class ShopRightView(View):
    def get(self, request):
        return render(request, 'web/shop-right-sidebar.html')


class SingleProductView(View):
    def get(self, request):
        return render(request, 'web/single-product.html')


class TeamView(View):
    def get(self, request):
        return render(request, 'web/team.html')


class WishlistView(View):
    def get(self, request):
        return render(request, 'web/wishlist.html')
