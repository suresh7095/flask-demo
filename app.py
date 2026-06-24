from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Google Clone</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 150px;
        }

        .logo {
            font-size: 90px;
            font-weight: bold;
        }

        .blue { color: #4285F4; }
        .red { color: #EA4335; }
        .yellow { color: #FBBC05; }
        .green { color: #34A853; }

        input {
            width: 600px;
            padding: 12px;
            border: 1px solid #dcdcdc;
            border-radius: 25px;
            font-size: 16px;
            margin-top: 20px;
        }

        button {
            margin-top: 20px;
            padding: 10px 20px;
            border: none;
            background: #f8f9fa;
            cursor: pointer;
            border-radius: 4px;
        }

        button:hover {
            border: 1px solid #dadce0;
        }
    </style>
</head>
<body>

<div class="logo">
    <span class="blue">G</span>
    <span class="red">o</span>
    <span class="yellow">o</span>
    <span class="blue">g</span>
    <span class="green">l</span>
    <span class="red">e</span>
</div>

<input type="text" placeholder="Search Google or type a URL">

<br>

<button>Google Search</button>
<button>I'm Feeling Lucky</button>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)