from flask import Flask

app = Flask(__name__)

@app.route("/hello/<name>")

def hello_person(name):
	html = """
		<h1>
			Hello {}!
		</h1>
		<p>
			Here's a picture of some Banksy street art
		</p>
		<img src ="https://farm4.staticflickr.com/3671/10547215773_86a12b5ce3_o.jpg">
	"""
	return html.format(name.title())

if __name__ == "__main__":
	app.run()