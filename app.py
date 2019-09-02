from flask import Flask, request
import base64
import codecs

app = Flask(__name__)

hashes = ["pzzki2","b7d7d20cec9ebd4cd2a91c56325972d5"]

def htmlImage():
	f=codecs.open("playfair", 'r')
	return f.read()

def Image():
	with open("Hash.jpg", "rb") as image:
		b64string = base64.b64encode(image.read())
	return b64string

@app.route('/CcNC')
def rebound():
	try:
		key = request.args.get('key')
		
		if key == "stego":
			return htmlImage()
		elif key == "Zmlu":
			return "Yes! You have finished this puzzle. :)"
		elif key.lower() in hashes:
			return Image()
		else:
			return "<html><font color = \"white\" size = \"20\">opubmmspbetmfbeupspnf.cvujujtbojdftubsu. Why are emperors names so wierdly...?</font></html>"
	except:
		return "<html><font color = \"white\" size = \"20\">opubmmspbetmfbeupspnf.cvujujtbojdftubsu. Why are emperors names so wierdly...?</font></html>"

@app.route('/')
def fail():
	return "<html><font color = \"white\" size = \"20\">opubmmspbetmfbeupspnf.cvujujtbojdftubsu. Why are emperors names so wierdly...?</font></html>"

if __name__ == '__main__':
	app.run()
