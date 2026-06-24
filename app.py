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

<title>Suresh World of Tools</title>

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

.logo{
    font-size:34px;
    color:#ffbf00;
}

.logo span{
    font-family:'Pacifico',cursive;
    color:white;
    font-size:42px;
}

.status{
    background:#0d8b2c;
    padding:10px 20px;
    border-radius:25px;
    font-weight:bold;
}

/* Hero */
.hero{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:70px;
}

.hero-left{
    width:50%;
}

.hero-left h1{
    font-size:70px;
    line-height:1.1;
}

.hero-left h1 span{
    font-family:'Pacifico',cursive;
    color:#ffffff;
}

.hero-left h2{
    color:#ffbf00;
    font-size:60px;
}

.hero-left p{
    margin-top:20px;
    font-size:20px;
    color:#d6d6d6;
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
}

/* Logo Grid */
.tools{
    padding:40px 70px;
}

.tools h2{
    text-align:center;
    margin-bottom:30px;
}

.grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(180px,1fr));
    gap:20px;
}

.card{
    background:white;
    color:black;
    text-align:center;
    padding:20px;
    border-radius:12px;
}

.card img{
    height:80px;
    margin-bottom:10px;
}

/* Footer */
.footer{
    margin-top:50px;
    background:#02122d;
    padding:25px;
    text-align:center;
}
</style>
</head>

<body>

<nav class="navbar">
    <div class="logo">
        <span>Suresh</span> World Of Tools
    </div>

    <div class="status">
        ✅ DEPLOYED SUCCESSFULLY
    </div>
</nav>

<section class="hero">

    <div class="hero-left">
        <h1>Welcome to</h1>
        <h2><span>Suresh</span><br>World Of Tools</h2>

        <p>
            Cloud | DevOps | Automation | CI/CD
            <br><br>
            AWS • Azure • Docker • Kubernetes • Jenkins • GitHub • Terraform
        </p>

        <a href="#" class="btn">Explore Tools</a>
        <a href="#" class="btn">View Projects</a>
    </div>

    <div class="hero-right">
        <img width="500"
        src="https://upload.wikimedia.org/wikipedia/commons/e/e3/Devops-toolchain.svg">
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
    © 2026 Suresh World Of Tools | DevOps Demo Project
</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)