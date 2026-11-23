# usei o tradutor pra traduzior o os pro japonês, pq eu sou um idiota
# あなた = os
# チーム = time
# レンダリングテンプレート = render_template
# フラスコ = Flask
# 前 = Fore
# スタイル = Style
# プラットフォーム = Platform
# 再 = re
# 掃除する = Limpar
# サーバーを起動する = start_server
# espero que goste da porra do codigo, SEU MERDA !

import os as あなた
import time as チーム
import platform as プラットフォーム
import re as 再
from flask import Flask as フラスコ,render_template as レンダリングテンプレート
from colorama import Fore as 前,Style as スタイル
from pathlib import Path

# funções
def 掃除する():
    あなた.system('cls')

def サーバーを起動する():
    BASE_DIR = Path(__file__).resolve().parent
    TEMPLATES_DIR = BASE_DIR / "templates"

    app = フラスコ(
        __name__,
        template_folder="templates",
        static_folder="templates",
        static_url_path="/assets"
    )

    @app.route("/")
    def home():
        html = レンダリングテンプレート("index.html")


        extensoes = (
            ".png", ".jpg", ".jpeg", ".gif", ".webp",
            ".ico", ".mp3", ".wav", ".ogg",
            ".mp4", ".webm"
        )

        def carregar(match):
            atributo = match.group(1)
            caminho = match.group(2)

            if caminho.startswith(("http://", "https://", "/", "data:", "#")):
                return match.group(0)

            arquivo = TEMPLATES_DIR / caminho

            if arquivo.suffix.lower() in extensoes and arquivo.is_file():
                return f'{atributo}="/assets/{caminho}"'

            return match.group(0)

        html = 再.sub(
            r'(src|href)=["\']([^"\']+)["\']',
            carregar,
            html
        )

        return html


    if __name__ == "__main__":
        app.run(debug=True)

# configuração básica
掃除する()
あなた.system('title Servidor Flask')

print(f'{前.LIGHTBLUE_EX}code by stock!{スタイル.RESET_ALL}\n')
print(前.YELLOW + プラットフォーム.system()+スタイル.RESET_ALL, 前.YELLOW + プラットフォーム.release() + スタイル.RESET_ALL,'\n')
print(f'{前.CYAN}1) iniciar servidor\n{スタイル.RESET_ALL}')

質問 = input(f'{前.LIGHTBLUE_EX}Escolha uma opção: {スタイル.RESET_ALL}')

if 質問 == '1':
    print(f'{前.MAGENTA}\nIniciando servidor...{スタイル.RESET_ALL}')
    チーム.sleep(2)
    print(f'{前.GREEN}Servidor iniciado com sucesso!{スタイル.RESET_ALL}')
    サーバーを起動する()
elif 質問 == '0':
        掃除する()
        exit()
else:
    print(f'{前.RED}Opção inválida!{スタイル.RESET_ALL}')