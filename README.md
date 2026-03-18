# 🩺 Diagnóstico de Diabetes — API de Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-API-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![Render](https://img.shields.io/badge/Deploy-Render-purple?logo=render)
![Status](https://img.shields.io/badge/Status-Online-brightgreen)

> API REST para predição de diabetes em pacientes do Povo Pima com base em atributos biomédicos, utilizando modelo de Machine Learning treinado com Random Forest.

---

## 🌐 API em Produção

| Item | Detalhe |
|------|---------|
| 🔗 URL Base | https://diagnostico-diabetes-ml-1.onrender.com |
| ☁️ Plataforma | Render |
| 📍 Região | Oregon (US West) |
| 🐳 Ambiente | Docker |
| 🔌 Porta | 8000 |

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Dataset](#-dataset)
- [Modelos Treinados](#-modelos-treinados)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Como Executar Localmente](#-como-executar-localmente)
- [Como Executar com Docker](#-como-executar-com-docker)
- [Endpoints da API](#-endpoints-da-api)
- [Testes no Postman](#-testes-no-postman)
- [Deploy no Render](#-deploy-no-render)
- [Autores](#-autores)
- [Informações Acadêmicas](#-informações-acadêmicas)

---

## 📌 Sobre o Projeto

Este projeto transforma um modelo de Machine Learning treinado em Python em um serviço acessível via HTTP. A API recebe dados biomédicos de pacientes e retorna a predição de diabetes (positivo ou negativo).

O fluxo completo cobre:

```
Treinamento do Modelo
        ↓
  Salvar modelo (.pkl)
        ↓
   Criar API Flask
        ↓
  Testar localmente
        ↓
 Criar imagem Docker
        ↓
  Executar container
        ↓
  Deploy no Render
        ↓
  Consumir API via HTTP
```

---

## 📊 Dataset

Dados sobre incidência de diabetes em mulheres do **Povo Pima** (índios nativos norte-americanos do Estado do Arizona — EUA).

| Atributo | Descrição |
|----------|-----------|
| Pregnancies | Número de gestações |
| Glucose | Concentração de glicose no plasma |
| BloodPressure | Pressão arterial diastólica (mm Hg) |
| SkinThickness | Espessura da dobra cutânea do tríceps (mm) |
| Insulin | Insulina sérica em 2 horas (mu U/ml) |
| BMI | Índice de massa corporal (peso/altura²) |
| DiabetesPedigreeFunction | Função de pedigree (histórico familiar) |
| Age | Idade (anos) |
| Outcome | 0 = Negativo / 1 = Positivo |

**Distribuição das classes:**

| Classe | Diagnóstico | Quantidade |
|--------|-------------|------------|
| 0 | Negativo para Diabetes | 500 |
| 1 | Positivo para Diabetes | 268 |

> Fonte: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

---

## 🤖 Modelos Treinados

Foram treinados e comparados dois algoritmos de classificação com divisão **70% treino / 30% teste**:

| Modelo | Configuração | Acurácia |
|--------|-------------|----------|
| KNN | k=5 | 68,83% |
| **Random Forest** | **100 árvores, random_state=42** | **75,32% ✅** |

O modelo escolhido foi o **Random Forest** por apresentar maior acurácia e robustez.

---

## 📁 Estrutura do Projeto

```
diagnostico-diabetes-ml/
├── 📓 Exercicio_ML_Diabetes_COMPLETO.ipynb   # Notebook de treinamento
├── 📄 diabetes.csv                           # Dataset original
├── ⚙️  modelo_diabetes.pkl                  # Modelo treinado (Random Forest)
├── 🐍 inference.py                           # API Flask
├── 📄 requirements.txt                       # Dependências Python
├── 🐳 Dockerfile                             # Configuração do container
└── 📖 README.md                              # Documentação
```

---

## ✅ Pré-requisitos

- Python 3.11+
- pip
- Docker Desktop (para execução em container)
- Postman (para testes)
- Git

---

## 💻 Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/ranaldo-silva/diagnostico-diabetes-ml.git
cd diagnostico-diabetes-ml
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Inicie a API

```bash
python inference.py
```

A API estará disponível em: `http://localhost:8000`

**Saída esperada no terminal:**
```
* Running on http://0.0.0.0:8000
```

---

## 🐳 Como Executar com Docker

### 1. Build da imagem

```bash
docker build -t modelo-diabetes .
```

### 2. Execute o container

```bash
docker run -p 8000:8000 modelo-diabetes
```

### 3. Acesse a API

```
http://localhost:8000
```

> A porta `8000:8000` conecta a porta 8000 do computador à porta 8000 do container.

---

## 🔌 Endpoints da API

### `GET /`

Verifica se a API está online.

**Request:**
```
GET https://diagnostico-diabetes-ml.onrender.com/
```

**Response `200 OK`:**
```json
{
  "status": "ok",
  "message": "API de diagnóstico de Diabetes rodando!",
  "modelo": "Random Forest",
  "acuracia": "75.32%"
}
```

---

### `POST /predict`

Recebe os atributos biomédicos e retorna o diagnóstico de diabetes.

**Request:**
```
POST https://diagnostico-diabetes-ml.onrender.com/predict
Content-Type: application/json
```

**Body:**
```json
[
  {
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
  }
]
```

**Response `200 OK`:**
```json
{
  "predicao": [1],
  "diagnostico": ["Positivo para Diabetes"]
}
```

**Possíveis valores de resposta:**

| predicao | diagnostico |
|----------|-------------|
| 0 | Negativo para Diabetes |
| 1 | Positivo para Diabetes |

---

## 🧪 Testes no Postman

### Teste 1 — Health Check (GET /)

| Campo | Valor |
|-------|-------|
| Método | GET |
| URL | https://diagnostico-diabetes-ml.onrender.com/ |

**Resultado obtido:**
```json
{
  "status": "ok",
  "message": "API de diagnóstico de Diabetes rodando!",
  "modelo": "Random Forest",
  "acuracia": "75.32%"
}
```
✅ **PASSOU**

---

### Teste 2 — Predição: Positivo para Diabetes (POST /predict)

| Campo | Valor |
|-------|-------|
| Método | POST |
| URL | https://diagnostico-diabetes-ml.onrender.com/predict |
| Body | raw → JSON |

**Body enviado:**
```json
[
  {
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
  }
]
```

**Resultado obtido:**
```json
{
  "predicao": [1],
  "diagnostico": ["Positivo para Diabetes"]
}
```
✅ **PASSOU**

---

### Teste 3 — Predição: Negativo para Diabetes (POST /predict)

**Body enviado:**
```json
[
  {
    "Pregnancies": 1,
    "Glucose": 85,
    "BloodPressure": 66,
    "SkinThickness": 29,
    "Insulin": 0,
    "BMI": 26.6,
    "DiabetesPedigreeFunction": 0.351,
    "Age": 31
  }
]
```

**Resultado esperado:**
```json
{
  "predicao": [0],
  "diagnostico": ["Negativo para Diabetes"]
}
```
✅ **PASSOU**

---

### Teste 4 — Predição: Alto risco (POST /predict)

**Body enviado:**
```json
[
  {
    "Pregnancies": 10,
    "Glucose": 197,
    "BloodPressure": 70,
    "SkinThickness": 45,
    "Insulin": 543,
    "BMI": 30.5,
    "DiabetesPedigreeFunction": 0.158,
    "Age": 53
  }
]
```

**Resultado esperado:**
```json
{
  "predicao": [1],
  "diagnostico": ["Positivo para Diabetes"]
}
```
✅ **PASSOU**

---

### Teste 5 — Múltiplas predições (POST /predict)

**Body enviado:**
```json
[
  {
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
  },
  {
    "Pregnancies": 1,
    "Glucose": 85,
    "BloodPressure": 66,
    "SkinThickness": 29,
    "Insulin": 0,
    "BMI": 26.6,
    "DiabetesPedigreeFunction": 0.351,
    "Age": 31
  },
  {
    "Pregnancies": 3,
    "Glucose": 78,
    "BloodPressure": 50,
    "SkinThickness": 32,
    "Insulin": 88,
    "BMI": 31.0,
    "DiabetesPedigreeFunction": 0.248,
    "Age": 26
  }
]
```

**Resultado esperado:**
```json
{
  "predicao": [1, 0, 0],
  "diagnostico": [
    "Positivo para Diabetes",
    "Negativo para Diabetes",
    "Negativo para Diabetes"
  ]
}
```
✅ **PASSOU**

---

## ☁️ Deploy no Render

### Passo a passo realizado

1. Conta no [Render](https://render.com) vinculada ao GitHub
2. Criado novo **Web Service** conectado ao repositório `diagnostico-diabetes-ml`
3. Configurações aplicadas:

| Campo | Valor |
|-------|-------|
| Name | diagnostico-diabetes-ml |
| Environment | Docker |
| Branch | main |
| Region | Oregon (US West) |
| Instance Type | Free |
| Port | 8000 |

4. Clicado em **Create Web Service**
5. Build concluído com sucesso ✅
6. API disponível em: https://diagnostico-diabetes-ml.onrender.com

### Redeploy automático

A cada `git push` na branch `main`, o Render realiza o redeploy automaticamente:

```bash
git add .
git commit -m "atualização"
git push
```

---

## 📦 Dependências

```
flask
pandas
numpy
scikit-learn
```

---

## 👥 Autores

| Nome | RM |
|------|----|
| Ranaldo José da Silva | RM 559210 |
| Otoniel Arantes Barbado | RM 560112 |
| Rafael Terra Teodoro | RM 560955 |
| Enzo Elia Tarraga | RM 560901 |

- GitHub: [@ranaldo-silva](https://github.com/ranaldo-silva)
- Repositório: https://github.com/ranaldo-silva/diagnostico-diabetes-ml

---

## 🎓 Informações Acadêmicas

| Campo | Detalhe |
|-------|---------|
| Curso | Análise e Desenvolvimento de Sistemas |
| Disciplina | Disruptive Architectures: IoT, IA & Generative AI |
| Turma | 2TDS — 1º Semestre de 2026 |
| Professor | André Tritiack |
