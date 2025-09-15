import re
import html as html_lib
import streamlit as st

def make_id(title):
    return "card-" + re.sub(r'[^0-9a-zA-Z\\-]+', '-', title)

card_13 = """Hablé contigo, cuanto hubiese querido que fuera en persona, pero el ruido en mi cabeza no me daba paz. Quiero morir, nunca he estado peor en mi vida, perdí a la mujer de mi vida por ser inmaduro, en todo aspecto.

De cierta forma obtuve alivio con esa charla, pero la indiferencia y el resentimiento que coseché me revuelven el estomago y aprietan mi pecho profundamente. Es mi culpa, cuanto quisiera decir que no lo es: que no es de nadie, pero es mía.

Me arrepiento no haber estado para ti, porque si hubiese podido comunicarme no te habría perdido, al menos en el sentimiento. Porque te amo más que a nadie en el mundo, más que a mis padres, más que a mis abuelos, y te amaría más que a un hijo. El peor error de mi vida fue perderte y no solo eso, sino que las peores palabras las escuchaste de la persona que aún amabas, jamás voy a perdonarme a mí mismo, pero cuanto desearía que tu me perdonaras, porque aún no estoy seguro si lo hiciste.

Puedo dejar de mentir, porque no hay nada que conservar. Tuve pensamientos fugaces de terminar todo, por priorizar mi futuro, pero tonto yo que no entendí hasta hace unos meses que mi carrera solo es un medio para conseguir la felicidad, la felicidad que pude haber tenido contigo. Lo intenté todo porque no quería que nos separáramos, tuve charlas de noches enteras con muchos de mis amigos y aunque a veces no encontraba respuestas en otras ocasiones algo escuchaba en mi interior: que debía luchar por ti y quedarme a tu lado hasta el día de mi muerte, en ese proceso sentí tu indiferencia, y me carcomía sin encontrarle un sentido.

Muchas veces en la U y en privado hablaba del miedo que tenía por perderte. Me aterraba y ahora veo que en algo yo, si tenía la razón.

Es cierto, dije que eres un desastre, no te conocí así y entiendo que las circunstancias de la vida te metieron en un hoyo que cualquiera caería, siempre lo supe, siempre te entendí. Más aún ahora con la muerte de la mamá del Joaquín, a quien acompañé tal como lo hice contigo. Intenté seguir a tu lado, pero entiendo el asco que sentías hacia mí, traicioné tu confianza y no hay ninguna excusa que valga.

Dios sabe cuanto te amo y como jamás te olvidaré, no importa lo que pase, mi primer y único amor, la mujer que me enseñó que a amar y que te amen. Como quisiera haber luchado no solo en lo práctico, sino también en lo emocional, tener las herramientas necesarias y hacerte sentir amada, por todo el cariño que puedo darte, que no fue entregado.

No te escribí ni llamé por verte con alguien más, colapsé en llanto mucho antes ese día, ni siquiera te había visto. De todas formas es un dolor inimaginable.

Lamento terminar esta carta de esta manera, pero ya no hay forma de expresar el real cariño y amor que tengo por ti. Me niego a despedirme.
"""

