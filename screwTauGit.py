from fbchat import Client
from fbchat.models import *
import time

# while True:
# 	client.send(Message(text='Also! Fuck the Tau!'), thread_id='1684891288218201', thread_type=ThreadType.GROUP)
# 	time.sleep(60)

def inMessage(str1, str2):
	str2lower = str2.lower()
	str1lower = str1.lower()
	return str1lower in str2lower


class GuardsmanClient(Client):
	phrasebook = None


	def initializeMatrix(self, filename):
		self.phrasebook = {}
		phraseFile = open(filename)


	def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
		print("Received message, processing")
		print("AUTHOR ID: " + author_id)
		#if thread_id == '1684891288218201' and thread_type == ThreadType.GROUP:
		if "Hey! Guardsman!" in message_object.text:
			self.send(Message(text="You need something sir?"), thread_id=thread_id, thread_type=thread_type)
		if "Imperial Guard" in message_object.text:
			self.send(Message(text="The Guard's a good place to be...easy place to die"), thread_id=thread_id, thread_type=thread_type)
		# if "for the emperor" in message_object.text:
		# 	self.send(Message(text="For The Emperor!"), thread_id=thread_id, thread_type=thread_type)
		# if inMessage("for the emperor", message_object.text):
		# 	self.send(Message(text="FOR THE EMPEROR!"), thread_id=thread_id, thread_type=thread_type)
		if "for the greater good" in message_object.text.lower():
			self.send(Message(text="FUCK THE TAU!"), thread_id=thread_id, thread_type=thread_type)
		if "for the emperor" in message_object.text.lower() and author_id != "100030233231978":
			self.send(Message(text="FOR THE EMPEROR!"), thread_id=thread_id, thread_type=thread_type)
		if "there's a commissar nearby" in message_object.text.lower():
			self.send(Message(text="Oh fuck not that fucker again"), thread_id=thread_id, thread_type=thread_type)
		if "purge the heretic" in message_object.text.lower():
			self.send(Message(text="Afix Bayonets!"), thread_id=thread_id, thread_type=thread_type)
		if "fuck the tau" in message_object.text.lower() and author_id != "100030233231978":
			self.send(Message(text="Fuck the Tau!"), thread_id=thread_id, thread_type=thread_type)


client = GuardsmanClient('email', 'password')

client.listen()