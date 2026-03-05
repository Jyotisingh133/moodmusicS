from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

songs = {

"happy":[
{"title":"Kala Chashma","link":"https://www.youtube.com/embed/k4yXQkG2s1E?autoplay=1"},
{"title":"London Thumakda","link":"https://www.youtube.com/embed/udra3Mfw2oo?autoplay=1"},
{"title":"Kar Gayi Chull","link":"https://www.youtube.com/embed/NTHz9ephYTw?autoplay=1"},
{"title":"Badtameez Dil","link":"https://www.youtube.com/embed/II2EO3Nw4m0?autoplay=1"},
{"title":"Gallan Goodiyan","link":"https://www.youtube.com/embed/jCEdTq3j-0U?autoplay=1"},
{"title":"Cutiepie","link":"https://www.youtube.com/embed/p4W1b0m2Xr8?autoplay=1"},
{"title":"Bom Diggy","link":"https://www.youtube.com/embed/JjF2kU7q4d0?autoplay=1"},
{"title":"Saturday Saturday","link":"https://www.youtube.com/embed/0G2VxhV_gXM?autoplay=1"},
{"title":"Nachde Ne Saare","link":"https://www.youtube.com/embed/8M7Qm9l8G0k?autoplay=1"},
{"title":"Dil Dhadakne Do","link":"https://www.youtube.com/embed/TqC4gKQhMZ0?autoplay=1"},
{"title":"Gallan Kardi","link":"https://www.youtube.com/embed/8sG2v2Y7GJ8?autoplay=1"},
{"title":"Proper Patola","link":"https://www.youtube.com/embed/K0ibBPhiaG0?autoplay=1"}
],

"sad":[
{"title":"Channa Mereya","link":"https://www.youtube.com/embed/284Ov7ysmfA?autoplay=1"},
{"title":"Tujhe Kitna Chahne Lage","link":"https://www.youtube.com/embed/QoQ0qFz9XWQ?autoplay=1"},
{"title":"Hamari Adhuri Kahani","link":"https://www.youtube.com/embed/fdubeMFwuGs?autoplay=1"},
{"title":"Phir Bhi Tumko Chahunga","link":"https://www.youtube.com/embed/_iktURk0X-A?autoplay=1"},
{"title":"Agar Tum Saath Ho","link":"https://www.youtube.com/embed/sK7riqg2mr4?autoplay=1"},
{"title":"Khairiyat","link":"https://www.youtube.com/embed/hoNb6HuNmU0?autoplay=1"},
{"title":"Bekhayali","link":"https://www.youtube.com/embed/VOLKJJvfAbg?autoplay=1"},
{"title":"Tum Hi Ho","link":"https://www.youtube.com/embed/Umqb9KENgmk?autoplay=1"},
{"title":"Tera Ban Jaunga","link":"https://www.youtube.com/embed/Qdz5n1Xe5Qo?autoplay=1"},
{"title":"Lo Safar","link":"https://www.youtube.com/embed/IVBwE6c9qYI?autoplay=1"},
{"title":"Dil Ke Paas","link":"https://www.youtube.com/embed/Q1qvJzVx6v0?autoplay=1"},
{"title":"Judaai","link":"https://www.youtube.com/embed/k4yXQkG2s1E?autoplay=1"}
],

"romantic":[
{"title":"Raabta","link":"https://www.youtube.com/embed/zlt38OOqwDc?autoplay=1"},
{"title":"Dil Diyan Gallan","link":"https://www.youtube.com/embed/SAcpESN_Fk4?autoplay=1"},
{"title":"Raatan Lambiyan","link":"https://www.youtube.com/embed/gvyUuxdRdR4?autoplay=1"},
{"title":"Kesariya","link":"https://www.youtube.com/embed/BddP6PYo2gs?autoplay=1"},
{"title":"Hawayein","link":"https://www.youtube.com/embed/cYOB941gyXI?autoplay=1"},
{"title":"Bol Do Na Zara","link":"https://www.youtube.com/embed/0NFxcNheoLc?autoplay=1"},
{"title":"Tera Hone Laga Hoon","link":"https://www.youtube.com/embed/rTuxUAuJRyY?autoplay=1"},
{"title":"Pehli Nazar Mein","link":"https://www.youtube.com/embed/BadBAMnPX0I?autoplay=1"},
{"title":"Tum Mile","link":"https://www.youtube.com/embed/mt9xg0mmt28?autoplay=1"},
{"title":"Enna Sona","link":"https://www.youtube.com/embed/cP8k0s3dF5I?autoplay=1"},
{"title":"Janam Janam","link":"https://www.youtube.com/embed/v0UXgoJ6Shg?autoplay=1"},
{"title":"Gerua","link":"https://www.youtube.com/embed/AEIVhBS6baE?autoplay=1"}
],

"neutral":[
{"title":"Ilahi","link":"https://www.youtube.com/embed/fdubeMFwuGs?autoplay=1"},
{"title":"Subhanallah","link":"https://www.youtube.com/embed/QYO6AlxiRE4?autoplay=1"},
{"title":"Safarnama","link":"https://www.youtube.com/embed/Ay8rY9m7C5A?autoplay=1"},
{"title":"Zinda","link":"https://www.youtube.com/embed/A0T9gCAnFjE?autoplay=1"},
{"title":"Patakha Guddi","link":"https://www.youtube.com/embed/vKDsAB1ccn0?autoplay=1"},
{"title":"Love You Zindagi","link":"https://www.youtube.com/embed/5oU9uKk6F9c?autoplay=1"},
{"title":"Sooraj Dooba Hai","link":"https://www.youtube.com/embed/nJZcbidTutE?autoplay=1"},
{"title":"Ik Vaari","link":"https://www.youtube.com/embed/8xN5FQqk7qA?autoplay=1"},
{"title":"Dil Chahta Hai","link":"https://www.youtube.com/embed/5Yy0jRrHn0U?autoplay=1"},
{"title":"Yeh Jawaani Hai Deewani","link":"https://www.youtube.com/embed/k0m4S7k7hN8?autoplay=1"},
{"title":"Senorita","link":"https://www.youtube.com/embed/yZ1GgB4bNqQ?autoplay=1"},
{"title":"Matargashti","link":"https://www.youtube.com/embed/hZp5YHylfCM?autoplay=1"}
]

}

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/detect')
def detect():

    emotion = random.choice(["happy","sad","romantic","neutral"])

    song = random.choice(songs[emotion])

    return jsonify({
        "emotion":emotion,
        "song":song
    })


if __name__ == "__main__":
    app.run(debug=True)