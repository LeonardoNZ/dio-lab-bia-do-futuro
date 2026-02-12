# 🥦 Nutrix — Educador Alimentar Inteligente

> Agente de IA Generativa que educa sobre alimentação saudável de forma simples e personalizada, usando o perfil e hábitos do próprio usuário como base para exemplos práticos.

---

## 💡 O Que é o Nutrix?

O Nutrix é um educador alimentar que **ensina**, não prescreve. Ele explica conceitos como macronutrientes, grupos alimentares, hidratação e leitura de rótulos com uma abordagem didática e acolhedora, adaptando os exemplos ao perfil do usuário.

**O que o Nutrix faz:**
- ✅ Explica conceitos nutricionais de forma clara e acessível
- ✅ Usa os hábitos e preferências do usuário como exemplos
- ✅ Responde dúvidas sobre alimentos, dietas e rotinas alimentares
- ✅ Analisa padrões alimentares de forma educativa

**O que o Nutrix NÃO faz:**
- ❌ Não prescreve dietas ou planos alimentares clínicos
- ❌ Não substitui um nutricionista registrado
- ❌ Não fornece orientações para condições médicas específicas

---

## 🏗️ Arquitetura

```
flowchart TD
    A[Usuário] --> B[Streamlit]
    B --> C[Ollama - LLM Local]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Resposta Educativa]
```

**Stack:**
- Interface: Streamlit
- LLM: Ollama (modelo local)
- Dados: JSON/CSV com perfil e histórico alimentar

---

## 📁 Estrutura do Projeto

```
├── data/                            # Base de conhecimento
│   ├── perfil_usuario.json          # Perfil e preferências alimentares
│   ├── registro_alimentar.csv       # Histórico de refeições
│   ├── historico_atendimento.csv    # Interações anteriores
│   └── alimentos_referencia.json    # Base de alimentos para ensino
│
├── docs/                            # Documentação completa
│   ├── 01-documentacao-agente.md    # Caso de uso e persona
│   ├── 02-base-conhecimento.md      # Estratégia de dados
│   ├── 03-prompts.md                # System prompt e exemplos
│   ├── 04-metricas.md               # Avaliação de qualidade
│   └── 05-pitch.md                  # Apresentação do projeto
│
├── examples/                        # Exemplos de interações
├── assets/                          # Imagens e recursos visuais
└── src/
    └── app.py                       # Aplicação Streamlit
```

---

## 🚀 Como Executar

**1. Instalar o Ollama**
```bash
# Baixar em: ollama.com
ollama pull llama3
ollama serve
```

**2. Instalar Dependências**
```bash
pip install streamlit pandas requests
```

**3. Rodar o Nutrix**
```bash
streamlit run src/app.py
```

---

## 🎯 Exemplos de Uso

**Pergunta:** "O que são proteínas e por que são importantes?"  
**Nutrix:** "Proteínas são os 'tijolos' do seu corpo — constroem e reparam tecidos, incluindo músculos. Olhando seu registro de hoje, você consumiu frango no almoço, ótima fonte! Quer que eu explique a diferença entre proteínas de origem animal e vegetal?"

**Pergunta:** "Estou comendo de forma equilibrada?"  
**Nutrix:** "No seu registro desta semana, frutas e vegetais aparecem em apenas 2 das 14 refeições registradas. O ideal seria pelo menos metade do prato em cada refeição. Quer que eu explique como montar um prato mais equilibrado sem complicar?"

---

## 📊 Métricas de Avaliação

| Métrica | Objetivo |
|---|---|
| **Assertividade** | O agente responde o que foi perguntado? |
| **Segurança** | Evita inventar informações nutricionais (anti-alucinação)? |
| **Coerência** | A resposta é adequada ao perfil do usuário? |

---

## 🎬 Diferenciais

- **Personalização:** Usa os hábitos reais do usuário nos exemplos
- **100% Local:** Roda com Ollama, sem enviar dados para APIs externas
- **Educativo:** Foco em ensinar autonomia alimentar, não em prescrever
- **Seguro:** Estratégias de anti-alucinação e limites claros documentados

---

## 📝 Documentação Completa

Toda a documentação técnica, estratégias de prompt e casos de teste estão disponíveis na pasta [`docs/`](./docs).

---

> Desenvolvido como parte do laboratório **BIA do Futuro** na [DIO](https://www.dio.me).
