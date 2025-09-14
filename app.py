import re
import html as html_lib
import streamlit as st

def make_id(title):
    return "card-" + re.sub(r'[^0-9a-zA-Z\-]+', '-', title)

card_13 = """Texto de la carta del 13-09-2025. Pega aquí contenido largo; puedes usar saltos de línea libremente.
Puedes incluir comillas simples ' y dobles " sin problema.
"""

card_14 = """Nada de lo que me digas me quita de la cabeza que eres el amor de mi vida, aunque entendí muchas cosas. Ni siquiera se si alguna vez verás estas cartas, porque no planeo avisarte de ellas, decidiste alejarte de mí y lo entiendo.

Otra vez me congelé, quise despedirme pero nuevamente, no sabía cómo. Las lágrimas se secan y sedimentan en mis lentes de sol, que debo lavar diariamente, de cierta forma me gusta ocultar parte del sufrimiento cuando me veo al espejo.

Esto se ve sin salto de línea como los párrafos siguientes, pasa siempre en el primer y segundo párrafo
"""

cards = [
    {"id": make_id("13-09-2025"), "title": "13-09-2025", "content": card_13},
    {"id": make_id("14-09-2025"), "title": "14-09-2025", "content": card_14},
]

css = """
<style>
:root{ -webkit-user-select:none; -moz-user-select:none; -ms-user-select:none; user-select:none; }
html, body, .stApp { -webkit-user-select:none !important; -moz-user-select:none !important; -ms-user-select:none !important; user-select:none !important; }
.nav{ position:sticky; top:0; background:rgba(255,255,255,0.95); padding:10px; z-index:1000; display:flex; gap:8px; flex-wrap:wrap; align-items:center; border-bottom:1px solid rgba(0,0,0,0.06); }
.nav a{ text-decoration:none; }
.nav button{ padding:8px 12px; border:1px solid rgba(0,0,0,0.08); border-radius:6px; background:transparent; cursor:pointer; font-weight:600; }
.card{ border-radius:8px; padding:20px; margin:24px 0; box-shadow:0 2px 8px rgba(0,0,0,0.04); background:#ffffff; }
.card h3{ margin:0 0 8px 0; font-size:18px; }
.card-content{ white-space:pre-wrap; -webkit-user-select:none; -moz-user-select:none; -ms-user-select:none; user-select:none; }
</style>
"""

st.markdown(css, unsafe_allow_html=True)

nav_html = '<div class="nav">' + ''.join(f'<a href="#{c["id"]}"><button>{c["title"]}</button></a>' for c in cards) + '</div>'
st.markdown(nav_html, unsafe_allow_html=True)

for c in cards:
    text = c["content"].replace("\r\n", "\n").replace("\r", "\n")
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip() != ""]
    escaped_paras = []
    for p in paragraphs:
        p_escaped = html_lib.escape(p).replace("\n", "<br>")
        escaped_paras.append(f"<p>{p_escaped}</p>")
    content_html = "".join(escaped_paras) if escaped_paras else "<p></p>"

    card_html = (
        f'<div class="card" id="{c["id"]}" oncopy="return false" oncut="return false" '
        f'onpaste="return false" oncontextmenu="return false" draggable="false" unselectable="on">'
        f'<h3>{c["title"]}</h3>'
        f'<div class="card-content">{content_html}</div>'
        f'</div>'
    )
    st.markdown(card_html, unsafe_allow_html=True)
