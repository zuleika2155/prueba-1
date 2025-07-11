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

    opcion = st.selectbox("¿Qué te gustaría conocer en *ESInformación*?", [
        "Selecciona una opción",
        "1. ¿Qué es la ESI?",
        "2. Métodos anticonceptivos",
        "3. Mitos y verdades",
        "4. Autocuidado digital y sexting",
        "5. Relaciones afectivas y vínculos sanos",
        "6. Identidad de género y orientación sexual"
    ])

    # === SECCIÓN 1 ===
    if opcion == "1. ¿Qué es la ESI?":
        st.header("📌 ¿Qué es la ESI?")
        st.write("""
La Educación Sexual Integral, más conocida como la ESI, es un programa del MINEDU que busca brindar información, habilidades y valores a estudiantes para que puedan tomar decisiones informadas, saludables y responsables sobre su sexualidad.

Tiene como objetivos prevenir/reducir embarazos adolescentes, violencia sexual, uniones tempranas y problemas de salud relacionados.

Además, no solo está dirigida a estudiantes, sino también a docentes y familiares, mediante acciones formativas, preventivas y de fortalecimiento de capacidades.
        """)

    # === SECCIÓN 2 ===
    elif opcion == "2. Métodos anticonceptivos":
        st.header("📌 Métodos Anticonceptivos")
        st.markdown("Haz clic para conocer más sobre cada método:")

        metodos = {
            "🧴 Condón": {
                "img": "https://www.salud.mapfre.es/media/2021/04/condon.jpg",
                "desc": "**Condón**\n- Doble protección: embarazo e ITS.\n- Uso externo.\n- Eficacia: masculino 85%, femenino 79%."
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
    elif opcion == "3. Mitos y verdades":
        st.header("🎮 ¿Mito o Verdad?")
        st.write("Responde y descubre si tu respuesta es correcta.")

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
                "exp": "La ESI ayuda a tomar decisiones informadas y retrasar el inicio sexual.",
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
            st.image(item["img"], width=100)
            st.markdown(f"**{i}. {item['preg']}**")
            respuesta = st.radio("Elige una opción:", ["mito", "verdad"], key=f"mito{i}")
            if respuesta:
                if respuesta == item["rpta"]:
                    st.success("✔️ ¡Correcto!")
                else:
                    st.error("❌ Incorrecto")
                st.info(item["exp"])
                st.markdown("---")

    # Puedes mantener tus secciones 4, 5 y 6 igual

    # === SECCIÓN FEEDBACK ===
    st.subheader("🗣️ ¿Te gustó la experiencia?")
    satisfaccion = st.slider("Del 1 al 10, ¿qué tanto te gustó esta app?", 1, 10)
    comentarios = st.text_area("¿Tienes alguna sugerencia o comentario?", "")
    if st.button("Enviar opinión"):
        st.success("✅ ¡Gracias por tu feedback! 💌")

# === PIE DE PÁGINA ===
st.markdown("""
<hr>
<div style='text-align:center; color: #753a88;'>
Gracias por usar <b>ESInformación</b> 💜
</div>
""", unsafe_allow_html=True)
