import json
import urllib.request

from django.contrib.auth.decorators import login_required
from django.views import generic as views


@login_required
class Home(views.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        word = str(self.request.GET.get('city'))
        source = urllib.request.urlopen('https://api.dictionaryapi.dev/api/v2/entries/en/' + word).read()
        data = json.loads(source)

        context['word'] = word
        context['phonetics_text'] = str(data['phonetics']['text'])
        context['phonetics_audio'] = str(data['phonetics']['audio'])
        context['origin'] = str(data['origin'])

        for i in range(3):
            speech = str(data['meanings'][i]['partOfSpeech'])
            context['partOfSpeech' + speech] = str(data['meanings'][i]['partOfSpeech'])
            context['definition' + speech] = str(data['meanings'][i]['definitions']['definition'])
            context['example' + speech] = str(data['meanings'][i]['definitions']['example'])
            context['synonyms' + speech] = str(data['meanings'][i]['definitions']['synonyms'])
            context['antonyms' + speech] = str(data['meanings'][i]['definitions']['antonyms'])

        return context




