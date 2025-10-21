from django.views import generic
from .models import Post # Postモデルをimport
from django.urls import reverse_lazy
from .forms import PostCreateForm 

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'handson_app/index.html'

class PostListView(generic.ListView): # generic の ListViewクラスを継承
    model = Post # 一覧表示させたいモデルを呼び出し
    template_name = 'handson_app/post_list.html'

class PostCreateView(generic.CreateView): # 追加
    model = Post # 作成したい model を指定
    form_class = PostCreateForm # 作成した form クラスを指定
    success_url = reverse_lazy('handson_app:post_list')
    template_name = 'handson_app/post_create.html'


