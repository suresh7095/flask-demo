from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Suresh World Of Tools</title>

<link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:'Poppins',sans-serif;
    background:linear-gradient(135deg,#04142d,#071b44,#13083f);
    color:white;
    min-height:100vh;
}

/* Top Bar */

.navbar{
    background:#02122d;
    padding:12px 30px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    border-bottom:1px solid rgba(255,255,255,0.1);
}

.nav-title{
    font-size:20px;
    color:#ffbf00;
    font-weight:600;
}

.status{
    background:#0d8b2c;
    padding:8px 16px;
    border-radius:20px;
    font-size:13px;
    font-weight:bold;
}

/* Hero */

.hero{
    text-align:center;
    padding:20px 20px 10px;
}

.hero img{
    width:120px;
    border-radius:15px;
    margin-bottom:10px;
    box-shadow:0 10px 25px rgba(0,0,0,0.4);
}

.hero h1{
    font-size:34px;
    margin-bottom:5px;
}

.hero h2{
    font-family:'Pacifico',cursive;
    font-size:58px;
    color:white;
    margin-bottom:5px;
}

.hero h3{
    color:#ffbf00;
    font-size:28px;
    margin-bottom:10px;
}

.hero p{
    font-size:15px;
    color:#d8d8d8;
    line-height:1.6;
}

/* Buttons */

.btn{
    display:inline-block;
    background:#1e90ff;
    color:white;
    text-decoration:none;
    padding:10px 18px;
    border-radius:8px;
    margin:15px 5px;
    font-size:14px;
}

/* Tools */

.tools{
    padding:15px 30px;
}

.tools h2{
    text-align:center;
    margin-bottom:15px;
    font-size:26px;
}

.grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:12px;
}

.card{
    background:white;
    color:black;
    text-align:center;
    padding:12px;
    border-radius:10px;
    transition:0.3s;
}

.card:hover{
    transform:translateY(-3px);
}

.card img{
    height:45px;
    margin-bottom:8px;
}

.card h3{
    font-size:14px;
}

/* Footer */

.footer{
    margin-top:15px;
    background:#02122d;
    padding:12px;
    text-align:center;
    font-size:13px;
}

@media(max-width:900px){

.grid{
    grid-template-columns:repeat(2,1fr);
}

.hero h2{
    font-size:42px;
}

}

</style>
</head>

<body>

<nav class="navbar">

    <div class="nav-title">
        DevOps Portfolio
    </div>

    <div class="status">
        🚀 DEPLOYED SUCCESSFULLY
    </div>

</nav>

<section class="hero">

    <img src="/static/spartan-helmet.png" alt="Spartan Helmet">

    <h1>Welcome To</h1>

    <h2>Suresh's</h2>

    <h3>World Of Tools</h3>

    <p>
        Cloud • DevOps • Automation • CI/CD
        <br>
        AWS • Azure • Docker • Kubernetes • Jenkins • GitHub • Terraform
    </p>

    <a href="#" class="btn">Explore Tools</a>
    <a href="#" class="btn">View Projects</a>

</section>

<section class="tools">

    <h2>Technologies I Work With</h2>

    <div class="grid">

        <div class="card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg">
            <h3>AWS</h3>
        </div>

        <div class="card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg">
            <h3>Azure</h3>
        </div>

        <div class="card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg">
            <h3>Docker</h3>
        </div>

        <div class="card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg">
            <h3>Kubernetes</h3>
        </div>

        <div class="card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg">
            <h3>Jenkins</h3>
        </div>

        <div class="card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg">
            <h3>GitHub</h3>
        </div>

        <div class="card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/terraform/terraform-original.svg">
            <h3>Terraform</h3>
        </div>

        <div class="card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg">
            <h3>Linux</h3>
        </div>

    </div>

</section>

<div class="footer">
    © 2026 Suresh World Of Tools | Flask • Docker • Jenkins • DevOps
</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)