import re
import html as html_lib
import streamlit as st

def make_id(title):
    return "card-" + re.sub(r'[^0-9a-zA-Z\\-]+', '-', title)

card_18 = """Si amas algo déjalo ir, es cierto. No mandaré más mensajes, desapareceré de tu vida y lidiaré con verte en los lugares que ambos frecuentamos. Te dejaré ir y espero que vuelvas, espero seas feliz sin mí, pero yo sería el doble de feliz si es conmigo.

No me quejaré más, no habrá más lamentos ni palabras tristes, aunque el tono de estas cartas siempre será el que es. Quisiera saber cómo estás, quisiera hablar con tu abuela y hacerle saber la maravillosa nieta que tiene, tan amable y sensible. Tu mamá me odiaría tanto, aunque aún no viene a tirarme de las patas y se lo agradezco, el lugar en donde está debe ser muy hermoso y pacífico, aunque no lo creas extrañaré por siempre a esa mujer.

Hoy intentaré salir a caminar, quizás no pueda, también debo entregar un informe a la agrícola de mi tesis, y es muy difícil, además, en octubre tengo mi primera prueba y soy incapaz de estudiar. Qué difícil es romper esta rutina, me consuela saber que estás mucho mejor que yo.

También debo hacer ejercicio, la falta de apetito me está quitando grasa pero también musculatura, me fuerzo a comer carne pero hace tiempo que no la disfruto, no como antes al menos. Me imagino que tengo que comer proteína, pero sigo en un déficit muy alto y el estrés no está ayudando. Siempre quise ser fuerte pero mis estúpidas rodillas me daban vergüenza, evitaba los deportes porque no podía jugar sin dolor y sin salir a quejarme por algo. Estoy haciendo calistenia ahora que cerró el gimnasio por el receso, necesito mantener el hábito y voy bien, aunque me siento muy débil aún.

Una de mis motivaciones y quizás la más grande (y estúpida) es que me veas y digas “que guapo se ve”. Siento que nunca te pude dar un cuerpo equivalente al tuyo, siempre fui bastante dejado y feo. Sigo sin tener un cuerpo hegemónico pero al menos ya no me doy asco. Olvidemos este párrafo.

Fui a ver a mi abuela el día antes de verte, no supo que decirme respecto a nuestra relación, que era muy contemporánea. Supongo que ellos se casaban y se resignaban toda la vida a ello, nunca lo entenderé. Además, pude notar como verme fumar y no comer le afectó, quizás debí mostrarme más fuerte, lo intenté.

Mi mamá también escribió, pero le dije que no podía confiar en ella (con un perdón posterior) ¿Sabías que nunca aportó económicamente? Me parece muy fuerte, sabía que fue mala madre pero pensé que al menos le daba una cantidad mínima de plata a mis abuelos. Siempre escuché que me abandonó, pero yo elegía pensar que estábamos peleados, de hecho, prefiero creer eso.

Cómo puedo hablar de ti si ya no sé nada. Me alegro mucho de que vayas a ver a Sabrina, es algo muy impresionante, pero me da celos que te vayan a ver tantos hombres (sí), incluso me da celos que te hable el weon del programa de citas, csm por favor no lo hagas, y ni hablemos del depredador.

Quitemos las bromas (no tan bromas), saber que ya no me amas es duro y escribirte los párrafos más depresivos no es la idea. Objetivamente te superaré, entendiéndolo como poder tener una vida sin depender de ti, actualmente me es imposible, renunciaré al doctorado. No tiene caso seguir la vida que tenía planeada contigo, voy a llorar y seguir llorando y quizás vaya al psicólogo.

No quiero que me olvides, porque eso implica perderte para siempre, perderte al nivel más ínfimo de humanidad.

PD: Iré borrando las cartas antiguas, las conservaré para mí, se que ya no me amas, se que no las guardarás. Tengo miedo de que me odies, tengo miedo de tu rencor, no me destruyas por favor.
"""
card_19 ="""Esta carta es dura y no fue mi intención hacerla así, pero si el haberme amado no te hace recapacitar en tus acciones me sale esto:

Nadie que no sea un infiel o un abusador mental/físico merece que lo terminen, es un acto de crueldad, inmadurez y/o simplemente falta de amor.

Me dejaste de amar por mi actitudes, está bien, no quisiste arreglar las cosas, entonces tu amor nunca fue tan inmenso como creías. Es hiriente, y tus canciones me confirman que tu intención fue herirme, yo te doy asco y lo comprendo, pero no lo comparto. No importa lo mucho que intentes justificarte, me prometiste amor incondicional y lo rompiste, tú sabes que pudimos solucionarlo como muchas cosas antes, pero elegiste abandonarme. 

Es cierto, todos merecemos sentirnos felices y realizados, pase lo que pase. Si cometiste errores, puedes aprender de ellos. En el futuro, no los vas a repetir cuando importe, pero ese es el punto, dejé de importarte, dejaste de amarme y me obligaste a leer tu carta de despecho, muy distinta a la mía.

Ya no hay nada más que hablar, te di la despedida más gentil y llena de amor, pero tu cortaste al escucharme decir “Ok, se acabó” ¿Por qué? Porque no me amas. 

Lamentablemente no pudiste cerrar este ciclo en buenos términos, tus palabras fueron vacías y te picaban las manos por deshacerte de mí o de esa llamada. Encontraré a alguien que sea el amor de mi vida, y seré mucho mejor pareja a diferencia de ti, porque yo me humillé por amor, porque luché por saber lo que pasó y cómo mejorar. No es un ataque por Dios, tu no eres una santa.

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
