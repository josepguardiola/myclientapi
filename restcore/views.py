from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.conf import settings

import requests


from restcore.forms import SubmitEmbed
from restcore.serializers import EmbedSerializer

def save_embed(request):

    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            r = requests.get('http://api.embed.ly/1/oembed?key='+settings.EMBEDED_KEY +'&url=' + url)
            json = r.json()
            serializer = EmbedSerializer(data=json)
            if serializer.is_valid():
                embed = serializer.save()
                return render(request, 'embeds.html', {'embed': embed})
    else:
        form = SubmitEmbed()

    return render(request, 'index.html', {'form': form})

        
    
       
            
        
                
    
