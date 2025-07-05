import os
import json
import re
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain.agents import Tool, initialize_agent, AgentType

# Archivo donde se guarda la memoria
MEMORY_FILE = "memoria.json"

# Inicializa el modelo LLM local
chat = ChatOllama(model="mistral")

# Función herramienta (calculadora)
def calculadora(query: str) -> str:
    try:
        resultado = eval(query)
        return f"El resultado de {query} es {resultado}"
    except Exception:
        return "Lo siento, no pude resolver esa operación."

# Tool definida para LangChain
tools = [
    Tool(
        name="Calculadora",
        func=calculadora,
        description="Úsala para resolver operaciones matemáticas simples. Ej: '5 * (2 + 3)'"
    )
]

# Prompt personalizado
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Eres *Orion*, un agente conversacional en español, con memoria y capacidad de razonar. "
        "Respondes de forma clara, cercana y didáctica. "
        "Puedes usar herramientas como una calculadora para ayudar mejor al usuario. "
        "Recuerda lo que el usuario te ha dicho antes y sé útil, empático y profesional."
    ),
    MessagesPlaceholder(variable_name="messages")
])

# Función para cargar historial desde archivo
def cargar_memoria():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                contenido = f.read().strip()
                if not contenido:
                    return []
                raw_history = json.loads(contenido)
                history = []
                for m in raw_history:
                    if m["type"] == "human":
                        history.append(HumanMessage(content=m["content"]))
                    elif m["type"] == "ai":
                        history.append(AIMessage(content=m["content"]))
                return history
        except json.JSONDecodeError:
            return []
    return []

# Función para guardar historial a archivo
def guardar_memoria(history):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        raw_history = [
            {"type": "human" if isinstance(m, HumanMessage) else "ai", "content": m.content}
            for m in history
        ]
        json.dump(raw_history, f, indent=2, ensure_ascii=False)

# Configuración de Streamlit
st.set_page_config(page_title="Orion - Agente IA local", layout="centered")
st.title("🧠 Orion: tu agente IA local con herramientas")

st.markdown("Hola, soy Orion. Puedo ayudarte a entender cosas, resolver cálculos y recordar lo que conversamos. "
            "Prueba escribiendo algo como **'¿Cuánto es 25 * (3 + 2)?'** o **'Explícame qué es una función en Python'.**")

# Cargar historial
if "history" not in st.session_state:
    st.session_state.history = cargar_memoria()

# Mostrar historial previo
for msg in st.session_state.history:
    with st.chat_message("user" if isinstance(msg, HumanMessage) else "assistant"):
        st.markdown(msg.content)

# Entrada del usuario
user_input = st.chat_input("Escribe tu mensaje...")

if user_input:
    st.session_state.history.append(HumanMessage(content=user_input))

    # Crear el agente con herramientas
    agent = initialize_agent(
        tools=tools,
        llm=chat,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        handle_parsing_errors=True
    )

    # Ejecutar el agente con historial como contexto
    response = agent.invoke(st.session_state.history)

    # Extraer texto limpio de la respuesta
    if hasattr(response, "content"):
        respuesta_final = response.content
    elif isinstance(response, dict) and "output" in response:
        respuesta_final = response["output"]
    else:
        respuesta_final = str(response)

    # Limpieza si viene string con formato tipo HumanMessage(...)
    if isinstance(respuesta_final, str) and "HumanMessage" in respuesta_final:
        match = re.search(r"content='(.*?)'", respuesta_final)
        if match:
            respuesta_final = match.group(1)

    # Mostrar y guardar
    st.session_state.history.append(AIMessage(content=respuesta_final))

    with st.chat_message("assistant"):
        st.markdown(respuesta_final)

    guardar_memoria(st.session_state.history)
