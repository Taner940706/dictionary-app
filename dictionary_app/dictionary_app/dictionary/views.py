import urllib.request
import urllib.error
import json
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from decouple import config

@method_decorator(login_required, name='dispatch')
class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        part_of_speech = []
        definition = []
        synonyms = []
        antonyms = []

        context = super().get_context_data(**kwargs)
        word = str(self.request.GET.get('word'))

        source_dict = None  # Initialize source_dict with a default value
        data_dict = None    # Initialize data_dict with a default value
        data_pic = None     # Initialize data_pic with a default value

        try:
            source_dict = urllib.request.urlopen('https://api.dictionaryapi.dev/api/v2/entries/en/' + (word.replace(" ", "%20"))).read()
            data_dict = json.loads(source_dict)
        except urllib.error.HTTPError as err:
            pass

        try:
            source_pic = urllib.request.urlopen('https://pixabay.com/api/?key=' + config('API_KEY_PIC') + '&q=' + (word.replace(" ", "%20"))).read()
            data_pic = json.loads(source_pic)
        except urllib.error.HTTPError as err:
            print(f'A HTTPError was thrown: {err.code} {err.reason}')

        if data_dict is not None:
            context['word'] = word

            if 'phonetics' in data_dict[0] and data_dict[0]['phonetics']:
                context['phonetics_text'] = str(data_dict[0]['phonetics'][-1]['text'])
                context['phonetics_audio'] = str(data_dict[0]['phonetics'][0]['audio'])
                context['source'] = str(data_dict[0]['phonetics'][0]['sourceUrl'])

            for i in range(len(data_dict[0]['meanings'])):
                part_of_speech.append(str(data_dict[0]['meanings'][i]['partOfSpeech']))
                definition.append(str(data_dict[0]['meanings'][i]['definitions'][0]['definition']))
                synonyms.append(str(data_dict[0]['meanings'][i]['definitions'][0]['synonyms']))
                antonyms.append(str(data_dict[0]['meanings'][i]['definitions'][0]['antonyms']))

            context['part_of_speech'] = part_of_speech
            context['definition'] = definition
            context['synonyms'] = synonyms
            context['antonyms'] = antonyms

            if data_pic is not None and 'hits' in data_pic and data_pic['hits']:
                context['picture'] = data_pic['hits'][0]['webformatURL']

            context['meanings'] = dict(enumerate(zip(context['part_of_speech'], context['definition'], context['synonyms'], context['antonyms'])))

        return context


class View404(generic.TemplateView):
    template_name = '404.html'  # Replace with the actual template name for your 404 page

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['request_path'] = request.path
        return self.render_to_response(context)


class View500(generic.TemplateView):
    template_name = '500.html'  # Replace with the actual template name for your 500 page

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Add any additional context data you need
        return self.render_to_response(context)