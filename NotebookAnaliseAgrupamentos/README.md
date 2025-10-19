# Análise de Regressão

## 1.0 Base Principal

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

## 2.0 Análise Exploratória de Dados

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

## 3.0 Tratamento de Dados

Com os dados consistentes, na fase de tratamento de dados, realizamos um estudo de outliers sobre os nossos dados. Era esperado em, algumas variáveis, a presença de outliers. Por exemplo, variáveis como saldo médio e duração de ligação.
Durante o tratamento observou-se que os outliers eram esperados e, nessa situação, não poderíamos desconsiderá-los. Sendo assim, parte dessa tratativa deixamos para a fase de pré-processamento de dados e, também, para a fase de engenharia de atributos.

## 4.0 Engenharia de Atributos

Na fase da engenharia de atributos, realizamos alteramos as variáveis numéricas age, day e pdays para a visão de faixas, tornando elas categóricas.

**Balanceamento dos Dados**: Após as devidas tratativas, realizamos o balanceamento dos dados utilizando o método de subamostragem da classe majoritária.

## 5.0 Pré-Processamento dos Dados

Na etapa de pré-processamento de dados utilizamos encoders clássicos como OrdinalEncoder, OneHotEncoder. Após tudo estar em formato numérico, padronizamos para colocar tudo sobre a mesma escala, aplicando o StandardScaler.

## 6.0 Clusterização dos Grupos

Nessa etapa, com o objetivo de obter grupos naturais, aplicamos dois algoritmos de clusterização, no caso, KMeans e Gaussian Mixture. Aplicando o método do Cotovelo, chegamos a conclusão que a melhor quantidade de cluster é três. Ao analisar as métricas de Silhouette Score e Davies-Boulding com essa quantidade de cluster, temos que o Gaussian Mixture realiza a melhor clusterização.

Segue as métricas de avaliação abaixo para três clusters:


|      Modelos     | Métrica Silhouette | Métrica Davies-Bouldin |
| ---------------- |--------------------| -----------------------|
|       KMeans     |         0.16       |         2.06           |
| Gaussian Mixture |         0.14       |         3.06           |

## 8.0 Análise dos Clusters

**Prospects** (Representação de 68% do conjunto de dados)

* O perfil médio desse grupo é composto por indivíduos de 39 anos, geralmente empregados em funções operacionais (colarinho azul) ou atuando como empresários e gestores, casados e com ensino médio completo.

* Do ponto de vista financeiro, esses clientes não apresentam inadimplência, possuem saldo médio de R$ 1.142,17 e não possuem empréstimos pessoais ativos.

* No que se refere à campanha e aos contatos realizados, observa-se que o principal canal de comunicação é o telefone celular, com ligações que duram, em média, 259 segundos — aproximadamente quatro a cinco minutos


**Prospects Sêniors**(Representação de 13% do conjunto de dados)

* O perfil médio dos clientes desse grupo é de 49 anos, sendo majoritariamente aposentados, empreendedores ou empregados domésticos, com ensino médio completo.

* Do ponto de vista financeiro, esses clientes não apresentam inadimplência, possuem saldo médio de R$ 2.191,00, não possuem financiamento imobiliário nem empréstimo pessoal ativo.

* No que se refere à campanha e aos contatos realizados, são clientes abordados tanto por telefone fixo quanto por celular, com ligações que duram, em média, 247 segundos — aproximadamente quatro a cinco minutos. Além disso, observa-se que esses clientes foram contatados, em média, três vezes durante a campanha, sem nenhum histórico de contato anterior em campanhas passadas.

**Reengajáveis**(Representação de 19% do conjunto de dados)

* O perfil médio desse grupo é composto por indivíduos de 40 anos, geralmente empregados em funções operacionais (colarinho azul) ou atuando como empresários e gestores, casados e com ensino médio completo.

* Do ponto de vista financeiro, esses clientes não apresentam inadimplência, possuem saldo médio de R$ 1.556,88, têm financiamento imobiliário ativo e não possuem empréstimo pessoal.

* No que se refere à campanha e aos contatos realizados, são clientes contatados principalmente por celular, com ligações que duram, em média, 260 segundos — aproximadamente quatro a cinco minutos. Além disso, observa-se que esses clientes foram contatados, em média, duas vezes durante a campanha atual. Estão há mais de seis meses sem contato anterior e, historicamente, recebiam cerca de três contatos em campanhas anteriores. Na última campanha, contudo, não houve conversão, indicando ineficiência na ação anterior.


