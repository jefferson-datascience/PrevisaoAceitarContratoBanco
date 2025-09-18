# 1.0 Objetivo do Projeto de Marketing - UCI Bank(Banco Português)

Nesse projeto, vamos trabalhar no modelo de negócio bancário com o produto de depósitos bancários à prazo. Para isso, vamos utilizar os dados públicos da UCI que nos traz os dados de um banco português. As habilidades que serão melhoradas e aperfeiçoadas aqui são análise de regressão, análise de clusters e modelagem de dados para problemas de classificação. 

# 2.0 Problema de Negócio

O setor de Marketing é vital para qualquer empresa — ele constrói a imagem institucional, direciona ações de prospecção, mantém clientes engajados e promove produtos para aumentar a relação do cliente com a marca. Entre suas diversas funções, está o disparo de campanhas por e-mail, SMS e WhatsApp para oferecer produtos e gerar conversões.
A instituição bancária portuguesa UCI Bank realiza ações de contratação de depósito bancário à prazo de seus clientes por meio de ações de telamarketing. Com o objetivo de melhorar essas ações, nos foi solitado estudos e análises para um melhor alocamento de recursos e construções de campanhas mais efetivas. Logo, aqui temos as seguintes perguntas a serem respondidas:

- E se pudéssemos prever a probabilidade de um cliente aceitar um contrato pela ligação?
- Será que existem grupos específicos em que a campanha é mais ou menos efetiva?
- Existe a possibilidade de entender quais variáveis influenciam um cliente abrir uma campanha?

## 2.1 Proposta de Solução
Para essa pergunta e para o objetivo do time de marketing, temos a seguinte proposta de solução: 

- Analisar os clientes que aceitaram ou não no passado para identificar clusters naturais. A partir disso, desenvolver um modelo preditivo capaz de antecipar a propensão de aceitação. Assim, gestores podem acessar indicadores estratégicos e analistas podem ter visão detalhada para ações de marketing.

## 2.2 Entrega Final:

* Estudo de variáveis que impactam a aceitação de contratos.
* Análise de clusters para identificar perfis de clientes e direcionar campanhas.
* Dashboard analítico para gestores e analistas, com indicadores de conversão e visão detalhada da base de clientes.

Para acessar todo a gestão do projeto, basta acessar esse link para ser direcionado para o documento que está aqui no github.

# 3.0 [Parte 1] - Análise de Regressão

## 3.1 Base Principal

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

## 3.2 Análise Exploratória de Dados

Com o entendimento das nossa variáveis, nos encaminhamos para uma análise exploratória dos dados para compreender se, os dados, são coerentes com o modelo de negócio apresentado. O processo nos levou ao seguinte resumo:

**Job:** As profissões de management, technician, blue-collar e admin são as mais frequentes, o que é esperado, já que representam grande parte do mercado de trabalho. Observa-se que management, technician e admin têm maior propensão a aceitar o contrato, possivelmente por apresentarem maior poder aquisitivo e, em geral, maior conhecimento financeiro.

**Marital:** 
O status married se destaca tanto em volume quanto em taxa de aceitação. Isso é consistente, pois pessoas casadas tendem a apresentar maior estabilidade financeira e, em alguns casos, contam com renda familiar combinada. No caso de solteiros, a ausência de despesas familiares também pode aumentar a disponibilidade de recursos, o que pode favorecer a adesão.

**Education:** A distribuição é coerente, já que boa parte da população possui apenas ensino fundamental (primary) ou médio (secondary). Proporcionalmente, indivíduos com ensino superior (tertiary) apresentam maior propensão a depósitos, possivelmente pelo acesso a cargos mais qualificados e maior conhecimento financeiro. Já aqueles com menor escolaridade tendem a ter menor adesão, reflexo de menor renda média e menor acesso a conhecimento financeiro.

**Default:** A variável é clara: clientes inadimplentes dificilmente aderem ao contrato, pois não dispõem de recursos extras. Já os clientes adimplentes apresentam maior propensão, confirmando a consistência do dado.

**Housing:** Clientes com financiamento imobiliário possuem compromissos de longo prazo que reduzem sua disponibilidade financeira para depósitos. Ainda assim, clientes com maior organização ou renda podem aderir. Proporcionalmente, os sem financiamento demonstram maior aceitação.

