# 1.0 Objetivo do Projeto de Marketing - UCI Bank(Banco Português)

Nesse projeto, vamos trabalhar no modelo de negócio bancário com o produto de depósitos bancários à prazo. Para isso, vamos utilizar os dados públicos da UCI que nos traz os dados de um banco português. As habilidades que serão melhoradas e aperfeiçoadas aqui são análise de regressão, análise de clusters e modelagem de dados para problemas de classificação. 

## 2.0 Problema de Negócio

O setor de Marketing é vital para qualquer empresa — ele constrói a imagem institucional, direciona ações de prospecção, mantém clientes engajados e promove produtos para aumentar a relação do cliente com a marca. Entre suas diversas funções, está o disparo de campanhas por e-mail, SMS e WhatsApp para oferecer produtos e gerar conversões.
A instituição bancária portuguesa UCI Bank realiza ações de contratação de depósito bancário à prazo de seus clientes por meio de ações de telamarketing. Com o objetivo de melhorar essas ações, nos foi solitado estudos e análises para um melhor alocamento de recursos e construções de campanhas mais efetivas. Logo, aqui temos as seguintes perguntas a serem respondidas:

- E se pudéssemos prever a probabilidade de um cliente aceitar um contrato pela ligação?
- Será que existem grupos específicos em que a campanha é mais ou menos efetiva?
- Existe a possibilidade de entender quais variáveis influenciam um cliente abrir uma campanha?

### 2.1 Proposta de Solução
Para essa pergunta e para o objetivo do time de marketing, temos a seguinte proposta de solução: 

- Analisar os clientes que aceitaram ou não no passado para identificar clusters naturais. A partir disso, desenvolver um modelo preditivo capaz de antecipar a propensão de aceitação. Assim, gestores podem acessar indicadores estratégicos e analistas podem ter visão detalhada para ações de marketing.

### 2.2 Entrega Final:

* Estudo de variáveis que impactam a aceitação de contratos.
* Análise de clusters para identificar perfis de clientes e direcionar campanhas.
* Dashboard analítico para gestores e analistas, com indicadores de conversão e visão detalhada da base de clientes.

Para acessar todo a gestão do projeto, basta acessar esse link para ser direcionado para o documento que está aqui no github.

## 3.0 [Parte 1] - Análise de Regressão

### 3.1 Base Principal

Na primeira etapa de um projeto é entender as variáveis que estamos trabalhando e que informações elas carregam.

Logo abaixo, temos o dicionário das variáveis.

| Variable Name | Description |
|---------------|-------------------|
|     age       |   Idade do Cliente| 
|     job       | 	Tipo do trabalho. Temos as seguintes categorias: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown'.|
|    marital    |   Status Matrimonia. Categorias: 'divorced','married','single','unknown'. |
|   education   |   Nível educacional do cliente. Categorias: 'primary', 'secondary', 'tertiary' |
|    default    |   Essa variável nos diz se o cliente é inadimplente. Categorias: 'yes', 'no'. |
|    balance    |   Saldo médio anual do cliente na conta, cuja unidade é em euros. |
|    housing    |   Possui financiamento imobiliário? Categorias: 'yes', 'no'.|
|    loan       |   Possui empréstimo pessoal? Categorias: 'yes', 'no'. |
|    contact    |   Meio de contato utilizado para falar com o cliente. Categorias: 'celular', 'telephone'.|
|  day_of_week  |   Último Dia da semana em que o contato foi feito. |
|     month     |   Último mês de contato com o cliente. |
|   duration    |   Duração da ligação, em segundos, da última ligação. |
|   campaign    |   Número de contatos realizados com o cliente durante a campanha atual. |
|    pdays      |   Número de dias que se passaram desde o último contato com o cliente em uma campanha anterior. Se a variável -1, então o cliente não foi contatado. |
|   previous    |   Número de contatos realizados com o clientes antes dessa campanha. |
|   poutcome    |   Resultado da campanha anterior de marketing. |
|      y        |   Variável alvo para saber se o cliente assinou ou não termo de depósito. Categorias: 'failure','nonexistent','success'. |




