from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
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
}

/* Navbar */

.navbar{
    background:#02122d;
    padding:18px 40px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    border-bottom:1px solid rgba(255,255,255,0.1);
}

.nav-title{
    font-size:24px;
    font-weight:600;
    color:#ffbf00;
}

.status{
    background:#0d8b2c;
    padding:10px 20px;
    border-radius:25px;
    font-weight:bold;
}

/* Hero Section */

.hero{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:70px;
    min-height:500px;
}

.hero-left{
    width:55%;
}

.hero-left h1{
    font-size:60px;
    margin-bottom:10px;
}

.hero-left h2{
    font-family:'Pacifico',cursive;
    font-size:90px;
    color:white;
    margin-bottom:10px;
}

.hero-left h3{
    font-size:50px;
    color:#ffbf00;
    margin-bottom:20px;
}

.hero-left p{
    font-size:22px;
    color:#d6d6d6;
    line-height:1.8;
}

.btn{
    margin-top:30px;
    display:inline-block;
    background:#1e90ff;
    color:white;
    text-decoration:none;
    padding:15px 30px;
    border-radius:8px;
    margin-right:15px;
    transition:0.3s;
}

.btn:hover{
    transform:translateY(-3px);
}

/* Helmet */

.hero-right{
    width:40%;
    text-align:center;
}

.hero-right img{
    width:350px;
    border-radius:20px;
    box-shadow:0 20px 40px rgba(0,0,0,0.5);
}

/* Tools Section */

.tools{
    padding:50px 70px;
}

.tools h2{
    text-align:center;
    margin-bottom:40px;
    font-size:40px;
}

.grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(180px,1fr));
    gap:25px;
}

.card{
    background:white;
    color:black;
    text-align:center;
    padding:25px;
    border-radius:15px;
    transition:0.3s;
}

.card:hover{
    transform:translateY(-5px);
}

.card img{
    height:80px;
    margin-bottom:15px;
}

/* Footer */

.footer{
    margin-top:50px;
    background:#02122d;
    padding:25px;
    text-align:center;
    font-size:18px;
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

    <div class="hero-left">

        <h1>Welcome To</h1>

        <h2>Suresh</h2>

        <h3>World Of Tools</h3>

        <p>
            Cloud • DevOps • Automation • CI/CD
            <br><br>
            AWS • Azure • Docker • Kubernetes
            <br>
            Jenkins • GitHub • Terraform
        </p>

        <a href="#" class="btn">Explore Tools</a>
        <a href="#" class="btn">View Projects</a>

    </div>

    <div class="hero-right">

        <img src="/static/spartan-helmet.png" alt="Spartan Helmet">

    </div>

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

    </div>

</section>

<div class="footer">
    © 2026 Suresh World Of Tools | Built with Flask, Docker & Jenkins
</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)