from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string
from . import fortune as fortune_module
from .models import Uranai   
 
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(render_to_string('fortune/index.html'))

def fortune(request: HttpRequest) -> HttpResponse:
    """
    おみくじ結果画面表示

    :param request: HTTPリクエスト
    :return: おみくじ結果画面をボディに持つHTTPレスポンス
    """
    # おみくじの結果を関数より取得
    fortune = fortune_module.tell_fortune()

    results = Uranai.objects.raw('select * from fortune_uranai')
    sum = len(list(results))
    results = Uranai.objects.raw('select * from fortune_uranai where daikichi=1')
    daikichi = len(list(results))
    results = Uranai.objects.raw('select * from fortune_uranai where chukichi=1')
    chukichi = len(list(results))
    results = Uranai.objects.raw('select * from fortune_uranai where shokichi=1')
    shokichi = len(list(results))

    daikichi_per = round(100*(daikichi / sum),1)
    chukichi_per = round(100*(chukichi / sum),1)
    shokichi_per = round(100*(shokichi / sum),1)
    
    # テンプレートからHTMLを生成するときに参照されるコンテキスト
    context = {
        'fortune': fortune,
        'daikichi_per': daikichi_per,
        'chukichi_per': chukichi_per,
        'shokichi_per': shokichi_per,
    }

    # コンテキストをもとにテンプレートからHTML文字列を生成した結果をHTTPレスポンスのボディとする
    return HttpResponse(render_to_string('fortune/fortune.html', context=context))
