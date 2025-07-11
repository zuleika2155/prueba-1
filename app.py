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
st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)

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
            La Educación Sexual Integral (ESI) es un programa educativo que busca brindar información,
            habilidades y valores para tomar decisiones saludables y responsables sobre la sexualidad.
            También involucra a docentes y familias para formar una comunidad educativa informada.
        """)

    elif opcion == "2. Métodos anticonceptivos":
        metodo = st.selectbox("Selecciona un método para conocer más:", [
            "Condón", "Pastillas anticonceptivas", "Inyecciones", "Implante subdérmico",
            "SIU hormonal", "DIU de cobre", "Anticoncepción oral de emergencia"
        ])
        info = {
            "Condón": "Brinda doble protección: embarazo e ITS. Eficacia: 85% (masculino), 79% (femenino).",
            "Pastillas anticonceptivas": "Método hormonal diario. Eficacia: 99.7% si se usa correctamente.",
            "Inyecciones": "Versión mensual o trimestral. Eficacia: más del 99%.",
            "Implante subdérmico": "Varilla bajo la piel. Dura hasta 3 años. Eficacia: 99.95%.",
            "SIU hormonal": "Dispositivo en el útero. Dura hasta 5 años. Eficacia: 99.5%.",
            "DIU de cobre": "Dispositivo sin hormonas. Dura hasta 12 años. Eficacia: 99.4%.",
            "Anticoncepción oral de emergencia": "Se toma hasta 72 horas después. Eficacia: hasta 95%."
        }
        st.info(info[metodo])

    elif opcion == "3. Mitos y verdades":
        st.header("🎮 Juguemos: ¿Mito o Verdad?")
        preguntas = [
            ("La ESI interfiere con la educación del hogar.", "mito",
             "La ESI complementa la educación familiar, no la reemplaza."),
            ("Hablar de sexo incita a tener relaciones sexuales.", "mito",
             "La ESI retrasa el inicio sexual y promueve decisiones informadas."),
            ("La ESI enseña sobre diversidad sin imponer identidades.", "verdad",
             "Promueve respeto y no impone ningún tipo de orientación o identidad.")
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
            "Cómo evitar la difusión de material íntimo",
            "Responsabilidad legal",
            "Recursos y ayuda"
        ])
        contenidos = {
            "¿Qué es el sexting?": "Es compartir imágenes sexuales por redes. Puede ser riesgoso sin consentimiento.",
            "Cómo evitar la difusión de material íntimo": "Evalúa a quién le compartes contenido. Una vez enviado, pierdes control.",
            "Responsabilidad legal": "Difundir imágenes sin permiso puede tener penas de 2 a 6 años de cárcel.",
            "Recursos y ayuda": "Puedes llamar al 1818, escribir a divindat.depcpi@policia.gob.pe o acudir a la Dirincri."
        }
        st.write(contenidos[tema])

    elif opcion == "5. Relaciones afectivas y vínculos sanos":
        pareja = st.radio("¿Tienes pareja?", ["sí", "no"])
        st.write("Aprendamos más sobre vínculos saludables:")
        tema = st.selectbox("Selecciona un tema:", [
            "Amor, atracción y deseo",
            "¿Qué es el amor?",
            "Relaciones tóxicas",
            "¿Estoy en una relación tóxica?"
        ])
        if tema == "Amor, atracción y deseo":
            st.write("El deseo es atracción física; la atracción, emoción intensa; el amor, conexión profunda.")
        elif tema == "¿Qué es el amor?":
            st.write("Es un sentimiento complejo que implica respeto, afecto y conexión emocional.")
        elif tema == "Relaciones tóxicas":
            st.write("Señales: control, manipulación, invalidación emocional, cambios forzados.")
        elif tema == "¿Estoy en una relación tóxica?":
            st.write("Reflexiona: ¿Te sientes libre? ¿Apoyadx? ¿Validadx? Si no, podrías necesitar ayuda profesional.")

    elif opcion == "6. Identidad de género y orientación sexual":
        tema = st.selectbox("Selecciona un tema:", [
            "¿Qué es el sexo?",
            "¿Qué es el género?",
            "¿Qué es la identidad de género?",
            "¿Qué es la orientación sexual?"
        ])
        respuestas = {
            "¿Qué es el sexo?": "Etiqueta asignada al nacer según genitales y cromosomas (masculino/femenino).",
            "¿Qué es el género?": "Construcción social y cultural que define roles y expectativas según el sexo asignado.",
            "¿Qué es la identidad de género?": "Es cómo una persona se percibe internamente. Puede coincidir o no con su sexo asignado.",
            "¿Qué es la orientación sexual?": "Atracción emocional, romántica o sexual hacia otras personas. Ej: bisexualidad, asexualidad."
        }
        st.info(respuestas[tema])

# Pie
st.markdown("""
<hr>
<div style='text-align:center;'>
Gracias por usar <b>ESInformación</b> 💜
</div>
""", unsafe_allow_html=True)
