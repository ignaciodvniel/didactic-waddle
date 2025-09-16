import re
import html as html_lib
import streamlit as st

def make_id(title):
    return "card-" + re.sub(r'[^0-9a-zA-Z\\-]+', '-', title)

card_18 = """

PD: Iré borrando las cartas antiguas, las conservaré para mí, se que ya no me amas, se que no las guardarás. Tengo miedo de que me odies, tengo miedo de tu rencor, no me destruyas por favor.
"""
card_19 ="""Esta carta es dura y no fue mi intención hacerla así, pero si el haberme amado no te hace recapacitar en tus acciones me sale esto:

Nadie que no sea un infiel o un abusador mental/físico merece que lo terminen, es un acto de crueldad, inmadurez y/o simplemente falta de amor.

Me dejaste de amar por mi actitudes, está bien, no quisiste arreglar las cosas, entonces tu amor nunca fue tan inmenso como creías. Es hiriente, y tus canciones me confirman que tu intención fue herirme, yo te doy asco y lo comprendo, pero no lo comparto. No importa lo mucho que intentes justificarte, me prometiste amor incondicional y lo rompiste, tú sabes que pudimos solucionarlo como muchas cosas antes, pero elegiste abandonarme. 

Es cierto, todos merecemos sentirnos felices y realizados, pase lo que pase. Si cometiste errores, puedes aprender de ellos. En el futuro, no los vas a repetir cuando importe, pero ese es el punto, dejé de importarte, dejaste de amarme y me obligaste a leer tu carta de despecho, muy distinta a la mía.

Ya no hay nada más que hablar, te di la despedida más gentil y llena de amor, pero tu cortaste al escucharme decir “Ok, se acabó” ¿Por qué? Porque no me amas. 

Lamentablemente no pudiste cerrar este ciclo en buenos términos, tus palabras fueron vacías y te picaban las manos por deshacerte de mí o de esa llamada. Encontraré a alguien que sea el amor de mi vida, y seré mucho mejor pareja a diferencia de ti, porque yo me humillé por amor, porque luché por saber lo que pasó y cómo mejorar.

En síntesis, no te odio, no te guardo ningún tipo de rencor, jamás pensé en ti en ninguna canción de despecho, porque tu mamá tenía razón, soy un caballero. Fuiste la mujer que amé, y voy a respetar tu nombre hasta siempre. Sigue haciéndome mierda con tus amigas, sigue comiéndote weones frente a mí, sigue haciéndome saber lo mejores que son en comparación de mí (cuando yo solo pude decir que eres mejor que todas mis tinder-citas (otra maldita crueldad tuya, parece que omites que tú me dejaste) o minas que conocí), yo estaré aquí para decir solo buenas palabras de ti y comerme todo el odio que sembraste.

Te aconsejo tocar este tema en tu terapia, no es normal que odies a tantas personas, no es normal odiar de por sí. Y tratar mal a la persona que dedicó su mundo durante todo tu período universitario es preocupante.

Hasta nunca, Antonia. Espero esto te haga mejorar como persona y actúes como dices te criaron, como la persona de la cual me enamoré.
"""
cards = [
    {"id": make_id("16-09-2025"), "title": "16-09-2025", "content": card_18},
    {"id": make_id("fin"), "title": "fin", "content": card_19},
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
