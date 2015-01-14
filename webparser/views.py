from django.shortcuts import render
from grab import Grab
from grab.tools.work import make_work


def index(request):
    return render(request, 'webparser/index.html')

def parse(request):
    context = []
    post = request.POST['url']
    post_urls = post.splitlines()
    urls = list(map(str.strip, post_urls))
    for result in make_work(worker, urls, limit=5):
        context.append(result)
    return render(request, 'webparser/index.html', {'context' : context, 'post' : post})

def worker(url):
    g = Grab()
    g.go(url)
    code = g.response.code
    title = g.doc.select('//title').text(default=None)
    description = g.doc.select('//meta[@name="description"]/@content').text(default=None)
    keywords = g.doc.select('//meta[@name="keywords"]/@content').text(default=None)
    h1 = g.doc.select('//h1').text(default=None)
    result = {'url' : url, 'title' : title, 'description' : description, 'keywords' : keywords, 'h1' : h1, 'code' : code}
    return result
