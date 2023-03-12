from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django_email_verification import send_email
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Обо мне', 'url_name': 'about'},
    {'title': 'Портфолио', 'url_name': 'portfolio'},
    {'title': 'Цены', 'url_name': 'price'},
    {'title': 'Контакты', 'url_name': 'contacts'},
    {'title': 'Блог', 'url_name': 'blog'},
]

class HomePage(ListView):
    queryset = FeedbackModel.objects.order_by('-id')
    template_name = 'mainapp/home.html'
    context_object_name = 'posts'

    @staticmethod
    def all_settings():
        return BlogModel.objects.order_by('-time_create')[:3]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Портфолио для фотографа'
        return context


class AboutPage(TemplateView):
    template_name = 'mainapp/about.html'
    extra_context = {'menu': menu, 'title': 'Обо мне'}


class PortfolioPage(ListView):
    model = PortfolioModel
    template_name = 'mainapp/portfolio.html'
    context_object_name = 'port'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Моё портфолио'
        return context


class PricePage(ListView):
    model = PriceModel
    template_name = 'mainapp/price.html'
    context_object_name = 'cards'
    extra_context = {'menu': menu, 'title': 'Мои цены'}

class ContactsPage(FormView):
    form_class = ContactsForm
    template_name = 'mainapp/contacts.html'
    extra_context = {'menu': menu, 'title': 'Мои контакты'}
    success_url = reverse_lazy('contacts')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            data = {
                'name': form.cleaned_data.get('name'),
                'email': form.cleaned_data.get('email'),
                'msg': form.cleaned_data.get('msg')
            }
            html_body = render_to_string('mainapp/appoinment_email.html', data)
            msg = EmailMultiAlternatives(subject="Письмо с сайта", to=['roman197t@gmail.com'])
            msg.attach_alternative(html_body, 'text/html')
            msg.send()
            return self.form_valid(form)
        return self.form_invalid(form)


class BlogPage(ListView):
    model = BlogModel
    template_name = 'mainapp/blog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Мой блог'
        context['cat_selected'] = 0
        context['object_list'] = BlogModel.objects.all()
        paginator = Paginator(context['object_list'], 3)
        page = self.request.GET.get('page')
        try:
            context['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            context['object_list'] = paginator.page(paginator.num_page)

        return context

class BlogCategory(ListView):
    model = BlogModel
    template_name = 'mainapp/blog.html'
    context_object_name = 'posts'
    allow_empty = False
    def get_queryset(self):
        return BlogModel.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Раздел - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context


class PortfolioPost(DetailView):
    model = PortfolioModel
    template_name = 'mainapp/portfolio-category.html'
    slug_url_kwarg = 'portf_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Портфолио'
        return context


class ShowPost(FormMixin, DetailView):
    model = BlogModel
    form_class = CommentForm
    template_name = 'mainapp/blog_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_success_url(self, **kwargs):
        return reverse_lazy('post', kwargs={'post_slug': self.get_object().slug})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Пост из блога'
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class LoginUser(LoginView):
    form_class = AuthUserForm
    template_name = 'mainapp/login_page.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, 'А может ты не зарегистрирован?')

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def get_success_url(self, **kwargs):
        return self.success_url


@csrf_exempt
def sendEmail(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    user = get_user_model().objects.create(username=username, password=password, email=email)
    user.is_active = False
    send_email(user)
    return render(request, 'mainapp/confirm_template.html')


class RegisterUser(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'mainapp/register_page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        aut_user = authenticate(username=username, email=email, password=password)
        login(self.request, aut_user)
        return form_valid


class LogoutUser(LogoutView):
    next_page = reverse_lazy('home')


def pageNotFound(request, exception):
    context = {'title': '404'}
    return render(request, 'mainapp/page404.html', context=context)