card_14 = """Nada de lo que me digas me quita de la cabeza que eres el amor de mi vida, aunque entendí muchas cosas. Ni siquiera se si alguna vez verás estas cartas, porque no planeo avisarte de ellas, decidiste alejarte de mí y lo entiendo.

Otra vez me congelé, quise despedirme pero nuevamente, no sabía cómo. Las lágrimas se secan y sedimentan en mis lentes de sol, que debo lavar diariamente, de cierta forma me gusta ocultar parte del sufrimiento cuando me veo al espejo.

Quisiera contarte toda mi vida, todo lo que cambié, mejoré y mejoraré. Se supone que el sufrimiento de una ruptura se sana con tiempo y canalización en cosas de provecho hacia uno mismo, pero estoy acostumbrado a vivir por ti aunque así no lo veas, es así como puedo sobrevivir, es el propósito de mi  vida. 

Ya no hay nada nuevo que sepa lamentar, pero el dolor no se irá. No quiero dejarte ni en lo físico ni en lo emocional, seguiré diciendo “te amo antonia” repetidamente en mi cabeza, en voz alta, como se me ocurra en el momento.

Hasta el sentimiento de compartir un asiento en la micro lo extraño, sentir tu presencia y calidez, de apoyarte en mi hombro, y lamentablemente me recuerda a como nos encerrábamos en mi casa. Hoy tengo el tiempo libre de estar solo, de no estudiar, el conocimiento de mi pequeño mundo para poder llevarte a donde sea. Es algo que llegó a mi vida no por perderte, sino el hablar contigo.

Estoy en mi casa y aún siento un poco de tu aroma perdiéndose en mi chaqueta, cada cigarro es un recuerdo nuestro que consumo, y el sentir el sabor de la colilla quemándose el recuerdo de que las cosas terminaron. En esencia el cigarro es el mismo, y no quiero otros.

Las plantas brotan y muchos dicen que el amor es hormonal, pero el crecimiento de estas y especialmente en frutales es algo que perdura, los protegen y dan sostén a nuevos tejidos. Es cierto, es hormonal, pero gracias a eso llegan a la luz, gracias a eso despiertan después de un horrible invierno, floreciendo. Cuanto me gustaría verte florecer y me duele tanto que te hayas privado de ello, cuando era mi mayor deseo.

Florece, vuelve a mí, vuelve a mí de la manera que quieras. Quédate conmigo.

PD: Acaba de ganar la U 3-0 al colo, no siento nada xd.
"""

card_15 = """Sigo ejercitándome, quiero ser fuerte, lo suficiente para que pueda parecerte atractivo, porque decirme eso fue humillarme, yo no me rindo. Es difícil, tengo dos motivaciones: estar en mi cama y trabajar mi cuerpo, ambas me atraen pero son incompatibles.

Es complejo dormir, tengo pensamientos que no callan ni con la canción más destroza oídos que pueda encontrar. Quiero apagarlo y despertar contigo, amo dormir, recostarme y escuchar música hasta que me retumben los oídos y ahogar irónicamente el tinnitus que cada vez empeora. Al despertar veo las instantáneas que tomé con la polaroid, mi rostro con genuina felicidad, las flores y las energéticas de nuestras noches de estudio (no estudiamos tanto).

Cómo se le envían flores a alguien que no quiere estar conmigo, son las flores las que te gustan o es el detalle acaso, podrían ser ambas y es lo más probable. Pero que caso tiene, es patético y un mal recuerdo, algo que debí haber hecho antes. Siempre tuve una excusa y me consuela que prioricé tu bienestar, pero descuidé el romanticismo o la emoción y es tan triste.

Algo que contribuyó al bloqueo emocional que tuve fue que quería seguir a tu lado, pero acabó y hasta hace no mucho no entendía por qué, solo estaba seguro que te aburriste de mí y ya no me amabas. Saber lo que pasó me reconforta en el sentido de que ya no existe la injusticia, sino el entendimiento y el deseo de mejorar, pero pega tan fuerte que quieras o esperes que mejore para la próxima persona. Odio a esa persona, no la conozco y la detesto, porque significa que estaría equivocado, y estoy tan seguro que eres tú la indicada. 

Solo te amaré a ti, quizás pueda algún día volver a querer, pero nunca más voy a amar, no así. Necesito encontrar la manera de ser el indicado, el amor de tu vida, ya he comprendido cosas y estoy tan seguro que lo soy o seré. Mis bajas expectativas de que me elijas luchan contra mi único deseo de verte feliz y no seré hipócrita, porque a pesar de que es cierto, sería mucho mejor si lo fueras conmigo, en mis brazos.

Eres la mujer de mis sueños, dices que no aprecié tu amor pero es mentira. En mi cabeza fui el pololo perfecto, sabía que tenía algo mal dentro de mí pero jamás iba a permitir dañarte o que afectara a nuestra relación, esa era la idea al menos. Cuanto quisiera haber podido conversar esto antes, de la manera correcta, lo hubiese hecho todo por ti. Siempre supe que me amabas demasiado y al igual que tú pensaba que mi amor era mayor o igual, no creas lo contrario.

Hoy esa peste que tenía dentro desapareció, me comporté como un imbécil bajo la excusa de que me terminaste, que me dejaste de amar y tenía que ser feliz. No hay día que no llore la falta que me haces, estoy destrozado al punto de que no he comido absolutamente nada en todo el día. No hay mujer como tú, no hay una persona como tú, eso lo supe desde el primer día que empezamos a estar juntos.

Debí haber hecho más, siento que lo di todo pero no soy perfecto, tonto es un adjetivo corto a lo que fui, ingenuo. Tantos años sin darme cuenta y en una noche pudiste mostrarme mis bajezas y hacerme el hombre más triste del mundo, por mis acciones.
"""

