import json
import urllib.request
from random import random
from decouple import config
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic as views


@method_decorator(login_required, name='dispatch')
class HomeView(views.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        word = str(self.request.GET.get('city'))

        source_dict = urllib.request.urlopen('https://api.dictionaryapi.dev/api/v2/entries/en/' + word).read()
        source_pic = urllib.request.urlopen('https://pixabay.com/api/?key=' + config('API_KEY_PIC') + '&q=' + (word.replace(" ", "%20"))).read()

        data_dict = json.loads(source_dict)
        data_pic = json.loads(source_pic)

        context['word'] = word
        context['phonetics_text'] = str(data_dict['phonetics']['text'])
        context['phonetics_audio'] = str(data_dict['phonetics']['audio'])
        context['origin'] = str(data_dict['origin'])

        for i in range(3):
            speech = str(data_dict['meanings'][i]['partOfSpeech'])
            context['partOfSpeech' + speech] = str(data_dict['meanings'][i]['partOfSpeech'])
            context['definition' + speech] = str(data_dict['meanings'][i]['definitions']['definition'])
            context['example' + speech] = str(data_dict['meanings'][i]['definitions']['example'])
            context['synonyms' + speech] = str(data_dict['meanings'][i]['definitions']['synonyms'])
            context['antonyms' + speech] = str(data_dict['meanings'][i]['definitions']['antonyms'])

        context['picture'] = data_pic['hits'][random.randint(0, len(data_pic['hits']))]['webformatURL']

        return context




