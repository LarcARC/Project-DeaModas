from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    # URL do site que você deseja extrair o conteúdo
    url = "https://earth.google.com/web/@-5.67167031,-61.51112367,61.9294927a,5004906.66973315d,35y,0h,0t,0r/data=CjISMBIgN2IxOGI1NTcyYjRhMTFlN2E5MGIxZmI3OTk1MDNkMmUiDHNwbGFzaHNjcmVlbg"

    # Faz a requisição HTTP para obter o conteúdo HTML da página
    response = requests.get(url)
    html_content = response.content

    # Parseia o conteúdo HTML usando o Beautiful Soup
    soup = BeautifulSoup(html_content, "html.parser")

    # Encontra o elemento específico que deseja extrair
    # Por exemplo, para extrair o conteúdo dentro da tag <div id="conteudo">...</div>
    conteudo_div = soup.find("div", id="conteudo")

    # Renderiza o template HTML com o conteúdo extraído
    return render_template("inicio.html",conteudo=conteudo_div)

if __name__ == "__main__":
    app.run()
