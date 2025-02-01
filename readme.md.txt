# 📊 Análise do Mercado Imobiliário - SCOD Brasil

Este projeto analisa a saturação do mercado imobiliário no Brasil, avaliando a relação entre a população de **38 a 58 anos** e o **número de empresas ativas no setor de construção** por estado, no período de **2007 a 2022**. O objetivo é identificar **estados saturados** e **oportunidades futuras** no setor.

---

## 📌 **Objetivo do Projeto**
- **Coletar dados do SIDRA/IBGE** sobre empresas ativas no setor da construção.
- **Coletar dados populacionais do IBGE** e filtrar a faixa etária de 38 a 58 anos.
- **Calcular a razão entre população e empresas ativas** por estado.
- **Prever os anos de 2021 e 2022** com modelos estatísticos.
- **Agrupar estados com comportamentos semelhantes** para identificar saturação e oportunidades.

---

## 📂 **Estrutura do Projeto**
📁 `main.py` - Arquivo principal que executa todo o pipeline  
📁 `coletar_dados.py` - Código para coletar dados do SIDRA/IBGE  
📁 `tratar_dados.py` - Processa os dados e calcula a razão População/Empresas  
📁 `previsao.py` - Faz previsão para 2021 e 2022  
📁 `clusterizacao.py` - Agrupa os estados e identifica oportunidades  
📁 `visualizar.py` - Gera gráficos para análise  
📁 `README.md` - Explicação detalhada do projeto  
📁 `requirements.txt` - Lista de dependências do projeto  

---

## 🚀 **Como Rodar o Projeto**
### **1️⃣ Clonar o Repositório**
```bash
git clone https://github.com/seuusuario/scod-imobiliario.git
cd scod-imobiliario
