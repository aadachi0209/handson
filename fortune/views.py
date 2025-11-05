from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string
from . import fortune as fortune_module
 
 
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
    # テンプレートからHTMLを生成するときに参照されるコンテキスト
    context = {
        'fortune': fortune
    }

    # コンテキストをもとにテンプレートからHTML文字列を生成した結果をHTTPレスポンスのボディとする
    return HttpResponse(render_to_string('fortune/fortune.html', context=context))
