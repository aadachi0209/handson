from django.views import generic

from .models import Post # Postモデルをimport
from django.urls import reverse_lazy
from .forms import PostCreateForm 
from .forms import SignUpForm
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'handson_app/index.html'

class PostListView(LoginRequiredMixin, generic.ListView): # generic の ListViewクラスを継承
    model = Post # 一覧表示させたいモデルを呼び出し
    template_name = 'handson_app/post_list.html'
    
    login_url = reverse_lazy('handson_app:login')    

class PostCreateView(LoginRequiredMixin, generic.CreateView): # 追加
    model = Post # 作成したい model を指定
    form_class = PostCreateForm # 作成した form クラスを指定
    success_url = reverse_lazy('handson_app:post_list')
    template_name = 'handson_app/post_create.html'

    login_url = reverse_lazy('handson_app:login')

class PostDetailView(LoginRequiredMixin, generic.DetailView): # 追加
    model = Post
    template_name = 'handson_app/post_detail.html'

    login_url = reverse_lazy('handson_app:login')

class PostUpdateView(LoginRequiredMixin, generic.UpdateView): # 追加
    model = Post
    form_class = PostCreateForm 
    success_url = reverse_lazy('handson_app:post_list')
    template_name = 'handson_app/post_create.html'

    login_url = reverse_lazy('handson_app:login')

class PostDeleteView(LoginRequiredMixin, generic.DeleteView): # 追加
    model = Post
    success_url = reverse_lazy('handson_app:post_list')
    template_name = 'handson_app/post_confirm_delete.html'

    login_url = reverse_lazy('handson_app:login')

class PostLoginView(views.LoginView):
    template_name = 'handson_app/login.html'

    def get_success_url(self):
        return reverse_lazy('handson_app:post_list')

class PostLogoutView(views.LogoutView):
    def get_success_url(self):
        return reverse_lazy('handson_app:login')

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "handson_app/signup.html"
    success_url = reverse_lazy("handson_app:login")
