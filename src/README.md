# 🥗 Passo a Passo de Execução — Nutrix

## 📌 Sobre a Aplicação

O Nutrix é um agente educativo de nutrição básica que responde dúvidas sobre alimentação saudável, nutrientes, rótulos e hábitos alimentares.  
Ele **não prescreve dietas** e não substitui profissionais de saúde — atua apenas de forma didática.

O modelo roda localmente usando **Ollama + LLM** e a interface é feita com **Streamlit**.

---

# 🧠 Setup do Ollama

```bash
# 1. Instalar Ollama
https://ollama.com

# 2. Baixar o modelo utilizado no projeto
ollama pull llama3

# 3. Testar o modelo
ollama run llama3
```

Se responder no terminal, está funcionando.  
Digite `/bye` para sair.

---

# 🐍 Setup do Ambiente Python

Dentro da pasta do projeto:

```bash
# criar ambiente virtual
python -m venv .venv

# ativar ambiente (Windows PowerShell)
.venv\Scripts\activate

# instalar dependências
pip install streamlit pandas requests
```

---

# 📁 Estrutura de Pastas Esperada

```
src/
 ├── app.py
 └── data/
     ├── perfil_usuario.json
     ├── guia_nutrientes.json
     ├── registro_refeicoes.csv
     └── historico_orientacoes.csv
```

---

# ▶️ Como Rodar a Aplicação

Entre na pasta do código:

```bash
cd src
```

Execute:

```bash
streamlit run app.py
```

Se o comando não for reconhecido:

```bash
python -m streamlit run app.py
```

A aplicação abrirá no navegador:

```
http://localhost:8501
```

---

# 🔌 Garantir que o Ollama está ativo

Se ocorrer erro de conexão com o modelo, rode:

```bash
ollama run llama3
```

Se abrir normalmente, digite:

```
/bye
```

Depois execute o app novamente.

---

# ❗ Problemas Comuns

## Streamlit não reconhecido

```bash
python -m streamlit run app.py
```

---

## Erro de modelo no Ollama

Verifique se o modelo foi baixado:

```bash
ollama list
```

Se não aparecer:

```bash
ollama pull llama3
```

---

# 🧪 Evidência de Execução
<img width="1914" height="912" alt="Captura de tela 2026-02-12 123644" src="https://github.com/user-attachments/assets/c500d31a-a220-4e65-baa1-86bb24729b18" />


```markdown



---

# 📦 Código Fonte

Todo o código da aplicação está no arquivo:

```
src/app.py
```

---