**Loan:** O mesmo raciocínio vale para empréstimos pessoais. Em geral, são utilizados para quitação de dívidas ou consumo imediato, reduzindo a disponibilidade de recursos para depósitos.

**Contact:** Contatos via celular têm maior efetividade, já que normalmente permitem falar diretamente com o cliente. Por telefone fixo, há mais barreiras, como terceiros atendendo ou indisponibilidade. Isso explica a maior aceitação quando o contato é feito por celular.

**Month:** Observa-se maior adesão nos meses de maio a agosto. No entanto, não há informações suficientes para identificar o motivo. É necessário validar com as áreas de negócio se existem fatores sazonais ou campanhas específicas nesses períodos.

**Poutcome:** Clientes que já tiveram experiências positivas em ofertas anteriores tendem a aceitar novas, o que reforça a importância de um bom relacionamento e histórico de satisfação.

**Age:** A faixa entre 30 e 60 anos corresponde ao período de maior produtividade financeira, em que há busca por investimentos, depósitos e meios de pagamento. Por isso, essa faixa etária apresenta maior adesão.

**Balance:** A maioria dos clientes apresenta saldos médios baixos, o que é esperado, já que a base é composta, em grande parte, por blue-collar, admin, aposentados (retired), desempregados (unemployed), empregados domésticos (housemaid), estudantes (student) e autônomos (self-employed). Apenas uma minoria possui saldos médios elevados.

**Day:** Não se observa relação relevante entre o dia do contato e a adesão ao contrato. Portanto, essa variável não gera conclusões significativas.

**Duration:** O comportamento é esperado em telemarketing: muitas ligações são encerradas rapidamente (duração zero). Quando o cliente permanece ouvindo a proposta, a chance de conversão aumenta, o que é refletido no histograma.

**Campaign:** A cada nova tentativa de contato, a chance de aceitação diminui. Em geral, recusas iniciais reduzem a probabilidade de sucesso em ligações subsequentes. Assim, os dados são consistentes com o comportamento esperado.

**Pdays:** Intervalos moderados entre contatos podem favorecer a aceitação, já que permitem maturação da ideia. Porém, intervalos muito longos podem reduzir a eficácia, devido a mudanças no perfil ou nas condições do cliente.

**Previous:** Um histórico positivo de relacionamento com o banco reduz barreiras e aumenta a aceitação de novos produtos. Portanto, a variável se mostra coerente.

## 3.3 Tratamento de Dados

Com os dados consistentes, na fase de tratamento de dados, realizamos um estudo de outliers sobre os nossos dados. Era esperado em, algumas variáveis, a presença de outliers. Por exemplo, variáveis como saldo médio e duração de ligação.
Durante o tratamento observou-se que os outliers eram esperados e, nessa situação, não poderíamos desconsiderá-los. Sendo assim, parte dessa tratativa deixamos para a fase de pré-processamento de dados e, também, para a fase de engenharia de atributos.

## 3.4 Engenharia de Atributos

Na fase da engenharia de atributos, realizamos alteramos as variáveis numéricas age, day e pdays para a visão de faixas, tornando elas categóricas.

**Balanceamento dos Dados**: Após as devidas tratativas, realizamos o balanceamento dos dados utilizando o método de subamostragem da classe majoritária.

## 3.5 Pré-Processamento dos Dados

Na etapa de pré-processamento de dados utilizamos encoders clássicos como OrdinalEncoder, OneHotEncoder. Após tudo estar em formato numérico, padronizamos para colocar tudo sobre a mesma escala, aplicando o StandardScaler.

## 3.6 Análise de Regressão

Com o objetivo de entender como as variáveis independentes impactam na nossa variável alvo, que no caso, é a aceitação ou não do depósito bancário, utilizamos a regressão logística para obter os coeficiente de cada variável independente. Com uma regressão logística com uma capacidade de aprendizado de:


|Métrica| Score|
|-------|------|
| AUC Score | 87.5%|
| Precisão  | 80.0%|
| Recuperação | 79.3%|
| F1-Score | 79.8% |

Podemos extrair insights confiáveis e significativos. Segue abaixo o relatório:

* *duration*(1.9): Clientes que passam mais tempo em ligações tendem a ter maior probabilidade de aceitar o contrato. Isso sugere estratégias para captação e retenção do cliente nos primeiros momentos de contato.

