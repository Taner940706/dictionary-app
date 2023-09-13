import json
import urllib.request
from http.client import HTTPException
from urllib.error import URLError

from decouple import config
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import generic as views
from urllib3.exceptions import HTTPError


@method_decorator(login_required, name='dispatch')
class HomeView(views.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        part_of_speech = []
        definiton = []
        synonyms = []
        antonyms = []

        context = super().get_context_data(**kwargs)
        word = str(self.request.GET.get('word'))
        source_dict = urllib.request.urlopen(
            'https://api.dictionaryapi.dev/api/v2/entries/en/' + (word.replace(" ", "%20"))).read()

        source_pic = urllib.request.urlopen(
            'https://pixabay.com/api/?key=' + config('API_KEY_PIC') + '&q=' + (word.replace(" ", "%20"))).read()

        data_dict = json.loads(source_dict)
        data_pic = json.loads(source_pic)

        context['word'] = word

        try:
            context['phonetics_text'] = str(data_dict[0]['phonetics'][-1]['text'])
        except KeyError as ke:
            pass
        except IndexError as ind:
            pass

        try:
            context['phonetics_audio'] = str(data_dict[0]['phonetics'][0]['audio'])
        except KeyError as ke:
            pass
        except IndexError as ind:
            pass

        try:
            context['source'] = str(data_dict[0]['phonetics'][0]['sourceUrl'])
        except KeyError as ke:
            pass
        except IndexError as ind:
            pass

        for i in range(len(data_dict[0]['meanings'])):
            part_of_speech.append(str(data_dict[0]['meanings'][i]['partOfSpeech']))
            definiton.append(str(data_dict[0]['meanings'][i]['definitions'][0]['definition']))
            synonyms.append(str(data_dict[0]['meanings'][i]['definitions'][0]['synonyms']))
            antonyms.append(str(data_dict[0]['meanings'][i]['definitions'][0]['antonyms']))

        context['part_of_speech'] = part_of_speech
        context['definiton'] = definiton
        context['synonyms'] = synonyms
        context['antonyms'] = antonyms

        try:
            context['picture'] = data_pic['hits'][0]['webformatURL']
        except IndexError as ind:
            pass

        context['meanings'] = dict(enumerate(zip(context['part_of_speech'],context['definiton'],context['synonyms'], context['antonyms'])))


        return context


class View404(views.TemplateView):
    template_name = '404.html'


class View500(views.TemplateView):
    template_name = '500.html'

