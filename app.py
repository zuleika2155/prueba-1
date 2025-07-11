# ESInformación: Aplicación Streamlit interactiva
import streamlit as st

# Configuración general
st.set_page_config(page_title="ESInformación 🧠💬", page_icon="🌈", layout="centered")

# Estilos
st.markdown("""
    <style>
    .titulo {
        font-size: 2.2em;
        font-weight: bold;
        color: #eb8ec7;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitulo {
        font-size: 1.3em;
        color: #4b0082;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #ffea7d;
        color: black;
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
        border: 2px solid #eb8ec7;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<div class="titulo">🌈 ¡Bienvenidx a <i>ESInformación</i>! 🧠💬</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Un espacio seguro para aprender sobre Educación Sexual Integral (ESI)</div>', unsafe_allow_html=True)
print("La Educación Sexual Integral busca brindar a los estudiantes información confiable sobre su cuerpo, la sexualidad y la afectividad, para que puedan tomar decisiones libres y responsables.")
print("Promueve el respeto por uno mismo y por los demás, fomenta relaciones sanas y equitativas, y ayuda a prevenir la violencia, los embarazos no deseados y las infecciones de transmisión sexual.")
print("Además, enseña a valorar la diversidad, cuestionar estereotipos de género y fortalecer la autoestima, el autocuidado y la autoafirmación.")


# Inputs iniciales
nombre = st.text_input("¿Cómo te llamas?")
edad = st.number_input("¿Cuántos años tienes?", min_value=0, step=1, key="edad")

if nombre and edad:
    if edad < 18:
        st.info(f"¡Perfecto, {nombre}! Como eres menor de edad, usaremos un lenguaje claro y respetuoso 😊.")
    else:
        st.success(f"Gracias por confiar en nosotros, {nombre}. Esta herramienta es útil para todxs 🧡.")

    opcion = st.selectbox("¿Qué te gustaría conocer en *ESInformación*?", [
        "Selecciona una opción",
        "1. ¿Qué es la ESI?",
        "2. Métodos anticonceptivos",
        "3. Mitos y verdades",
        "4. Autocuidado digital y sexting",
        "5. Relaciones afectivas y vínculos sanos",
        "6. Identidad de género y orientación sexual"
    ])

    if opcion == "1. ¿Qué es la ESI?":
        st.header("📌 ¿Qué es la ESI?")
        st.write("""
La Educación Sexual Integral, más conocida como la ESI, es un programa del MINEDU que busca brindar información, habilidades y valores a estudiantes para que puedan tomar decisiones informadas, saludables y responsables sobre su sexualidad.

Tiene carácter de prevenir/reducir embarazos adolescentes, violencia sexual, uniones tempranas y problemas de salud relacionados.

Además, no solo está dirigida a estudiantes, sino también a docentes y familiares, mediante acciones formativas, preventivas y de fortalecimiento de capacidades.
        """)

    elif opcion == "2. Métodos anticonceptivos":
        st.header("📌 Métodos Anticonceptivos")
        st.markdown("""
        A continuación, verás los métodos anticonceptivos más comunes. Haz clic en cada uno para ver su información completa.
        """)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🧴 Condón"):
                st.image("https://www.salud.mapfre.es/media/2021/04/condon.jpg", width=300)
                st.write("""
✅ **Condón**
- Brinda doble protección: contra embarazos no planificados y contra ITS, incluyendo VIH.
- Debe colocarse antes del acto sexual.
- Eficacia: masculino 85%, femenino 79% en uso común.
""")

            if st.button("💊 Pastillas anticonceptivas"):
                st.image("https://cdn.pixabay.com/photo/2018/04/24/16/58/pill-3348198_960_720.jpg", width=300)
                st.write("""
✅ **Pastillas anticonceptivas**
- Método hormonal diario que inhibe la ovulación y espesa el moco cervical.
- Eficacia del 99.7% si se usa correctamente.
- También protege contra algunos tipos de cáncer.
""")

            if st.button("💉 Inyecciones"):
                st.image("https://www.gob.pe/institucion/minsa/noticias/489497-uso-de-inyectables-anticonceptivos-es-una-alternativa-segura-para-prevenir-embarazos-no-deseados", width=300)
                st.write("""
✅ **Inyecciones**
- Detienen la ovulación. Existen versiones mensuales y trimestrales.
- Eficacia mensual 99.5%, trimestral 99.7%.
- Se aplican en centros de salud.
""")

        with col2:
            if st.button("📍 Implante subdérmico"):
                st.image("https://www.nexplanonusa.com/assets/images/nx_diagram_2.png", width=300)
                st.write("""
✅ **Implante subdérmico**
- Pequeña varilla bajo la piel del brazo. Libera hormonas y protege hasta 3 años.
- Eficacia del 99.95%.
- Puede afectar el ciclo menstrual.
""")

            if st.button("⚙️ SIU - Sistema intrauterino hormonal"):
                st.image("https://www.healthychildren.org/SiteCollectionImagesArticleImages/IUD.jpg", width=300)
                st.write("""
✅ **SIU - Sistema intrauterino hormonal**
- Dispositivo que se coloca en el útero y libera hormonas. Protege hasta 5 años.
- Eficacia del 99.5%.
- Colocación y retiro por profesional de salud.
""")

            if st.button("🧲 DIU - Dispositivo intrauterino de cobre"):
                st.image("https://www.plannedparenthood.org/uploads/filer_public_thumbnails/filer_public/55/40/554029cd-066e-4d9e-873d-bc35283f9628/iud_illustration.jpg__800x600_q85_crop_subsampling-2.jpg", width=300)
                st.write("""
✅ **DIU - Dispositivo intrauterino de cobre**
- Pequeño dispositivo sin hormonas que previene la fecundación. Dura hasta 12 años.
- Eficacia del 99.4%.
- No interfiere con el acto sexual.
""")

            if st.button("🚨 AOE - Anticoncepción Oral de Emergencia"):
                st.image("https://cdn.pixabay.com/photo/2017/08/06/12/39/contraceptive-2595580_1280.jpg", width=300)
                st.write("""
✅ **Anticoncepción oral de emergencia (AOE)**
- Uso solo en emergencias.
- Hasta 72 horas después del acto sexual sin protección.
- Eficacia de hasta 95%, cuanto antes se use, mejor.
- No es un método regular.
""")

# Pie
st.markdown("""
---
<center>Gracias por usar <b>ESInformación</b> 💜</center>
""", unsafe_allow_html=True)

    elif opcion == "3. Mitos y verdades":
        st.header("🎮 Juguemos: ¿Mito o Verdad?")
        preguntas = [
            ("La educación sexual en la escuela interfiere con la educación que los padres y madres brindan en el hogar", "mito", "La educación sexual integral no interfiere con la educación previa que nuestros padres y madres nos ofrecen, sino que por el contrario, la labor de padres y profesores se complementa para asegurar una formación integral."),
            ("Hablar de sexo incita a los adolescentes a tener relaciones.", "mito", "Está demostrado que la ESI retrasa el inicio sexual y mejora la toma de decisiones, además ayuda a crecer en conocimiento y valores para vivir la sexualidad con bienestar."),
            ("Hay adultos quienes no tuvieron previa enseñanza sobre la sexualidad, aprendieron solos y les fue bien", "mito", "Estas son personas que no tuvieron la oportunidad de recibir información integral en la escuela, ello ha generado diversas dudas que les impide disfrutar su sexualidad plenamente. Por ello es importante hablar sobre la ESI."),
            ("La ESI habla sobre identidad de género u orientación sexual en la escuela, sin determinar la sexualidad de las personas", "verdad", "Verdad, pues enseña a no discriminar y a valorar la diversidad que hay a nuestro alrededor.")
        ]
        for i, (preg, rpta, expl) in enumerate(preguntas, 1):
            user = st.radio(f"{i}. {preg}", ["mito", "verdad"], key=f"m{i}")
            if user:
                if user == rpta:
                    st.success("✔️ ¡Correcto!")
                else:
                    st.error("❌ Incorrecto")
                st.info(expl)

    elif opcion == "4. Autocuidado digital y sexting":
        tema = st.selectbox("Selecciona un tema:", [
            "¿Qué es el sexting?",
            "Cómo evitar ser víctima de la difusión de material íntimo",
            "Responsabilidad legal ante estas acciones",
            "Recursos y ayuda"
        ])
        contenidos = {
            "¿Qué es el sexting?": "Es el intercambio de imágenes o videos de contenido sexual a través de mensajes como WhatsApp o redes sociales. Puede ser una práctica peligrosa, especialmente para menores de edad, ya que puede derivar en abuso sexual. Podemos decir que no es nada siempre y cuando haya consentimiento de la persona, sin embargo, acosar o presionar constantemente a alguien para que le envíe una foto o un vídeo desnudo sí es ilegal.",
            "Cómo evitar ser víctima de la difusión de material íntimo": "Ello trae consecuencias como la violación de nuestros derechos a la privacidad, libertad de expresión y derechos sexuales. Evalúa muy bien con quién compartes tus fotos o videos. Una vez que lo envías, pierdes el control. Si recibes contenido íntimo con consentimiento, no lo reenvíes. Si es sin consentimiento, elimínalo inmediatamente.",
            "Responsabilidad legal ante estas acciones": "Según el Código Penal, la pena puede ser de 2 a 5 años de cárcel y de 30 a 120 días multa. Si quien difunde el contenido ha tenido una relación con la víctima, la pena va de 3 a 6 años y de 180 a 365 días multa.",
            "Recursos y ayuda": "Puedes denunciar reuniendo pruebas ante la División de Investigación de Delitos de Alta Tecnología (Divindat) de la PNP. Llama gratis al 1818 o al (01) 431-8898, escribe a divindat.depcpi@policia.gob.pe o acude a la Dirincri (Av. España 323, Lima)."
        }
        st.write(contenidos[tema])

    elif opcion == "5. Relaciones afectivas y vínculos sanos":
        pareja = st.radio("¿Tienes pareja?", ["sí", "no"])
        if pareja == "sí":
            st.write("Gracias por compartirlo 💖. Ahora exploraremos cómo construir relaciones sanas.")
        else:
            st.write("¡Perfecto! También es importante aprender sobre vínculos sanos para relaciones futuras 💬.")

        tema = st.selectbox("Selecciona un tema:", [
            "Distinguir amor, atracción y deseo",
            "¿Qué es el amor?",
            "Señales de relaciones tóxicas",
            "¿Estoy en una relación tóxica?"
        ])
        if tema == "Distinguir amor, atracción y deseo":
            st.write("""
El deseo sexual, también conocido como libido o lujuria, es la primera etapa del amor en pareja. Se caracteriza por una fuerte atracción física y el interés en mantener relaciones sexuales. Esta fase está impulsada por las hormonas sexuales: la testosterona y los estrógenos.

La segunda fase del amor de pareja es la atracción romántica o el enamoramiento, y está dominada por tres sustancias clave: la dopamina, la norepinefrina y la serotonina. Estas dos hormonas generan sensaciones de euforia, entusiasmo, energía, y pueden causar una disminución del apetito y del sueño.

El amor es un sentimiento profundo que implica una conexión emocional, física y espiritual.
""")
        elif tema == "¿Qué es el amor?":
            st.write("""
Es un sentimiento profundo y complejo que se experimenta hacia otra persona, uno mismo o algo que nos apasiona. Implica una conexión emocional, física y espiritual que nos hace sentir felices, plenos y realizados.
""")
        elif tema == "Señales de relaciones tóxicas":
            st.write("""
- Control y desconfianza: necesidad de saber dónde estás todo el tiempo.
- Manipulación emocional: frases como “si me amaras, lo harías”.
- Comunicación tóxica: sarcasmo, crítica constante, silencio como castigo.
- Ignorar tus propias necesidades: cambiar tu comportamiento por miedo.
- Minimizar tus emociones: frases como “eso no es nada” o “te quejas por gusto”.
""")
        elif tema == "¿Estoy en una relación tóxica?":
            st.write("""
Reflexiona con estas preguntas:
- ¿Tu pareja apoya tus metas o las ridiculiza?
- ¿Sientes que nunca es suficiente lo que haces?
- ¿Te has alejado de tus amigos o familia?
- ¿Se burla de tus gustos?
- ¿Usa el chantaje emocional?
- ¿Te exige explicaciones todo el tiempo?
- ¿Toma decisiones sin consultarte?

Si varias respuestas te incomodan, podrías estar en una relación tóxica. Hablar con un profesional puede ayudarte.
""")

    elif opcion == "6. Identidad de género y orientación sexual":
        tema = st.selectbox("Selecciona un tema:", [
            "¿Qué es el sexo?",
            "¿Qué es el género?",
            "¿Qué es la identidad de género?",
            "¿Qué es la orientación sexual?"
        ])
        respuestas = {
            "¿Qué es el sexo?": "Es la etiqueta que se nos asigna al nacer, generalmente por un doctor, basándose en nuestros genitales y cromosomas. Se registra en el certificado de nacimiento como masculino o femenino.",
            "¿Qué es el género?": "Es una construcción legal, social y cultural, que establece normas, expectativas y roles sobre cómo deben comportarse las personas según su sexo asignado.",
            "¿Qué es la identidad de género?": "Es cómo cada persona se siente y se percibe a sí misma en relación con el género. Se expresa a través de la ropa, el lenguaje corporal, la forma de hablar o presentarse, y puede coincidir o no con el sexo asignado al nacer.",
            "¿Qué es la orientación sexual?": "Es una atracción emocional, romántica, sexual o afectiva duradera hacia otros. Entre las más comunes están la homosexualidad, bisexualidad, asexualidad."
        }
        st.write(respuestas[tema])

# Pie
txt = """
<hr>
<div style='text-align:center;'>
Gracias por usar <b>ESInformación</b> 💜
</div>
"""
st.markdown(txt, unsafe_allow_html=True)
