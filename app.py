# ESInformación: Aplicación Streamlit interactiva
import streamlit as st

# Configuración general
st.set_page_config(page_title="ESInformación 🧠💬", page_icon="🌈", layout="centered")

# Estilos personalizados
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

# Presentación de la ESI
st.write("""
La Educación Sexual Integral busca brindar a los estudiantes información confiable sobre su cuerpo, la sexualidad y la afectividad, para que puedan tomar decisiones libres y responsables.

Promueve el respeto por uno mismo y por los demás, fomenta relaciones sanas y equitativas, y ayuda a prevenir la violencia, los embarazos no deseados y las infecciones de transmisión sexual.

Además, enseña a valorar la diversidad, cuestionar estereotipos de género y fortalecer la autoestima, el autocuidado y la autoafirmación.
""")

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

    # Secciones temáticas
    if opcion == "1. ¿Qué es la ESI?":
        st.header("📌 ¿Qué es la ESI?")
        st.write("""
La Educación Sexual Integral, más conocida como la ESI, es un programa del MINEDU que busca brindar información, habilidades y valores a estudiantes para que puedan tomar decisiones informadas, saludables y responsables sobre su sexualidad.

Tiene como objetivos prevenir/reducir embarazos adolescentes, violencia sexual, uniones tempranas y problemas de salud relacionados.

Además, no solo está dirigida a estudiantes, sino también a docentes y familiares, mediante acciones formativas, preventivas y de fortalecimiento de capacidades.
        """)

elif opcion == "2. Métodos anticonceptivos":
    st.header("📌 Métodos Anticonceptivos")
    st.markdown("Haz clic para conocer más sobre cada método:")

    metodos = {
        "🧴 Condón": {
            "img": "https://www.salud.mapfre.es/media/2021/04/condon.jpg",
            "desc": """
**Condón**  
- Doble protección: embarazo e ITS.  
- Uso externo.  
- Masculino 85%, femenino 79% (uso común)."""
        },
        "💊 Pastillas anticonceptivas": {
            "img": "https://cdn.pixabay.com/photo/2018/04/24/16/58/pill-3348198_960_720.jpg",
            "desc": """
**Pastillas anticonceptivas**  
- Diarias.  
- 99.7% eficacia (uso correcto).  
- Regulan el ciclo y reducen algunos riesgos de cáncer."""
        },
        "💉 Inyecciones": {
            "img": "https://cdn.pixabay.com/photo/2020/05/19/19/39/syringe-5193891_1280.jpg",
            "desc": """
**Inyecciones**  
- Mensuales o trimestrales.  
- 99.5% – 99.7% de eficacia.  
- Aplicación en centro de salud."""
        },
        "📍 Implante subdérmico": {
            "img": "https://www.nexplanonusa.com/assets/images/nx_diagram_2.png",
            "desc": """
**Implante subdérmico**  
- Varilla en el brazo.  
- Hasta 3 años.  
- 99.95% eficacia."""
        },
        "⚙️ SIU Hormonal": {
            "img": "https://www.healthychildren.org/SiteCollectionImagesArticleImages/IUD.jpg",
            "desc": """
**SIU Hormonal**  
- Dentro del útero.  
- Libera hormonas por 5 años.  
- 99.5% eficaz."""
        },
        "🧲 DIU de cobre": {
            "img": "https://www.plannedparenthood.org/uploads/filer_public_thumbnails/filer_public/55/40/554029cd-066e-4d9e-873d-bc35283f9628/iud_illustration.jpg__800x600_q85_crop_subsampling-2.jpg",
            "desc": """
**DIU de cobre**  
- Sin hormonas.  
- Protege hasta 12 años.  
- 99.4% eficaz."""
        },
        "🚨 AOE": {
            "img": "https://cdn.pixabay.com/photo/2017/08/06/12/39/contraceptive-2595580_1280.jpg",
            "desc": """
**AOE (pastilla de emergencia)**  
- Solo para emergencias.  
- Hasta 72h después.  
- 95% eficaz si se toma pronto."""
        }
    }

    for metodo, info in metodos.items():
        with st.expander(metodo):
            st.image(info["img"], use_column_width=True)
            st.markdown(info["desc"])


