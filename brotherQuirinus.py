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

	def loadPhraseBook(self, filename):
		phrasebook = {}
		phrases = open(filename, "r")
		for line in phrases:
			str1, str2 = line.split(",")
			phrasebook[str1] = str2
		print(str(phrasebook))
		phrases.close()



	def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
		print("Received message, processing")
		print("AUTHOR ID: " + author_id)
		
		#if thread_id == '1684891288218201' and thread_type == ThreadType.GROUP:
		if "for the emperor" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="FOR PRIMARCH GUILLIMAN AND THE EMPEROR!"), thread_id=thread_id, thread_type=thread_type)	
		if "fuck the tau" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="Fuck the Tau!"), thread_id=thread_id, thread_type=thread_type)
		if "assemble astartes" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="Marine squad deployed!"), thread_id=thread_id, thread_type=thread_type)
		if "greater good" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="Xenos scum!"), thread_id=thread_id, thread_type=thread_type)
		if "raise the banner high" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="Let the degenerates know who comes to conquer them this day!"), thread_id=thread_id, thread_type=thread_type)
		if "play chaos" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="Heretic! Cleanse, Purge, KILL!"), thread_id=thread_id, thread_type=thread_type)
		if "titan inbound" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="Fall back and regroup!"), thread_id=thread_id, thread_type=thread_type)
		if "play space marines" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="He who stands with me shall be my brother."), thread_id=thread_id, thread_type=thread_type)
		if "we march for macragge" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="AND WE SHALL KNOW NO FEAR!"), thread_id=thread_id, thread_type=thread_type)
		if "courage and honor" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="COURAGE AND HONOUR!"), thread_id=thread_id, thread_type=thread_type)								
		if "emperor protects" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="And having a loaded bolter never hurt, either"), thread_id=thread_id, thread_type=thread_type)
		if "i don't want to paint" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="The codex astartes does not support this action"), thread_id=thread_id, thread_type=thread_type)
		if "primaris marines are cooler" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="At least I can enter more transports"), thread_id=thread_id, thread_type=thread_type)
		if "i love this group" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="The Emperor loves you too"), thread_id=thread_id, thread_type=thread_type)
		if "play tyranids" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="Ask me about how Hive Fleet Behemoth ended up..."), thread_id=thread_id, thread_type=thread_type)
		if "play orks" in message_object.text.lower() and author_id != "100030347255471":
			self.send(Message(text="Cleanse them with sword and fire!"), thread_id=thread_id, thread_type=thread_type)		
		for key in self.phrasebook:
			if key in message_object.text.lower() and author_id != "100030347255471":
				self.send(Message(text=phrasebook[key]), thread_id=thread_id, thread_type=thread_type)


client = GuardsmanClient("email", "pw")
client.loadPhrasebook("testbook")

client.listen()
