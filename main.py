# importing requests package
import requests
import pyttsx3
engine = pyttsx3.init('sapi5')



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def NewsFromBBC():

	# BBC news api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "4dbc17e007ab436fb66416009dfb59a8"
	}
	main_url = " https://newsapi.org/v1/articles"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()

	# getting all articles in a string article
	article = open_bbc_page["articles"]

	# empty list which will
	# contain all trending news
	results = []

	for ar in article:
		results.append(ar["title"])
	speak('todays news is ')
	for i in range(len(results)):

		# printing all trending news
		speech = i + 1, results[i]
		
		speak(speech)
		print(i + 1, results[i])


	speak('this is todays news')

# Driver Code
if __name__ == '__main__':

	# function call
	NewsFromBBC()
