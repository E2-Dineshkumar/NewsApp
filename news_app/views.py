from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url="https://newsapi.org/v2/everything?q=Crypto&from=2022-09-19&sortBy=popularity&apiKey=339cca699e334da3939de4c86354a44d"

    crypto_news=requests.get(url).json()
    
    a=crypto_news['articles']
    
    desc=[]
    title=[]
    img=[]
    for i in range(len(a)):
        f=a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        
    mylist=zip(title,desc,img)
    context={'mylist':mylist}
    
    return render(request,'index.html',context)