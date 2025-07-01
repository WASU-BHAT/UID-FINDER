from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

GRAPH_API_URL = "https://graph.facebook.com/v18.0"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>BHAT WASU - UID Finder</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      background: url('https://i.ibb.co/qYtGC5Kz/In-Shot-20250306-044013972.jpg') no-repeat center center fixed;
      background-size: cover;
      color: white;
      text-align: center;
    }

    .container {
      max-width: 400px;
      margin: 80px auto;
      background: rgba(0, 0, 0, 0.85);
      padding: 30px 20px;
      border-radius: 15px;
      border: 2px solid white;
      box-shadow: 0 0 15px white;
    }

    .title {
      font-size: 28px;
      font-weight: bold;
      color: #00ffff;
      animation: moveUpDown 2s infinite;
      text-shadow: 0 0 10px cyan;
      margin-bottom: 30px;
    }

    @keyframes moveUpDown {
      0% { transform: translateY(0); }
      50% { transform: translateY(-10px); }
      100% { transform: translateY(0); }
    }

    input[type="text"] {
      width: 90%;
      padding: 12px;
      border-radius: 8px;
      border: 2px solid white;
      background: black;
      color: white;
      font-size: 16px;
      animation: glowInput 2s infinite alternate;
      box-shadow: 0 0 8px #00ffff;
    }

    @keyframes glowInput {
      from { box-shadow: 0 0 5px white; }
      to { box-shadow: 0 0 12px cyan; }
    }

    button {
      margin-top: 20px;
      padding: 10px 20px;
      font-size: 15px;
      border: 2px solid white;
      background: blue;
      color: white;
      border-radius: 6px;
      cursor: pointer;
      animation: glowBtn 2s infinite alternate;
    }

    button:hover {
      background: darkblue;
    }

    @keyframes glowBtn {
      from { box-shadow: 0 0 5px white; }
      to { box-shadow: 0 0 15px blue; }
    }

    .result-item {
      margin-top: 15px;
      padding: 10px;
      background: black;
      border: 2px solid white;
      border-radius: 10px;
      animation: glowResult 2s infinite alternate;
    }

    @keyframes glowResult {
      from { box-shadow: 0 0 5px white; }
      to { box-shadow: 0 0 15px magenta; }
    }

    .result-item strong {
      color: #00ffff;
      font-size: 17px;
    }

    .footer-box {
      margin-top: 30px;
      padding: 10px;
      background: rgba(0, 0, 0, 0.7);
      border: 2px solid white;
      border-radius: 10px;
      font-weight: bold;
      font-size: 14px;
      animation: glowFooter 2s infinite alternate;
    }

    @keyframes glowFooter {
      from { box-shadow: 0 0 5px white; }
      to { box-shadow: 0 0 15px pink; }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="title">MR PRINCE</div>
    <form method="POST">
      <input type="text" name="token" placeholder="Enter Access Token" required>
      <button type="submit">Submit</button>
    </form>

    {% if groups %}
      {% for group in groups %}
        <div class="result-item">
          <strong>{{ group.name }}</strong><br>
          UID: {{ group.id }}
        </div>
      {% endfor %}
    {% endif %}

    {% if error %}
      <div class="result-item" style="color: red;">{{ error }}</div>
    {% endif %}

    <div class="footer-box">THEW THE UNSTOPABLE LEGEND BO'II WASU ❣️</div>
  </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        access_token = request.form.get('token')

        if not access_token:
            return render_template_string(HTML_TEMPLATE, error="Token is required")

        url = f"{GRAPH_API_URL}/me/conversations?fields=id,name&access_token={access_token}"

        try:
            response = requests.get(url)
            data = response.json()

            if "data" in data:
                return render_template_string(HTML_TEMPLATE, groups=data["data"])
            else:
                return render_template_string(HTML_TEMPLATE, error="Invalid token or no Messenger groups found")
        except:
            return render_template_string(HTML_TEMPLATE, error="Something went wrong")

    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    print("🔥 Flask server started on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)
