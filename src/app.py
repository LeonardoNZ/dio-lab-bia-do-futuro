import json
import pandas as pd
import requests
import streamlit as st
from pathlib import Path

# ================= CONFIG =================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3"

st.set_page_config(
    page_title="Nutrix — Educador Alimentar",
    page_icon="🥗",
    layout="centered"
)

# ================= LOAD DATA =================

DATA_DIR = Path("./data")

@st.cache_data
def load_data():
    try:
        perfil = json.load(open(DATA_DIR / "perfil_usuario.json", encoding="utf-8"))
    except:
        perfil = {}

    try:
        refeicoes = pd.read_csv(DATA_DIR / "registro_refeicoes.csv")
    except:
        refeicoes = pd.DataFrame()

    try:
        historico = pd.read_csv(DATA_DIR / "historico_orientacoes.csv")
    except:
        historico = pd.DataFrame()

    try:
        alimentos = json.load(open(DATA_DIR / "guia_nutrientes.json", encoding="utf-8"))
    except:
        alimentos = {}

    return perfil, refeicoes, historico, alimentos


perfil, refeicoes, historico, alimentos = load_data()

# ================= CONTEXTO =================

def df_to_text(df):
    if df is None or df.empty:
        return "Sem registros."
    return df.to_string(index=False)

contexto = f"""
OBJETIVO ALIMENTAR: {perfil.get('objetivo','não informado')}
RESTRIÇÕES: {perfil.get('restricoes','não informado')}

REGISTRO DE REFEIÇÕES:
{df_to_text(refeicoes)}

ATENDIMENTOS ANTERIORES:
{df_to_text(historico)}

BASE DE ALIMENTOS:
{json.dumps(alimentos, ensure_ascii=False)}
"""

# ================= SYSTEM PROMPT =================

SYSTEM_PROMPT = """Você é o Nutrix, um educador de alimentação básica amigável, didático e responsável.

MISSÃO:
Explicar conceitos de nutrição e hábitos saudáveis de forma simples. Você educa — não prescreve.

PROIBIDO:
- prescrever dietas
- definir quantidades individuais
- tratar doenças
- substituir profissional de saúde

PERMITIDO:
- explicar nutrientes
- explicar rótulos
- explicar equilíbrio alimentar
- explicar hábitos saudáveis

Estilo:
- simples
- direto
- amigável
- até 3 parágrafos
- sem termos técnicos desnecessários
- finalize perguntando se o usuário entendeu.
"""

# ================= OLLAMA CALL =================

def perguntar(msg):

    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO:
{contexto}

Pergunta: {msg}
"""

    try:
        r = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        r.raise_for_status()
        data = r.json()

        return data.get("response", "Sem resposta do modelo.")

    except requests.exceptions.ConnectionError:
        return "⚠️ Ollama não está rodando. Abra o Ollama e rode: ollama run llama3"

    except Exception as e:
        return f"⚠️ Erro ao consultar modelo local: {e}"


# ================= UI =================

st.title("🥗 Nutrix — Educador Alimentar")
st.caption("Aprenda nutrição básica de forma simples. Sem dietas. Sem prescrição.")

st.success("🤖 Agente educativo ativo • Modelo local (Ollama)")

st.info("Pergunte sobre nutrientes, rótulos, hábitos alimentares e equilíbrio nutricional.")

# ================= CHAT =================

if "chat" not in st.session_state:
    st.session_state.chat = []

for role, content in st.session_state.chat:
    st.chat_message(role).write(content)

pergunta = st.chat_input("Digite sua dúvida sobre alimentação...")

if pergunta:
    st.session_state.chat.append(("user", pergunta))
    st.chat_message("user").write(pergunta)

    with st.spinner("Nutrix está pensando..."):
        resposta = perguntar(pergunta)

    st.session_state.chat.append(("assistant", resposta))
    st.chat_message("assistant").write(resposta)

# ================= FOOTER =================

st.divider()
st.caption("⚠️ Conteúdo educativo. Procure nutricionista para orientação personalizada.")