* *pdays*(0.309): Quanto maior o tempo sem contato o cliente possui em relação a campanha anterior, maior a tendência da probailidade de aceitar o contrato. Isso sugere que uma saturação de ofertas pode atrapalhar na captação e, em uma possível, conversão do cliente.

* *retired*(0.201): Clientes aposentados tendem aceitar o contrato. Isso sugere que aposentados querem construir recurso para uma possíveis planejamentos.

* *previous*(0.194): Antes dessa campanha entrar em vigor, clientes com mais frequência de contato têm maior probabilidade de aceitar o contrato. Isso sugere que, um clientes que possuem uma relação saudável com a instituição (analisando a variável pdays), em termos de contato, estão mais propenso a aceitar o contrato.

* *student*(0.163): Clientes que são estudantes têm uma maior probabilidade de aceitar o contrato. Isso sugere, esses clientes, estão construindo uma poupança ou algo dessa natureza, para irem para a faculdade, realizarem um intercâmbio ou obterem um bem-material.

* *education*(0.14): Clientes com maiores níveis educacionais tendem a um maior a probabilidade dele aceitar o contrato. Isso sugere, que clientes com uma formação mais robusta possuem um planejamento financeiro o qual permitem eles de realizarem depósitos à prazo. 

* *admin.*(0.10): Clientes que são administradores tendem a ter uma maior probabilidade de aceitar o contrato. Isso sugere que administradores possuem uma melhor planejamento financeiro para poder realizar esse depósitos.

* *divorced*(0.099): Clientes divorciados possuem maior probabilidade de aceitar o contrato.

* *managment*(0.093): Empresário possuem a probabilidade de aceitar o contrato.

* *balance(0.085):* Quanto maior o saldo médio em conta de um cliente ocorre uma maior tendência de aumento da probabilidade de aceitar um contrato. Isso sugere que clientes 

* As variáveis:

    * *unemployed*
    * *unknow_job*
    * *married*
    * *month*
    * *celullar*
    * *unknow_contact*
    * *technician*
    * *age*
    * *day*
    * *services*
    * *housemaid*
    * *enterpreneur*
    * *single*
    * *self-empolyed*


não impactam na probabilidade de aceitar um contrato ou não, uma vez que, colocamos o critério de coeficiente entre 0.05 e -0.05 como não válidos.

* *blue-collar*(-0.069): Clientes de colarinho azul possuem tendem a menos probabilidade de aceitar o contrato. Isso sugere que, esses clientes, por terem salário mais baixos, não possuem capital para realizar depósitos à prazo.

* *default*(-0.227): Clientes que são inadimplentes tendem a ter menos probabilidade de aceitar o contrato. Isso sugere que, o fato da inadimplência iimplica que a prioridade não seria a construção de uma renda, mas sim, a quitação dessa dívida.

* *loan*(-0.299): Clientes que possuem empréstimos tendem a ter menos probabilidade de aceitar o contrato. Isso sugere que, um empréstimo pessoal compromete o orçamento do cliente, o que impede de realizar aportes para depósitos.

* *housing*(-0.496): Idem da variável anterior.

* *telephone*(-0.514): Clientes que são contatados por telefone fixo tem uma baixa probabilidade de aceitar o contrato. Isso sugere que, é muito fácil para o cliente esquivar de tais ofertas, pois, não necessariamente é o cliente que atende, mas sim, outra pessoa.


## 3.7 Recomendações

1º) Construções de estratégias para captação, retenção e prolongamento da ligação com o clientes.

2º) Planejamento para equilibrar a frequência de ofertas e o tempo de ficar sem contato para a maturação de ideia e, até, uma nova oferta.

3º) Produtos de depósitos bancários  personalizados para clientes que são aposentados, estudantes e admnistradores, empresários.

4º) Análise de saldo meédio de clientes para oferta do depósito

5º) Foco em clientes com um formação educacional mais elevada.

6º) Evitar clientes que já possuem algum comprometimento financeiro como empréstimos, financiamentos e inadimplências.

7º) Analisar viabilidade de outro produto para clientes de colarinho azul ou adaptação do produto ofertado.

8º) Evitar ao máximo contato por telefone. Sempre que possível, entrar em contato com o cliente pelo celular pessoal dele.
