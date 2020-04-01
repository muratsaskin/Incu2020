from flask import Flask, request
import requests
import json

bot_name = 'unwomenunofficial@webex.bot'
token = 'YTc1YmU4MTgtMDM5MS00ZGU2LWFjMGQtMWQwODk3OTYwNWM3MDJiYWNiOWUtYTBl_PF84_consumer'
header = {"content-type": "application/json; charset=utf-8",
		  "authorization": "Bearer " + token}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sendMessage():
	webhook = request.json
	url = 'https://api.ciscospark.com/v1/messages'
	msg = {"roomId": webhook["data"]["roomId"]}
	sender = webhook["data"]["personEmail"]
	message = getMessage()
	if (sender != bot_name):
		if (message == "Hello"):
			msg["markdown"] = "Hey! Welcome to **UN Women!** 😊 This bot is created for educational purposes only and is NOT an official release of United Nations (UN), or it's any other entities. The United Nations Entity for Gender Equality and the Empowerment of Women, also known as UN Women, is a United Nations entity working for the empowerment of women. List of available commands: \n- **Help** for Reporting Violence \n- **Info** for Recognizing Forms of Violence"
		elif (message == "Help"):
			msg["markdown"] = "**Investigations hotline:** Phone: +1 212 963-1111 (24 hours a day), **OR** Online reporting form: https://reportwrongdoing.unov.org/(X(1)S(1fv4vhg2jw2slnrab2hectte))/default.aspx?AspxAutoDetectCookieSupport=1"
		elif (message == "Info"):
			msg["markdown"] = "Violence against women is a human rights violation of pandemic proportions. We are striving to make the world a better place by ending violence against women. What kind of violence do you need help with? You can type: \n- 'Intimate Partner Violence' \n- 'Sexual Violence and Harassment' \n- 'Human Trafficking' \n- 'Child Marriage'"
		elif (message == "Intimate Partner Violence"):
				msg["markdown"] = "This is one of the most common forms of violence experienced by women globally. 1 in 3 women has experienced physical or sexual violence- mostly by an intimate partner. Worldwide, 1 in 2 women killed were killed by their partners or family in 2012. \n- If there is someone you know who is going through this, we would like to solve it. \n- Type 'Help' for reporting, or you can look at other forms of violence."
		elif (message == "Sexual Violence and Harassment"):
				msg["markdown"] = "Any sexual act or attempt to obtain a sexual act by violence or coercion, or acts directed against a person's sexuality, **regardless of the relationship to the victim**. 15 million adolescent women have experienced forced sex at some point in their life. \n- If there is someone you know who is going through this, we would like to solve it. \n- Type 'Help' for reporting, or you can look at other forms of violence."
		elif (message == "Human Trafficking"):
				msg["markdown"] = "71% of all trafficking victims worldwide are women. 3 out of 4 trafficked women are trafficked for sexual exploitation. \n- If there is someone you know who is going through this, we would like to solve it. \n- Type 'Help' for reporting, or you can look at other forms of violence."
		elif (message == "Child Marriage"):
				msg["markdown"] = "This puts an end to girl's education, vocation and her right to make life choices 🙁 Child marriage leads to greater risk for intimate partner violence. 650 million women and girls today were married before their 18th birthday. 4 in 10 girls in West and Central Africa were married before they were 18. \n- If there is someone you know who is going through this, we would like to solve it. \n- Type 'Help' for reporting, or you can look at other forms of violence."
		else:
			msg["markdown"] = "Sorry! I didn't recognize that. Type **Help** to Report Violence, or **Info** to Recognize Forms of Violence."
		requests.post(url,data=json.dumps(msg), headers=header, verify=True)

def getMessage():
	webhook = request.json
	url = 'https://api.ciscospark.com/v1/messages/' + webhook["data"]["id"]
	get_msgs = requests.get(url, headers=header, verify=True)
	message = get_msgs.json()['text']
	return message

app.run(debug = True)
