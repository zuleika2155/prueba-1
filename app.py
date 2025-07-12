# ESInformación: Aplicación Streamlit interactiva
import streamlit as st

# Configuración general
st.set_page_config(page_title="ESInformación 🧠💬", page_icon="🌈", layout="centered")

# Estilos personalizados y fondo cálido
st.markdown("""
    <style>
    body {
        background-color: #fff4f8;
    }
    .titulo {
        font-size: 2.5em;
        font-weight: bold;
        color: #cc2b5e;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitulo {
        font-size: 1.3em;
        color: #753a88;
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
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #fcb0d8;
        color: white;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<div class="titulo">🌈 ¡Bienvenidx a <i>ESInformación</i>! 🧠💬</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Un espacio seguro para aprender sobre Educación Sexual Integral (ESI)</div>', unsafe_allow_html=True)

# Presentación
st.write("""
La Educación Sexual Integral busca brindar a los estudiantes información confiable sobre su cuerpo, la sexualidad y la afectividad, para que puedan tomar decisiones libres y responsables.

Promueve el respeto por uno mismo y por los demás, fomenta relaciones sanas y equitativas, y ayuda a prevenir la violencia, los embarazos no deseados y las infecciones de transmisión sexual.

Además, enseña a valorar la diversidad, cuestionar estereotipos de género y fortalecer la autoestima, el autocuidado y la autoafirmación.
""")

# Inputs
nombre = st.text_input("¿Cómo te llamas?")
edad = st.number_input("¿Cuántos años tienes?", min_value=0, step=1)

if nombre and edad:
    if edad < 18:
        st.info(f"¡Perfecto, {nombre}! Como eres menor de edad, usaremos un lenguaje claro y respetuoso 😊.")
    else:
        st.success(f"Gracias por confiar en nosotros, {nombre}. Esta herramienta es útil para todxs 🧡.")

st.markdown("<div class='subtitulo'>¿Qué te gustaría conocer en <i>ESInformación</i>?</div>", unsafe_allow_html=True)

with st.container():
    with st.expander("Haz clic para explorar los temas disponibles", expanded=True):
        opcion = st.selectbox("", [
            "Selecciona una opción",
            "1. ¿Qué es la ESI?",
            "2. Métodos anticonceptivos",
            "3. Mitos y verdades",
            "4. Autocuidado digital y sexting",
            "5. Relaciones afectivas y vínculos sanos",
            "6. Identidad de género y orientación sexual"
        ], key="temas")

    if opcion == "1. ¿Qué es la ESI?":
        st.header("📌 ¿Qué es la ESI?")
        st.markdown("""
La Educación Sexual Integral (ESI) es un enfoque educativo que busca brindar conocimientos científicos, éticos y afectivos sobre la sexualidad. Está diseñada para que niñas, niños y adolescentes desarrollen habilidades para tomar decisiones informadas, responsables y respetuosas sobre su cuerpo y relaciones.

Entre sus objetivos destacan:
- Prevenir embarazos no deseados y enfermedades de transmisión sexual.
- Fomentar el respeto por la diversidad y los derechos humanos.
- Promover relaciones equitativas y libres de violencia.
- Fortalecer la autoestima, el autocuidado y la autoafirmación.

La ESI no reemplaza lo que se enseña en casa, sino que lo complementa, involucrando también a docentes, familias y comunidades.
        """)

    # === SECCIÓN 2 ===
    elif opcion == "2. Métodos anticonceptivos":
        st.header("📌 Métodos Anticonceptivos")
        st.markdown("Haz clic para conocer más sobre cada método:")

        metodos = {
            "🧴 Condón": {
                "img": "https://images.unsplash.com/photo-1575997803451-f0752869e498?q=80&w=1073&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                "desc": """**Condón**
Es el único método que brinda doble protección, ya que previene tanto un embarazo no planificado como las infecciones de transmisión sexual (ITS), incluyendo el VIH. Se debe colocar antes del acto scual.

EFICACIA: El condón masulino tiene una eficacia de 85% para prevenir embarazos no deseados y 95% para prevenir ITS. El condón femenino tiene una eficacia del 79% en su uso común."""
            },
            "💊 Pastillas anticonceptivas": {
                "img": "https://cdn.pixabay.com/photo/2018/04/24/16/58/pill-3348198_960_720.jpg",
                "desc": "**Pastillas anticonceptivas**\n- Uso diario.\n- 99.7% eficacia.\n- Requiere control médico."
            },
            "💉 Inyecciones": {
                "img": "https://cdn.pixabay.com/photo/2020/05/19/19/39/syringe-5193891_1280.jpg",
                "desc": "**Inyecciones**\n- Mensuales o trimestrales.\n- Eficacia entre 99.5% y 99.7%."
            },
            "📍 Implante subdérmico": {
                "img": "https://www.nexplanonusa.com/assets/images/nx_diagram_2.png",
                "desc": "**Implante subdérmico**\n- Dura hasta 3 años.\n- 99.95% eficaz."
            },
            "⚙️ SIU Hormonal": {
                "img": "https://www.healthychildren.org/SiteCollectionImagesArticleImages/IUD.jpg",
                "desc": "**SIU Hormonal**\n- Dispositivo en útero con hormonas.\n- Dura hasta 5 años."
            },
            "🧲 DIU de cobre": {
                "img": "https://www.plannedparenthood.org/uploads/filer_public_thumbnails/filer_public/55/40/554029cd-066e-4d9e-873d-bc35283f9628/iud_illustration.jpg__800x600_q85_crop_subsampling-2.jpg",
                "desc": "**DIU de cobre**\n- Sin hormonas.\n- Dura hasta 12 años.\n- 99.4% eficaz."
            },
            "🚨 AOE": {
                "img": "https://cdn.pixabay.com/photo/2017/08/06/12/39/contraceptive-2595580_1280.jpg",
                "desc": "**AOE (pastilla de emergencia)**\n- Solo en emergencias.\n- Hasta 72h después del acto sexual."
            }
        }

        for metodo, info in metodos.items():
            with st.expander(metodo):
                st.image(info["img"], use_column_width=True)
                st.markdown(info["desc"])

    # === SECCIÓN 3 ===
    if opcion == "3. Mitos y verdades":
        st.header("🎮 ¿Mito o Verdad?")
        preguntas = [
            ("La educación sexual en la escuela interfiere con lo que enseñan en casa.", "mito", "La ESI complementa lo aprendido en familia."),
            ("Hablar de sexualidad hace que los adolescentes tengan más relaciones sexuales.", "mito", "La ESI retrasa el inicio sexual."),
            ("La ESI enseña sobre identidad de género sin imponer orientación.", "verdad", "La ESI enseña a no discriminar y valorar la diversidad."),
            ("Los anticonceptivos afectan permanentemente la fertilidad.", "mito", "La mayoría son reversibles si se usan correctamente."),
            ("El respeto y consentimiento son claves para toda relación.", "verdad", "Sin consentimiento no hay respeto ni salud sexual.")
        ]
        aciertos = 0
        for i, (preg, correcta, exp) in enumerate(preguntas):
            st.markdown(f"**{i+1}. {preg}**")
            rpta = st.radio("¿Qué opinas?", ["", "mito", "verdad"], key=f"rpta_{i}")
            if rpta:
                if rpta == correcta:
                    st.success("✔️ ¡Correcto!")
                    aciertos += 1
                else:
                    st.error("❌ Incorrecto")
                st.info(exp)
                st.markdown("---")

        if aciertos >= 3:
            st.balloons()
            st.success(f"🎉 ¡Felicidades {nombre}! Acertaste {aciertos} de 5 preguntas.")

    # Puedes mantener tus secciones 4, 5 y 6 igual
    elif opcion == "4. Autocuidado digital y sexting":
        st.header("📱 Autocuidado Digital y Sexting")
        st.markdown("""
### Consentimiento - Sexting
El sexting es el intercambio de imágenes o videos de contenido sexual mediante mensajes o redes. Puede ser riesgoso, especialmente en menores, y derivar en abuso sexual. No es aceptable si no hay consentimiento. Presionar a alguien a enviar fotos íntimas es ilegal.

### Cómo evitar la difusión de contenido íntimo
La difusión sin autorización de material íntimo viola el derecho a la privacidad, libertad de expresión y derechos sexuales. Evalúa bien a quién se lo compartes. Si recibes contenido sin consentimiento, elimínalo.

### Responsabilidad ante estas acciones
Difundir material íntimo puede ser penado con hasta 6 años de prisión. Además, pueden sumarse sanciones económicas.

### Recursos y ayuda
Puedes denunciar con pruebas en la División de Delitos de Alta Tecnología de la Policía Nacional. Llama gratis al 1818 o al (01) 431-8898, o escribe a divindat.depcpi@policia.gob.pe.
""")

    elif opcion == "5. Relaciones afectivas y vínculos sanos":
        st.header("💞 Relaciones afectivas y vínculos sanos")
        st.markdown("""
### Amor, atracción y deseo
El deseo es atracción física y sexual. La atracción romántica involucra emociones y euforia. El amor es una conexión profunda, emocional, física y espiritual.

### ¿Qué es el amor?
Es un sentimiento complejo que da plenitud, felicidad y conexión con otros.

### Señales de relaciones tóxicas
- Control y celos excesivos  
- Manipulación emocional ("si me amaras...")  
- Comunicación dañina (críticas, silencio castigador, gaslighting)  
- Ignorar tus necesidades o emociones  
- Minimizar lo que sientes

### ¿Estoy en una relación tóxica?
Hazte preguntas: ¿Te respeta? ¿Te manipula? ¿Te aísla? Si muchas respuestas son negativas, busca apoyo emocional profesional.
""")

    elif opcion == "6. Identidad de género y orientación sexual":
        st.header("🏳️‍🌈 Identidad de género y orientación sexual")
        st.markdown("""
### Sexo
Asignado al nacer por características físicas y cromosómicas.

### Género
Es una construcción social, cultural y legal sobre los roles esperados.

### Identidad de género
Cómo te identificas y expresas tu género (ropa, lenguaje, conducta). Puede o no coincidir con tu sexo asignado.

### Orientación sexual
Es la atracción emocional, afectiva o sexual hacia otras personas. Puede ser homosexual, bisexual, asexual, entre otras.
""")
    # === SECCIÓN FEEDBACK ===
st.markdown("## 🙋‍♀️ Califícanos")
experiencia = st.selectbox("¿Te gustó la experiencia en ESInformación?", ["", "⭐ Muy mala", "⭐⭐ Mala", "⭐⭐⭐ Regular", "⭐⭐⭐⭐ Buena", "⭐⭐⭐⭐⭐ Excelente"])
if experiencia:
    st.success("¡Gracias por tu calificación!")

# Pie de página
st.markdown("""
<hr>
<div style='text-align:center;'>
Gracias por usar <b>ESInformación</b> 💜
</div>
""", unsafe_allow_html=True)

