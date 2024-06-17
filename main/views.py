from django.contrib.auth import authenticate, login
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, DetailView, ListView
from hitcount.views import HitCountDetailView

from main.models import Post, Comment, Feedback, Faq, Testimonial, User

from django.shortcuts import redirect

def redirect_to_home(request):
    return redirect(reverse('index'))


class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-date')[:3]
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')
        Feedback.objects.create(name=name, email=email, phone=phone, message=comments)
        return redirect(reverse('index'))


class ContactPageView(TemplateView):
    '''указание html который будет показан'''
    template_name = 'contact.html'


    def post(self, request, *args, **kwargs):
        '''Получение с формы в контактах'''
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')
        Feedback.objects.create(name=name, email=email, phone=phone, message=comments)
        return redirect_to_home(request)



class PostDetailView(HitCountDetailView):
    '''Детальная страница новостей'''
    template_name = 'single-post.html'
    pk_url_kwarg = 'id'
    model = Post
    count_hit = True

    def post(self, request, id):
        '''Получение комментов'''
        msg = request.POST.get('msg')
        Comment.objects.create(user=request.user, content=msg, post_id=id)
        return redirect(reverse('post-detail', kwargs={"id":id}))


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        '''передача данных в html отзывы'''
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.all()
        return context


class NewsListPageView(ListView):
    template_name = 'two-column.html'
    model = Post
    context_object_name = 'post_list'


class FaqPageView(ListView):
    template_name = 'services.html'
    queryset = Faq.objects.order_by('id')
    context_object_name = 'faq_list'


class LoginPageView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect_to_home(request)

        return render(request, 'login.html', {"error": True})

class RegisterPageView(TemplateView):
    template_name = 'register.html'
    def post(self, request, *args, **kwargs):
        username = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            user = User.objects.create_user(username=username, email=username, password=password)
            login(request, user)
            return redirect_to_home(request)

        return render(request, 'register.html', {"error": True})