card_16 = """Vuelve a quererme, vuelve a decirme por qué no pudimos hablar antes, habían soluciones. Por qué te fuiste, prometiste que no lo harías al igual que yo, prometiste amarme para siempre y ahora estás tan lejos.

Soy invisible a tus ojos, y tu eres un sol que recuerda la felicidad más grande de mi vida. Recostado en mi cama, no puedo hacer otra cosa que no sea pensar en ti, en el metro, en la micro, camino a la U, camino a mi casa, camino a la esquina, es igual. No extraño el sentimiento, extraño a la persona,  extraño tu risa y tu calor, extraño muchas cosas, extraño a mi mejor amiga, pero dejaste de serlo meses antes de terminar y cuanto dolió.

Siento que te ríes de mí, ¿por qué no pudiste empatizar conmigo? no soy un monstruo, no soy una mala persona, ¿por qué permites que me atormenten?, ¿por qué tus amigas me destrozan y no te importa? Quiero la paz que me dabas, apoyar mi cabeza en la almohada y saber que estabas ahí, saber que mi día podía ser mejor al verte otra vez. Comprender qué es para ti más de 3 años amándonos.

Es cierto, no fui el mejor pololo, lo intenté con toda mi alma y cuerpo, y es lo que me reconforta y permite que pueda pseudo-dormir. Fui incapaz de decirte mis tormentos en la relación y no seré específico, porque ya no tiene caso, no quiero recriminarte nada, sino que me entiendas. 

Siempre me sentí menos que tú, siempre sentí que la llama se apagaba y que debía reprimir mi intensidad, mis ganas de entregarte mi cariño. Nunca me sentí incluido en tu mundo, sentir el peso de la indiferencia, sentir que tus amigos y amigas me detestaban ¿Por qué debía esperar callado a que terminaras de hablar con alguien en tu celular?, ¿por qué lo hacías si estabas conmigo? Quiero respuestas que no obtuve, quiero que me retribuyas ese amor que esperaba recibir, pero ya te fuiste.

Mis amigos desde el principio quisieron incluirte, pero comprendo tú no quisiste hacerlo, no congeniaste ¿Por qué yo nunca tuve esa oportunidad, una oportunidad real? ¿Por qué tenías esos pequeños rencores random hacia mí?

Estar una relación con alguien inestable emocionalmente, con posterior depresión e inseguridades latentes es muy difícil, pero te comprendí tanto y no puedes negarlo. Me quedé en las buenas y en las malas, siempre deseando tu felicidad, porque pensé que llegaría el día en que la tormenta del inicio de la vida adulta se despejaría y pudiésemos ver la inmensidad que nos deparaba, juntos.

Quiero partir de aquí, y no quiero hacerlo solo, te necesito conmigo. Te conozco desde que era un tonto adolescente, estuve contigo días, semanas enteras, meses, donde solo nos separábamos para buscar ropa o visitar familiares ¿Qué fue lo que pasó? Me repito a mí mismo, y aunque obtengo respuestas sigo sin entender cómo podrían ser válidas para acabar así.

Jamás fuimos a Punta Arenas, ya no iremos a Europa, a algún país anglosajón. Ya no podré mostrarte esa reconfortante brisa que lo era aunque cortara mi cara o la quemara del frío en la Patagonia, ya no podré hacerlo, añorando tanto que hayas estado en esos momentos.

Dices que no soy alma gemela, tu amor real o el amor de tu vida. Pero es injusto, no conocía el mundo y ahora que conozco un poco sé que no me importa, daría todo por estar junto a ti, mi vida por tu existencia. No hay otra mujer que me interese, no hay nadie más que tú y a pesar de todo lo que tú creas, es así… Y cuán seguro estoy de ello.

No voy a renunciar a la vida que imaginé contigo, donde somos tan felices. Ahora entiendo por qué si amas debes dejar ir, porque una vez nos separamos nos damos cuenta todo lo que hicimos mal, es un golpe tan duro de realidad que refuerza mis convicciones. Especialmente la convicción de luchar por ti hasta el último de mis días, despertar y llamarte mi esposa, porque ver Orgullo y Prejuicio por más ridículo que te parezca, era fruto del arrepentimiento de negarme a verla contigo, y como desearía poder voltear a tus ojos en cada escena en que pensé en ti.
"""