elif opcion == "3. Mitos y verdades":
    st.header("🎮 ¿Mito o Verdad?")
    st.write("Responde cada afirmación. Luego de responder, verás la explicación.")

    preguntas = [
        {
            "preg": "La educación sexual en la escuela interfiere con lo que enseñan en casa.",
            "rpta": "mito",
            "exp": "La ESI complementa lo aprendido en familia.",
            "img": "https://cdn-icons-png.flaticon.com/512/3839/3839959.png"
        },
        {
            "preg": "Hablar de sexualidad hace que los adolescentes tengan más relaciones sexuales.",
            "rpta": "mito",
            "exp": "Está demostrado que la ESI retrasa el inicio sexual.",
            "img": "https://cdn-icons-png.flaticon.com/512/2124/2124516.png"
        },
        {
            "preg": "La ESI enseña sobre identidad de género sin imponer orientación.",
            "rpta": "verdad",
            "exp": "La ESI enseña a no discriminar y valorar la diversidad.",
            "img": "https://cdn-icons-png.flaticon.com/512/3613/3613273.png"
        }
    ]

    for i, item in enumerate(preguntas, 1):
        st.markdown(f"**{i}. {item['preg']}**")
        st.image(item["img"], width=100)
        respuesta = st.radio("Elige una opción:", ["mito", "verdad"], key=f"mito{i}")
        if respuesta:
            if respuesta == item["rpta"]:
                st.success("✔️ ¡Correcto!")
            else:
                st.error("❌ Incorrecto")
            st.info(item["exp"])
            st.markdown("---")

    elif opcion == "4. Autocuidado digital y sexting":
        tema = st.selectbox("Selecciona un tema:", [
            "¿Qué es el sexting?",
            "Cómo evitar ser víctima de la difusión de material íntimo",
            "Responsabilidad legal ante estas acciones",
            "Recursos y ayuda"
        ])
        contenidos = {
            "¿Qué es el sexting?": "Es el intercambio de contenido íntimo. Puede ser riesgoso, especialmente en menores. Solo es válido si hay consentimiento.",
            "Cómo evitar ser víctima de la difusión de material íntimo": "Evalúa con quién compartes. Si recibes algo íntimo sin consentimiento, elimínalo.",
            "Responsabilidad legal ante estas acciones": "La pena puede ser de 2 a 6 años de prisión. Depende del vínculo con la víctima.",
            "Recursos y ayuda": "Llama gratis al 1818 o (01) 431-8898. También puedes escribir a divindat.depcpi@policia.gob.pe"
        }
        st.write(contenidos[tema])

    elif opcion == "5. Relaciones afectivas y vínculos sanos":
        pareja = st.radio("¿Tienes pareja?", ["sí", "no"])
        st.write("Gracias por compartir 💖" if pareja == "sí" else "¡Perfecto! También es útil para el futuro 💬.")

        tema = st.selectbox("Selecciona un tema:", [
            "Distinguir amor, atracción y deseo",
            "¿Qué es el amor?",
            "Señales de relaciones tóxicas",
            "¿Estoy en una relación tóxica?"
        ])
        respuestas = {
            "Distinguir amor, atracción y deseo": "El deseo es físico; la atracción, emocional; y el amor, un compromiso profundo.",
            "¿Qué es el amor?": "Una conexión emocional, física y espiritual que genera bienestar y realización.",
            "Señales de relaciones tóxicas": "- Control\n- Manipulación\n- Crítica constante\n- Aislamiento\n- Minimización de tus emociones",
            "¿Estoy en una relación tóxica?": "Hazte preguntas como: ¿Me apoya? ¿Respeta mis decisiones? ¿Puedo ser yo misma/o/x? Si dudas, busca ayuda."
        }
        st.write(respuestas[tema])

    elif opcion == "6. Identidad de género y orientación sexual":
        tema = st.selectbox("Selecciona un tema:", [
            "¿Qué es el sexo?",
            "¿Qué es el género?",
            "¿Qué es la identidad de género?",
            "¿Qué es la orientación sexual?"
        ])
        respuestas = {
            "¿Qué es el sexo?": "Es la asignación al nacer basada en genitales y cromosomas.",
            "¿Qué es el género?": "Es una construcción social sobre roles y expectativas.",
            "¿Qué es la identidad de género?": "Es cómo una persona se siente y se expresa respecto al género.",
            "¿Qué es la orientación sexual?": "Es la atracción emocional, sexual o afectiva hacia otros."
        }
        st.write(respuestas[tema])

# Pie de página
st.markdown("""
<hr>
<div style='text-align:center;'>
Gracias por usar <b>ESInformación</b> 💜
</div>
""", unsafe_allow_html=True)
