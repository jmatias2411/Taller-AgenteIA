# 🧠 Orion - Agente IA local con herramientas

Este repositorio contiene el **código completo y comentado** de un proyecto educativo que muestra cómo construir tu **primer agente inteligente con Python y Ollama**.

> 👨‍💻 Autor: Matías  
> 🧩 Temática: Agentes Inteligentes + Modelos LLM locales + Herramientas  
> ⚙️ Tecnologías: Python · Streamlit · LangChain · Ollama

---

## 🚀 ¿Qué es Orion?

**Orion** es un agente conversacional local, diseñado para funcionar completamente en tu equipo sin depender de servicios externos. Utiliza modelos de lenguaje **open-source** a través de **Ollama**, y se integra con herramientas externas como una **calculadora**, además de tener **memoria persistente** para recordar conversaciones anteriores.

Este proyecto demuestra cómo construir un **agente IA real**, con capacidad de **razonamiento**, uso de **herramientas** y **memoria**.

---

## ✨ Funcionalidades principales

- ✅ Modelo LLM local con **Ollama** (por defecto: Mistral)
- ✅ Interfaz amigable usando **Streamlit**
- ✅ Uso de **herramientas personalizadas** (como una calculadora)
- ✅ **Memoria persistente** guardada en `memoria.json`
- ✅ Agente con razonamiento tipo `ZERO_SHOT_REACT_DESCRIPTION`

---

## 🧩 Requisitos

- Python 3.10 o superior
- [Ollama](https://ollama.com) instalado y corriendo localmente con el modelo `mistral`
- Dependencias del proyecto:

```bash
pip install -r requirements.txt
````

---

## ▶️ Cómo ejecutarlo

1. Asegúrate de tener **Ollama** corriendo:

```bash
ollama run mistral
```

2. Clona este repositorio:

```bash
git clone https://github.com/jmatias2411/Taller-AgenteIA.git
cd Taller-AgenteIA
```

3. Instala las dependencias necesarias:

```bash
pip install streamlit langchain langchain-community langchain-core langchain-ollama
```

4. Ejecuta la app:

```bash
streamlit run app.py
```

---

## 🛠 Estructura del proyecto

| Archivo        | Descripción                                                               |
| -------------- | ------------------------------------------------------------------------- |
| `app.py`       | Script principal. Ejecuta el agente con interfaz, herramientas y memoria. |
| `memoria.json` | Archivo generado automáticamente con el historial de conversación.        |

---

## 🎯 ¿Para qué sirve?

* Para aprender cómo funciona LangChain y cómo usar herramientas en agentes IA
* Para construir tu propio asistente personal que recuerda y razona
* Para experimentar con IA local sin depender de la nube

---

## 💡 ¿Te gustó?

Si este proyecto te resulta útil, dale ⭐ en GitHub o sígueme en [LinkedIn](https://www.linkedin.com/in/matias-palomino-luna24/).
Estoy compartiendo más proyectos sobre IA local, automatización y agentes inteligentes.

---

**¡Construyamos una IA útil, cercana y bajo nuestro control!**
