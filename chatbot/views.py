from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from chatterbot.trainers import ChatterBotCorpusTrainer

from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
	
)
#chatbot.train(
#    "chatterbot.corpus.english.greetings",
#	"chatterbot.corpus.english.conversations"
#)

# Train based on the english corpus

#Already trained and it's supposed to be persistent
#chatbot.train("chatterbot.corpus.english")

@csrf_exempt
def get_response(request):
	response = {'status': None}

	if request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))
		message = data['message']

		chat_response = chatbot.get_response(message).text
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
		response['status'] = 'ok'

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)


def home(request, template_name="home.html"):
	context = {'title': 'Chatbot Version 1.0'}
	return render(None, template_name, context)
