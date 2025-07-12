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
                "img": "https://images.unsplash.com/photo-1576065435202-e0a7979b93e3?q=80&w=1117&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                "desc": """**Pastillas anticonceptivas**
Método hormonal que inhibe la ovulación y espesa el moco cervical, dificultando el paso de los espermatozoides. Las píldoras combinadas de estrógenos y progestágenos deben tomarse diariamente a la misma hora. Uso: Diariamente a la misma hora.

Eficacia: 99,7 % si se usa correctamente. También protege contra el cáncer de ovario y endometrio."""

            },
            "💉 Inyecciones": {
                "img": "https://images.unsplash.com/photo-1609009630912-f16dcf3e03a6?q=80&w=688&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                "desc": """**Inyecciones**
Actúan como deteniendo la ovulación y espesan el moco cervical, además que bloquean el paso de los espermatozoides hacia el útero. Puede hacerlo durante ciertos meses, por ejemplo inyectable mensual, te protege todo un mes, además del trimestre que es por tres meses.

Tiene una eficacia de manera mensual de 99.5% y trimestral de 99.7%"""

            },
            "📍 Implante subdérmico": {
                "img": "https://enfamilia.aeped.es/sites/enfamilia.aeped.es/files/images/articulos/implante2.jpg",
                "desc": """**Implante subdérmico**
Es una pequeña varilla flexible colocada debajo de la piel del brazo, libera progestágeno de manera seguida para prevenir el embarazo. Puede proteger hasta por 3 años 

Su eficacia es de 99.95%. Puede causar alteraciones menstruales, pero no interfiere con el acto sexual."""
            },
            "⚙️ Sistema Intrauterino de Levonorgestrel - SIU-LING": {
                "img": "https://images.unsplash.com/photo-1715111641899-b0118be16660?q=80&w=1108&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                "desc": """**SIU Hormonal**
Es un dispositivo pequeño que se inserta en el utero y liberta hormonas, puede proteger hasta por 5 años y es colocado por un profesional.

Tiene un 99.5% de eficacia."""
            },
            "🧲 Dispositivo intrauterino - DIU de cobre": {
                "img": "https://images.unsplash.com/photo-1576070932889-43995345c9b6?q=80&w=1077&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                "desc": """**DIU de cobre**
Pequeño dispositivo recubierto con cobre, que se coloca en el utero para evitar la fertilización, tiene una protección por 12 años y también es colocado por un profesional

Eficacia de 99.4%. No interfiere con el acto sexual"""
            },
            "🚨 Anticonceptivo Oral de Emergencia - AOE": {
                "img": "https://images.unsplash.com/photo-1576069445378-ddc40a383222?q=80&w=1073&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                "desc": """**AOE (pastilla de emergencia)**
Utilizado solo en situaciones de emergencia, como relaciones sin protección o violencia sexual, puede durar hasta 72 horas despúes del actos sexual.

Tiene hasta un 95% de efectividad, tiene mayor efectividad cuanto antes se use. No sustituye al uso regular de otros métodos."""

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
            ("La educación sexual en la escuela interfiere con lo que enseñan en casa.", "mito", "La educación sexual integral no interfiere con la educación previa que nuestros padres y madres nos ofrecen, sino que por el contrario, la labor de padres y profesores se complementa para asegurar una formación integral. ),
            ("Hablar de sexualidad hace que los adolescentes tengan más relaciones sexuales a temprana edad.", "mito", "Está demostrado que la ESI retrasa el inicio sexual y mejora la toma de decisiones, además ayuda a crecer en conocimiento y valores para vivir la sexualidad con bienestar."),
            ("Hay adultos quienes no tuvieron previa enseñanza sobre la sexualidad, aprendieron solos y les fue bien.", "mito", "Estas son personas que no tuvieron la oportunidad de recibir información integral en la escuela, ello ha generado diversas dudas que les impide disfrutar su sexualidad plenamente. Por ello es importante hablar sobre la ESI."),
            ("La ESI habla sobre identidad de género u orientación sexual en la escuela, sin determinar la sexualidad de las personas.", "verdad", "Verdad, pues enseña a no discriminar y a valorar la diversidad que hay a nuestro alrededor."),
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

        if aciertos == 4:
            st.balloons()
            st.markdown(f"<h2 style='text-align: center; color: green;'>🎉 ¡Excelente, {nombre}! Respondiste todas correctamente. ¡Sigue así! 🎉</h2>", unsafe_allow_html=True)
        elif aciertos == 3:
            st.markdown(f"<h2 style='text-align: center;'>👏 ¡Muy bien, {nombre}! Aciertos: 3 de 4. Vas por buen camino.</h2>", unsafe_allow_html=True)
        elif aciertos == 2:
            st.markdown(f"<h3 style='text-align: center;'>🙂 ¡Tú puedes! Acertaste 2, sigue practicando.</h3>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h3 style='text-align: center;'>💪 No te desanimes, {nombre}. ¡Sigue aprendiendo y mejorando!</h3>", unsafe_allow_html=True)


    #SECCIÓN 4
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

