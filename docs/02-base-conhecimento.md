# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve no Nutrix? |
|---------|---------|---------------------------|
| `historico_orientacoes.csv` | CSV | Contextualizar orientações já explicadas ao usuário e manter continuidade educativa. |
| `perfil_usuario.json` | JSON | Personalizar as explicações conforme rotina, restrições e objetivos alimentares. |
| `guia_nutrientes.json` | JSON | Fornecer a base conceitual de nutrientes para ensino didático. |
| `registro_refeicoes.csv` | CSV | Analisar padrões de refeições e usar exemplos práticos nas explicações. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os nutrientes foram organizados por função prática (energia, construção corporal, regulação e saúde intestinal) em vez de classificação técnica completa. Isso facilita explicações didáticas e reduz complexidade desnecessária para o público iniciante.

---

## Estratégia de Integração

### Como os dados são carregados?

Existem duas possibilidades, injetar os dados diretamente no prompt (Ctrl + C, Ctrl + V) ou carregar os arquivos via código, como no exemplo abaixo:

```python
import pandas as pd
import json

perfil = json.load(open('./data/perfil_usuario.json'))
refeicoes = pd.read_csv('./data/registro_refeicoes.csv')
historico = pd.read_csv('./data/historico_orientacoes.csv')
nutrientes = json.load(open('./data/guia_nutrientes.json'))

```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos simplesmente injetar os dados no prompt, garantindo que o agente tenha o melhor contexto possível. Em soluções mais robustas, o ideal é consultar essas informações dinamicamente conforme o tema da pergunta.

```text
DADOS DO USUÁRIO (data/perfil_usuario.json):
{
  "nome": "Maria Souza",
  "idade": 29,
  "rotina": "trabalho em escritório",
  "objetivo_alimentar": "melhorar qualidade da alimentação",
  "restricoes": ["intolerância à lactose"],
  "refeicoes_por_dia": 4,
  "consumo_agua_estimado_ml": 1200,
  "nivel_conhecimento_nutricao": "iniciante"
}

REGISTRO DE REFEIÇÕES (data/registro_refeicoes.csv):
data,refeicao,descricao,categoria
2026-02-01,cafe_da_manha,pao branco com manteiga,refinado
2026-02-01,almoco,arroz frango batata frita,caseiro
2026-02-01,lanche,biscoito recheado,ultraprocessado
2026-02-01,jantar,massa com molho pronto,processado
2026-02-02,cafe_da_manha,cereal com leite,processado
2026-02-02,almoco,arroz feijao carne salada,caseiro
2026-02-02,lanche,iogurte,processado
2026-02-02,jantar,sanduiche,processado

HISTORICO DE ORIENTAÇÕES (data/historico_orientacoes.csv):
data,canal,tema,resumo,resolvido
2026-01-20,chat,proteinas,explicacao sobre funcao das proteinas,sim
2026-01-25,chat,hidratacao,orientacao sobre consumo de agua,sim
2026-01-28,chat,rotulos,como ler tabela nutricional,sim
2026-02-02,chat,fibras,beneficios das fibras na dieta,sim

GUIA DE NUTRIENTES (data/guia_nutrientes.json):
[
  {
    "nome": "Carboidratos",
    "funcao": "fornecer energia",
    "exemplos": ["arroz", "pão", "massa", "batata", "aveia"],
    "observacao": "preferir integrais quando possível"
  },
  {
    "nome": "Proteínas",
    "funcao": "construção e reparo do corpo",
    "exemplos": ["frango", "ovos", "feijão", "peixe"],
    "observacao": "importante nas refeições principais"
  },
  {
    "nome": "Gorduras boas",
    "funcao": "função hormonal e absorção de vitaminas",
    "exemplos": ["azeite", "castanhas", "abacate"],
    "observacao": "usar com moderação"
  },
  {
    "nome": "Fibras",
    "funcao": "saúde intestinal e saciedade",
    "exemplos": ["verduras", "legumes", "grãos integrais"],
    "observacao": "aumentar consumo gradualmente"
  }
]
```

---

## Exemplo de Contexto Montado

O exemplo de contexto abaixo sintetiza os dados originais e mantém apenas as informações mais relevantes para reduzir consumo de tokens, sem perder qualidade educativa.

```
DADOS DO USUÁRIO:
- Nome: Maria Souza
- Objetivo: melhorar qualidade da alimentação
- Restrição: intolerância à lactose
- Refeições por dia: 4
- Nível: iniciante

PADRÃO RECENTE DE REFEIÇÕES:
- Café da manhã frequente: pão branco ou cereal processado
- Almoço: base caseira, porém com fritura em alguns dias
- Lanches: ultraprocessados
- Baixo consumo de integrais e fibras

CONCEITOS DISPONÍVEIS PARA ENSINO:
- Carboidratos = energia
- Proteínas = construção corporal
- Gorduras boas = função hormonal
- Fibras = saúde intestinal e saciedade
```
