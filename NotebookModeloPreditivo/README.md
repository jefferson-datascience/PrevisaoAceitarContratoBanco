# Desenvolvimento de Modelo Preditivo para Aceitação de Contrato

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
Durante o tratamento observou-se que os outliers eram esperados e, nessa situação, não poderíamos desconsiderá-los. Sendo assim, parte dessa tratativa deixamos para a fase de pré-processamento de dados e, também, para a fase de engenharia de atributos. Para além disso, eliminamos colunas desnecessárias para a nossa modelagem preditiva, no caso, as variáveis day e month e, também, selecionamos apenas os dados cujas ligações duraram mais de 30 segundos pelo menos, pois, entendemos, que com esse tempo pode se ter pelo menos uma apresentação breve e um prospecção inicial.

## 4.0 Engenharia de Atributos

Na fase da engenharia de atributos, realizamos alteramos a variável numérica pdays para a visão de faixas, tornando ela categórica.

## 5.0 Pré-Processamento dos Dados

Na etapa de pré-processamento de dados construímos nosso pipeline para o encoding das variáveis utilizando encoders clássicos como OrdinalEncoder, OneHotEncoder.

## 6.0 Balanceamento dos Dados

Realizamos o balanceamento dos dados utilizando o método de subamostragem da classe majoritária.

## 7.0 Separação: Treino, Teste e Validação
 
Com os nossos dados devidamente tratados, com as features novas criadas e balanceados, separamos o nosso dataset em treino, teste e validação sendo que, os dados de treino possuem 70% dos dados e teste e validação possuem, cada um, 15% dos dados.

## 8.0 Aprendizado de Máquina

Nessa fase, vamos treinar algoritmos de aprendizado de máquina para aprender os padrões do nossos dados e, a partir disso, vamos verificar se, de fato, nossos dados possuemm algum padrão por meio da performance dos modelo. De modo a facilitar essa etapa e realizar o deploy dos modelos, vamos construir pipelines para cada modelo. Nessa etapa, pelo fato de os dados possuírem um bom padrão, 3 modelos básicos conseguiram uma boa apredizagem e generalização. Os 3 modelos utilizados foram a Regressão Logística, Decision Tree e KNN.

### Capacidade de Aprendizado

Nossos modelos tiveram as seguintes capacidades de aprendizado:

|       Modelos       |  AUC  | Precisão | Recuperação |
| ------------------- | ----- | -------- | ----------- |
| Regressão Logística | 89.0% |   83.1%  |    78.6%    |
|    Decision Tree    | 87.7% |   81.2%  |    78.3%    |
|         KNN         | 92.7% |   84.2%  |    84.8%    |

### Capacidade de Generalização

Nossos modelos tiveram as seguintes capacidades de generalização:

|       Modelos       |  AUC  | Precisão | Recuperação |
| ------------------- | ----- | -------- | ----------- |
| Regressão Logística | 89.3% |   81.4%  |    79.1%    |
|    Decision Tree    | 85.2% |   78.7%  |    75.3%    |
|         KNN         | 85.0% |   78.2%  |    78.9%    |

Na determinação da escolha dos nossos modelos, podemos ver que KNN aprende bem, mas sua performance cai de forma bem agressiva na generalização, nos indicando uma instabilidade muito grande do modelo. Logo, nos resta apenas a Decision Tree e a Regressão Logística. Se fossemos analisar apenas números, escolheriamos a Regressão Logística, pois manteve ótimas métricas no aprendizado e, na generalização variou pouco. Entretanto, é importante sempre considerar complexidade do modelo. Uma vez que a regressão logística é menos complexa que a decision tree e sua performance é relativamente superior, cravamos decision tree como modelo escolhido.

## 9.0 Validação Cruzada

Na validação cruzada, nosso objetivo é verificar se, de fato, nosso modelo é performático, independente da partição do dataset que ele obtenha para aprendizado. Isto é, o que queremos aqui é verificar se nosso modelo é perfomático apenas pela coincidência de ter obtido uma parte boa do dataset para treinamento. Analisando as métricas de AUC, Precisão e Recuperação com um cross-validation de 5 partições, temos as seguintes Métricas:

|   Métricas  | Média | Desvio Padrão |
| ----------- | ----- | ------------- |
|      AUC    | 89.0% |      0.41%    |
|   Precisao  | 83.0% |      0.91%    |
| Recuperação | 79.0% |      0.27%    |

Por fim, temos um modelo super estável. 
Com um modelo bem performático e estável, vamos para a etapa da otimização do Threshold.

## 10. Otimização do Thershold

Nessa etapa queremos otimizar o threshold para a métrica roc-auc com o intuito de maximizar a identificação dos verdadeiros positivos e minimizar a identificação dos falso-positvos. O melhor corte escolhido foi o de 0.447 e obtivemos as seguintes métricas com os dados de teste, isto é, dados nunca antes vistos.

|   Métricas  | Valor |
| ----------- | ----- |
|      AUC    | 88.8% |
|   Precisao  | 80.7% |
| Recuperação | 81.6% |  

## Projeções de Ganhos com o Modelo

Ao analisarmos a base original, observamos que a taxa de conversão atual para contratos de depósitos a prazo é de 13%. Isso significa que, a cada 100 prospecções realizadas, apenas 13 clientes efetivamente fecham um contrato. A partir desse cenário, estimamos o ganho potencial com o uso do modelo de classificação.

No status quo, existem 13 clientes realmente interessados em cada grupo de 100 clientes. Considerando que o modelo possui 81% de recall, ele seria capaz de identificar aproximadamente 10 desses 13 clientes.

Além disso, com uma precisão de 80%, significa que, para cada conjunto de visitas recomendadas pelo modelo, 80% correspondem a clientes realmente interessados. Portanto, para localizar esses mesmos 10 clientes identificados pelo modelo, precisamos resolver:

80% × x = 10
x = 10 / 0.8
x ≈ 13 visitas

Ou seja, o modelo precisa de aproximadamente 13 visitas qualificadas para encontrar 10 clientes interessados.

Se quisermos encontrar os mesmos 13 clientes que seriam encontrados no cenário atual, o cálculo fica:

80% × x = 13
x = 13 / 0.8
x ≈ 16 visitas

Isso representa uma redução significativa no esforço de prospecção:

100 visitas no cenário atual para encontrar 13 clientes vs. 16 visitas com o modelo para encontrar os mesmos 13 clientes

O que corresponde a uma redução de aproximadamente 84% no volume de prospecções necessárias.

Portanto, o principal ganho trazido pelo modelo é a eficiência operacional: conseguimos identificar praticamente o mesmo número de clientes interessados com um volume muito menor de visitas, direcionando o time comercial para leads com maior probabilidade de conversão e reduzindo substancialmente o esforço comercial necessário


