import json
import pandas as pd
import requests
import streamlit as st

# ================= CONFIG =================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

st.set_page_config(
    page_title="Nutrix — Educador Alimentar",
    page_icon="🥗",
    layout="centered"
)

# ================= LOAD DATA =================
@st.cache_data
def load_data():
    perfil = json.load(open('./data/perfil_usuario.json'))
    refeicoes = pd.read_csv('./data/refeicoes.csv')
    historico = pd.read_csv('./data/historico_atendimento.csv')
    alimentos = json.load(open('./data/base_alimentos.json'))
    return perfil, refeicoes, historico, alimentos

perfil, refeicoes, historico, alimentos = load_data()

# ================= CONTEXTO =================
contexto = f"""
USUÁRIO: {perfil['nome']}, {perfil['idade']} anos
OBJETIVO ALIMENTAR: {perfil['objetivo']}
RESTRIÇÕES: {perfil['restricoes']}

REGISTRO DE REFEIÇÕES:
{refeicoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

BASE DE ALIMENTOS:
{json.dumps(alimentos, indent=2, ensure_ascii=False)}
"""

# ================= SYSTEM PROMPT =================
SYSTEM_PROMPT = """Você é o Nutrix, um educador de alimentação básica amigável, didático e responsável.

MISSÃO:
Ajudar o usuário a entender conceitos de nutrição e hábitos alimentares saudáveis de forma simples e prática. Você educa — não prescreve. Usa os dados fornecidos do usuário apenas como exemplos ilustrativos.

ESCOPO DE ATUAÇÃO:
Você pode explicar:
- nutrientes (carboidratos, proteínas, gorduras, fibras, vitaminas);
- equilíbrio alimentar;
- leitura de rótulos;
- organização básica de refeições;
- hábitos saudáveis do dia a dia;
- diferenças entre alimentos in natura, processados e ultraprocessados.

Você NÃO pode:
- prescrever dietas ou cardápios personalizados;
- definir quantidades exatas de consumo individual;
- tratar doenças com alimentação;
- substituir nutricionista, médico ou outro profissional de saúde.

REGRAS DE SEGURANÇA:
- NUNCA forneça prescrição alimentar personalizada;
- NUNCA recomende tratamento de saúde;
- Sempre inclua orientação para procurar profissional quando envolver condição clínica;
- Se o usuário pedir algo fora do escopo, responda lembrando seu papel educativo;
- Se faltarem dados, diga explicitamente que não tem informação suficiente.

USO DOS DADOS DO USUÁRIO:
- Use os dados fornecidos apenas como exemplo didático;
- Não faça julgamentos sobre hábitos alimentares;
- Destaque padrões e explique conceitos com base neles;
- Evite linguagem de culpa ou crítica.

ESTILO DE RESPOSTA:
- Linguagem simples, direta e amigável;
- Explique com analogias do cotidiano quando útil;
- Priorize clareza sobre termos técnicos;
- Seja objetivo (máximo 3 parágrafos);
- Sempre que possível finalize perguntando se o usuário entendeu.

INCERTEZA:
Quando não souber algo, diga:
"Não tenho essa informação específica, mas posso explicar o conceito geral relacionado."

PRIORIDADE DE COMPORTAMENTO:
Segurança > Escopo educativo > Clareza > Personalização didática.
"""

# ================= OLLAMA CALL =================
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO USUÁRIO:
{contexto}

Pergunta do usuário: {msg}
"""

    r = requests.post(
        OLLAMA_URL,
        json={"model": MODELO, "prompt": prompt, "stream": False}
    )

    return r.json()['response']

# ================= SIDEBAR =================
with st.sidebar:
    st.header("👤 Perfil do Usuário")
    st.write(f"**Nome:** {perfil['nome']}")
    st.write(f"**Idade:** {perfil['idade']}")
    st.write(f"**Objetivo:** {perfil['objetivo']}")
    st.write(f"**Restrições:** {perfil['restricoes']}")

    st.divider()
    st.caption("Nutrix é educativo e não prescreve dietas.")

    if st.button("📊 Ver últimas refeições"):
        st.dataframe(refeicoes.tail(5))

# ================= HEADER =================
st.title("🥗 Nutrix — Educador Alimentar")
st.caption("Aprenda nutrição básica de forma simples. Sem dietas, sem prescrição.")

st.info("Pergunte sobre nutrientes, rótulos, hábitos alimentares e equilíbrio nutricional.")

# ================= CHAT MEMORY =================
if "chat" not in st.session_state:
    st.session_state.chat = []

for role, content in st.session_state.chat:
    st.chat_message(role).write(content)

# ================= INPUT =================
pergunta = st.chat_input("Digite sua dúvida sobre alimentação...")

if pergunta:
    st.session_state.chat.append(("user", pergunta))
    st.chat_message("user").write(pergunta)

    with st.spinner("Nutrix está explicando..."):
        resposta = perguntar(pergunta)

    st.session_state.chat.append(("assistant", resposta))
    st.chat_message("assistant").write(resposta)

# ================= FOOTER =================
st.divider()
st.caption("⚠️ Conteúdo educativo. Procure um nutricionista para orientação personalizada.")
