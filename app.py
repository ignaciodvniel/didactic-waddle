import re
import html as html_lib
import streamlit as st

def make_id(title):
    return "card-" + re.sub(r'[^0-9a-zA-Z\\-]+', '-', title)

card_1 = """Seguiré escribiendo para mí, esto es estúpido. Si quiera los lees? Es ridículo para tí? Lo aprecias? no tengo idea.
"""
cards = [
    {"id": make_id("???"), "title": "???", "content": card_1},
]

css = """
<style>
:root{ -webkit-user-select:none; -moz-user-select:none; -ms-user-select:none; user-select:none; }

/* Base font */
html, body, .stApp {
    font-family: Georgia, 'Times New Roman', serif;
    -webkit-user-select:none !important;
    -moz-user-select:none !important;
    -ms-user-select:none !important;
    user-select:none !important;
}

/* Nav bar */
.nav{
    position:sticky; top:0; background:var(--background-color);
    padding:10px; z-index:1000; display:flex; gap:8px;
    flex-wrap:wrap; align-items:center;
    border-bottom:1px solid rgba(0,0,0,0.06);
}
.nav a{ text-decoration:none; }
.nav button{
    padding:8px 12px;
    border:1px solid rgba(0,0,0,0.15);
    border-radius:6px;
    background:transparent;
    cursor:pointer;
    font-weight:600;
    font-family: Georgia, 'Times New Roman', serif;
    color: var(--text-color);
}

/* Cards */
.card{
    border-radius:8px;
    padding:20px;
    margin:24px 0;
    box-shadow:0 2px 8px rgba(0,0,0,0.05);
    background:var(--card-bg);
    color: var(--text-color);
}
.card h3{
    margin:0 0 8px 0;
    font-size:18px;
}
.card-content{
    white-space:pre-wrap;
    text-align:justify;
    line-height:1.6;
}
.card-content p{
    text-align:justify;
    margin:0 0 1rem 0;
}

/* Light mode */
@media (prefers-color-scheme: light) {
    :root{
        --card-bg: #ffffff;
        --text-color: #222222;
        --background-color: rgba(255,255,255,0.95);
    }
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
    :root{
        --card-bg: #1e1e1e;
        --text-color: #e6e6e6;
        --background-color: rgba(30,30,30,0.95);
    }
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# Barra de navegación
nav_html = '<div class="nav">' + ''.join(
    f'<a href="#{c["id"]}"><button>{c["title"]}</button></a>' for c in cards
) + '</div>'
st.markdown(nav_html, unsafe_allow_html=True)

# Renderizado de cartas
for c in cards:
    text = c["content"].replace("\r\n", "\n").replace("\r", "\n")
    paragraphs = [p for p in text.split("\n\n")]
    escaped_paras = []
    for p in paragraphs:
        p_escaped = html_lib.escape(p.strip()).replace("\n", "<br>")
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
