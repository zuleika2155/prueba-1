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
        st.markdown("A continuación, verás los métodos anticonceptivos más comunes. Haz clic en cada uno para ver su información completa.")

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

    elif opcion == "3. Mitos y verdades":
        st.header("🎮 Juguemos: ¿Mito o Verdad?")
        preguntas = [
            ("La educación sexual en la escuela interfiere con la educación que los padres y madres brindan en el hogar", "mito", "La ESI complementa la educación familiar."),
            ("Hablar de sexo incita a los adolescentes a tener relaciones.", "mito", "La ESI retrasa el inicio sexual y mejora la toma de decisiones."),
            ("Hay adultos quienes no tuvieron enseñanza sobre la sexualidad y les fue bien", "mito", "La falta de información integral genera dudas e inseguridad."),
            ("La ESI habla sobre identidad de género sin imponer la sexualidad", "verdad", "Verdad: enseña a no discriminar y valorar la diversidad.")
        ]
        for i, (preg, rpta, expl) in enumerate(preguntas, 1):
            user = st.radio(f"{i}. {preg}", ["mito", "verdad"], key=f"m{i}")
            if user:
                st.success("✔️ ¡Correcto!") if user == rpta else st.error("❌ Incorrecto")
                st.info(expl)

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
