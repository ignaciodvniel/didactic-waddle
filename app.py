import re
import html as html_lib
import streamlit as st

def make_id(title):
    return "card-" + re.sub(r'[^0-9a-zA-Z\\-]+', '-', title)

card_18 = """

PD: Iré borrando las cartas antiguas, las conservaré para mí, se que ya no me amas, se que no las guardarás. Tengo miedo de que me odies, tengo miedo de tu rencor, no me destruyas por favor.
"""
card_19 ="""En la noche me comí unas tostadas, no estaban tan ricas, me duele el estómago porque por alguna razón comer me duele. No puedo levantarme, tengo cosas que hacer y no puedo hacerlas.

No me arrepiento de nada de lo que hice, me deja en paz saber que lo intenté. Jamás imaginé que las cosas serían así, hubo promesas que se rompieron y son puñaladas que me atraviesan desde el estómago hasta la garganta.

Se supone que mostrarte mi debilidad, mi disposición y saber de mí en general ayuda a que me puedas olvidar. Pero tú estás bien.

Voy a dormir un rato más.

PD:

No pude hacer nada de lo que te dije, las flores fueron las más bellas que encontré y me emocionaba pensar la pequeña posibilidad de que las olieras, dijeras que son hermosas y las pusieras en un jarrón en vez de botarlas.

Me ejercité hasta que mis músculos ardieron, pero no puedo llegar a los 130g de proteína, solo hice ~80g, no puedo forzarme a comer más, hasta para eso soy un perdedor. Posteriormente me dormí del agotamiento de quien sabe qué (falta de carbohidratos?) y lamentablemente volví a soñar contigo, esta vez no habían suspiros, calor ni abrazos, solo conversaciones inacabables, de cuando disfrutabas hablarme.

Como duele despertar después de volver a ser feliz, abrir los ojos y no encontrar nada más que cenizas, dolor y la pregunta de siempre ¿Cómo pudiste dejarme? Eras mi princesa, mi única preocupación y fallé, pudiste olvidarme.

Lees estas cartas?
"""

card_20 = """Son las 3:12 am, acabo de bañarme y acostarme. Salí cerca de las 11:30 pm a caminar, puse música y no paré hasta que sentí la boca seca y las piernas quemando, fueron un poco más de 20.000 pasos. Mi mente se despejó,  a ratos la vista se me empapaba y callaba esos pensamientos acelerando el paso, trotando.

Desde que te fuiste vi algunas películas y sobretodo no paro de escuchar música, de cierta forma el romperme los oídos me ayuda en el proceso. Slowdive, Deftones, The Smiths, The Marias, Cigarettes After Sex, Joy Division y sobretodo Radiohead -me encanta Radiohead- especialmente “How to Disappear Completely”, “Let Down”y “Street Spirit”, también disfruto mucho “Phantom Bride” y “Rosemary” de Deftones. Mi favorita de Cigarettes After Sex es “Crush”.

No puedo dormir, no quiero soñar ni que exista silencio, acelero el tap del teclado para huir de esos flashes, es inútil. Otra vez huí de mis responsabilidades, ya no quiero seguir con esto, la tos no se me pasa.

Estoy tan flaco, siempre quise ser así, pero no me voy a conformar, quiero el cuerpo que siempre quise darte. Perdí el apetito, el sentido del gusto, eso ayuda y espero me dure lo suficiente para un verano sin polera (?).

Ya me está dando sueño, hoy vienen mis amigos a tomar, pero yo no pienso hacerlo. Temo por mis riñones y quiero seguir bajando de peso. Mañana mi abuela hará empanadas, pensé en decirle que no, odio comer.

No quiero que llegue el 18, no quiero que vuelva a pasar lo de la fonda, tengo celos pero ya no somos nada. Sin más que contarte, dejo esta carta por aquí.
"""

cards = [
    {"id": make_id("16-09-2025"), "title": "16-09-2025", "content": card_18},
    {"id": make_id("fin"), "title": "fin", "content": card_19},
    {"id": make_id("17-09-2025"), "title": "17-09-2025", "content": card_20},
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