card_17 ="""Hoy soñé contigo, dormíamos juntos junto a una luz morada tenue, te acurrucabas y ponía mi mano sobre tu brazo, cuando inmediatamente desperté por mi papá tocando mi puerta. No pude hacer otra cosa que irme a su pieza a seguir durmiendo e intentar volver a esa realidad, solo lo intenté.

Quisiera decirte tantas cosas pequeñas, como que tengo un yogur en el refrigerador que se está echando a perder, una pechuga de pollo que cociné ayer y no pude comer, el agua se acaba y las cosas que me fuerzo a comer no se digieren. Quién diría que yo no tendría hambre.

Esta casa es tan grande y vacía que me siento como un hámster en una jaula, tengo una televisión para ver películas, una cocina con todo lo que quiero y aquí estoy, en una cueva que llamo mi pieza. Soy un roedor herido, tan frágil, porque llamarme perro es demasiado para lo soy.

Sinceridad es la palabra de hoy y me pregunto si lo fui alguna vez con otra persona que no seas tú ¿Quién soy? Ya sé quien soy: soy un buscador, una conciencia en aprendizaje, un alma libre que obra diariamente, pero mi rol en la vida es de ser hombre, un hombre que ama incondicionalmente.

Soy tan feliz porque despejé mi mente, aunque sea parcialmente, veo la vida de otra manera, pero aún soy desdichado porque perdí mi propósito de vida. Cuán feliz sería de tenerte unos minutos en mis brazos, de volver al 13-09 a las 11:55, acariciar tu rostro y decirte lo mucho que lo siento, que te amo. Hacer que vuelvas a confiar en mí, cambiar mi rostro, ser un cuerpo nuevo del que te puedas enamorar.

No tuvimos exactamente lo que necesitábamos, pero todavía queda un largo camino, todavía nos quedan objetivos,  algunos quedaron en el camino pero siempre podremos volver a crear nuevos. Tomaré cada ladrillo y lo pondré en su lugar,  haré la estructura más fuerte que pueda conocer el mundo. Solo debes decírmelo.

Tienes el poder de destruirme, con un solo mensaje y mi garganta se cierra con solo pensarlo, ámame por favor, nunca dejes de hacerlo aunque sea un poco. Volveré a ti algún día, tocaré tus labios, tu cintura y finalmente tu frente, al igual que esa primera noche. Volveremos a bailar, a ver películas, a caminar durante el atardecer, a tomar un café.

Escríbeme, vuelve y permíteme deshacerme ante ti. Si quise dormir a tu lado, si quise que me miraras, si quise que te quedaras acurrucada en mi brazo.
"""

cards = [
    {"id": make_id("13-09-2025"), "title": "13-09-2025", "content": card_13},
    {"id": make_id("14-09-2025"), "title": "14-09-2025", "content": card_14},
    {"id": make_id("15-09-2025"), "title": "15-09-2025", "content": card_15},
    {"id": make_id("especial"), "title": "De un día cualquiera", "content": card_16},
    {"id": make_id("existencial"), "title": "Por favor", "content": card_17},
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
