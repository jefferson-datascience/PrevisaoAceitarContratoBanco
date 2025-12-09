# 0.0 Pacotes e Bibliotecas

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1.0 Carregamento dos Dados

# ============================================================== Escrita da Primeira Página ===============================================================
st.set_page_config(layout='wide')

# Configurações da barra lateral
st.sidebar.subheader('Navegue pelo Projeto', divider='gray', width='stretch')
# Conteúdo na barra lateral


pagina = st.sidebar.selectbox("",["Apresentação", "Estudo de Variáveis", "Análise de Agrupamento", "Resultados Modelo Preditivo", "Dashboard"])

st.sidebar.markdown(
    """
    ### 🌐 Meus Contatos
    <div class="sidebar-links">
        <a href="https://www.linkedin.com/in/jeffersonhenriquecandido/" target="_blank">🔗 LinkedIn</a>
    </div>
    <div class="sidebar-links">
        <a href="https://github.com/jefferson-datascience" target="_blank">💻 GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)


caminho = "https://github.com/jefferson-datascience/PrevisaoAceitarContratoBanco/blob/main/ScriptProdutoFinal/"

if pagina == "Apresentação":


    st.header('Projeto de Ciência de Dados - Marketing\n', width='stretch')

    st.image(r"https://github.com/jefferson-datascience/PrevisaoAceitarContratoBanco/blob/main/ScriptProdutoFinal/LogoMarketing1.jpg", width='stretch')

    st.subheader('Apresentação', divider='gray')

    st.text('Seja bem-vindo em mais um novo projeto realizado por mim. O objetivo desse projeto é aprimorar habilidades Ciências de Dados voltadas para a análise de variáveis utilizando técnicas de regressão em problemas de classificação, ' \
            'análise de agrupamentos para identificação de melhores grupos e desenvolvimento de modelos de classificação. Para atingir esse objetivo, vamos trabalhar com desafio de assinatura de contratos de depósitos bancários ' \
            'à prazo de um banco português. Daremos o nome fictício a ele de UCI-Bank.', width='stretch') 

    st.subheader('Problema de Negócio', divider='gray', width='stretch')

    st.text('O setor de Marketing é vital para qualquer empresa — ele constrói a imagem institucional, direciona ações de prospecção, mantém clientes engajados e promove produtos para aumentar a relação do cliente com a marca. ' \
            'Entre suas diversas funções, está o disparo de campanhas por e-mail, SMS e WhatsApp para oferecer produtos e gerar conversões.A instituição bancária portuguesa UCI Bank realiza ações de contratação de depósito bancário' \
            'à prazo de seus clientes por meio de ações de telamarketing. Com o objetivo de melhorar essas ações, nos foi solicitado estudos e análises para um melhor alocamento de recursos e construções de campanhas mais efetivas.', width='stretch')

    st.text('Após reuniões e conversas com os gerentes e analistas do Marketing, conseguimos resumir os problemas em três perguntas principais a serem respondidas. São elas:', width='stretch')
    st.markdown(' * E se pudéssemos prever a probabilidade de um cliente aceitar um contrato pela ligação?\n' \
                ' * Será que existem grupos específicos em que a campanha é mais ou menos efetiva?\n ' \
                ' * Existe a possibilidade de entender quais variáveis influenciam um cliente abrir uma campanha?', unsafe_allow_html=False, width='stretch')

    st.subheader('Proposta de Solução', divider='gray', width='stretch')

    st.text('Para responder essas perguntas propomos analisar os clientes que aceitaram ou não no passado para identificar clusters naturais. e, a partir disso, desenvolver um modelo preditivo capaz de antecipar a propensão de aceitação.'
            'Assim, gestores podem acessar indicadores estratégicos e analistas podem ter visão detalhada para ações de marketing. Para além disso, como entrega final sugerimos:', width='stretch')

    st.markdown('* Estudo de variáveis que impactam a aceitação de contratos. \n'
                '* Análise de clusters para identificar perfis de clientes e direcionar campanhas. \n' \
                '* Dashboard analítico para gestores e analistas, com indicadores de conversão e visão detalhada da base de clientes.', width='stretch') 

    st.text('Logo ao lado, você verá uma barra de navegação com os resultados de cada tópico e, além disso, um link que leva para ao meu github onde terá, com mais detalhes, todo o desenvolvimento do projeto, isto é metodologias aplicadas, ciclos de entrega, ' \
            'e planejamentos.', width='stretch')

    st.subheader('Próximos Passos', divider='gray')

    st.text('Como próximos passos temos: ', width='stretch')
    st.markdown('* Teste estatístico para validação do nosso modelo. \n' \
                '* Treinamento de equipes para utilização do dashboard para ações. \n'
                '* Apresentação dos estudos realizados.', width='stretch')

elif pagina == "Estudo de Variáveis":

    st.header('Impacto das Variáveis nas Assinatura dos Contratos', divider='gray', width='stretch')

    st.image("LogoMarketing2.jpg")

    st.text('A primeira etapa em nosso projeto era entender como certas variáveis impactavam no assinatura de um contrato de depósito bancário à prazo. Para a realização desse estudo, desenvolvemos toda ' \
            'uma modelagem de dados, ideação de novas features e excução das devidas trativas para aplicar uma regressão logística e extrair esses fatores que nos mostrariam os impactos das variáveis no assinatura do ' \
            'contrato. Por fim, desenvolvemos um regressão logística com as seguintes performances: ', width='stretch')
    st.markdown(" * AUC Score: 87.5%; \n" \
                " * Precisão: 80.0%; \n" \
                " * Recuperação: 79.3% \n" \
                " * F1-Score: 79.8%", width='stretch')
    st.text('Portanto, temos um modelo que aprendeu razoavelmente bem os padrões e, com isso, podemos realizar, com segurança, o estudo. Logo Abaixo, temos o nosso relatório.')
    st.markdown(" * **duration**(1.9): Clientes que passam mais tempo em ligações tendem a ter maior probabilidade de aceitar o contrato. Isso sugere estratégias para captação e retenção do cliente nos primeiros momentos de contato.\n "
                " * **pdays**(0.309): Quanto maior o tempo sem contato o cliente possui em relação a campanha anterior, maior a tendência da probailidade de aceitar o contrato. Isso sugere que uma saturação de ofertas pode atrapalhar\n " \
                "na captação e, em uma possível, conversão do cliente.\n " \
                " * **retired**(0.201): Clientes aposentados tendem aceitar o contrato. Isso sugere que aposentados querem construir recurso para uma possíveis planejamentos.\n " \
                " * **previous**(0.194): Antes dessa campanha entrar em vigor, clientes com mais frequência de contato têm maior probabilidade de aceitar o contrato. Isso sugere que, " \
                "um clientes que possuem uma relação saudável com a instituição (analisando a variável pdays), em termos de contato, estão mais propenso a aceitar o contrato. \n"
                " * **student**(0.163): Clientes que são estudantes têm uma maior probabilidade de aceitar o contrato. Isso sugere, esses clientes, estão construindo uma poupança ou algo dessa " \
                "natureza, para irem para a faculdade, realizarem um intercâmbio ou obterem um bem-material.\n "
                " * **education**(0.14): Clientes com maiores níveis educacionais tendem a um maior a probabilidade dele aceitar o contrato. Isso sugere, que clientes com uma formação mais " \
                "robusta possuem um planejamento financeiro o qual permitem eles de realizarem depósitos à prazo.\n "
                " * **admin.**(0.10): Clientes que são administradores tendem a ter uma maior probabilidade de aceitar o contrato. Isso sugere que administradores possuem uma melhor planejamento " \
                "financeiro para poder realizar esse depósitos.\n "
                " * **blue-collar**(-0.069): Clientes de colarinho azul possuem tendem a menos probabilidade de aceitar o contrato. Isso sugere que, esses clientes, por terem salário mais baixos, " \
                "não possuem capital para realizar depósitos à prazo.\n "
                " * **default**(-0.227): Clientes que são inadimplentes tendem a ter menos probabilidade de aceitar o contrato. Isso sugere que, o fato da inadimplência iimplica que a prioridade não " \
                "seria a construção de uma renda, mas sim, a quitação dessa dívida.\n "
                " * **loan**(-0.299): Clientes que possuem empréstimos tendem a ter menos probabilidade de aceitar o contrato. Isso sugere que, um empréstimo pessoal compromete o orçamento do cliente," \
                "o que impede de realizar aportes para depósitos.\n "
                " * **housing**(-0.496): Idem da variável anterior.\n" \
                " * **telephone**(-0.514): Clientes que são contatados por telefone fixo tem uma baixa probabilidade de aceitar o contrato. Isso sugere que, é muito fácil para o cliente esquivar de tais " \
                "ofertas, pois, não necessariamente é o cliente que atende, mas sim, outra pessoa.\n", width='stretch')

    st.subheader('Recomendações baseadas no Estudo', width='stretch', divider='gray')
    st.markdown("1. Construções de estratégias para captação, retenção e prolongamento da ligação com o clientes.\n" \
                "2. Planejamento para equilibrar a frequência de ofertas e o tempo de ficar sem contato para a maturação de ideia e, até, uma nova oferta.\n" \
                "3. Produtos de depósitos bancários  personalizados para clientes que são aposentados, estudantes e admnistradores, empresários.\n" \
                "4. Análise de saldo meédio de clientes para oferta do depósito.\n" \
                "5. Foco em clientes com um formação educacional mais elevada.\n" \
                "6. Evitar clientes que já possuem algum comprometimento financeiro como empréstimos, financiamentos e inadimplências.\n" \
                "7. Analisar viabilidade de outro produto para clientes de colarinho azul ou adaptação do produto ofertado.\n" \
                "8. Evitar ao máximo contato por telefone. Sempre que possível, entrar em contato com o cliente pelo celular pessoal dele.", width='stretch')

    st.subheader('Observações', width='stretch', divider='gray')
    st.markdown(""" Para acessar os detalhes de construção e os códigos desse estudo, acesse esse link: <a href="https://github.com/jefferson-datascience/PrevisaoAceitarContratoBanco/tree/main/NotebooksAnaliseRegressao" target="_blank">Github do Projeto </a> """, unsafe_allow_html=True)

elif pagina == "Análise de Agrupamento":

    st.header('Análise de Grupos', width='stretch', divider='gray')
    
    st.image(r"https://raw.githubusercontent.com/jefferson-datascience/PrevisaoAceitarContratoBanco/blob/main/ScriptProdutoFinal/LogoMarketing3.png", width='stretch', clamp=True, channels='RGB')
    
    st.text('A segunda etapa do nosso projeto era encontrar perfis naturais do nosso conjunto de dados. Isto é, dada as características dos nossos clientes como emprego, idade, saldo médio em conta, tempo em telefone e, ' \
            'outras características, conseguiriamos entender quais grupos naturais existiriam em nosso dataset de modo a conseguir organizar melhor as campanhas. Para atingir esse objetivo, utilizamos machine learning para encontrar' \
            'os melhores grupos. A partir da técnica do cotovelo, o modelo Gaussian Mixture nos retornou os melhores três clusters. Segue abaixo as métricas que utilizamos para avaliar a separação: ', width='stretch')
    st.markdown('* Silhouette Score: 0.14. \n' \
                '* Davies-Boudin: 3.06.')
    st.text('A partir desse separação, temos a seguinte análise dos clusters encontrados:\n ')
    st.markdown(" **Prospects** (Representação de 68\% do conjunto de dados):\n"
                "   * O perfil médio desse grupo é composto por indivíduos de 39 anos, geralmente empregados em funções operacionais (colarinho azul) ou atuando como empresários e gestores, casados e com ensino médio completo.\n"
                "   * Do ponto de vista financeiro, esses clientes não apresentam inadimplência, possuem saldo médio de R$ 1.142,17 e não possuem empréstimos pessoais ativos.\n"
                "   * No que se refere à campanha e aos contatos realizados, observa-se que o principal canal de comunicação é o telefone celular, com ligações que duram, em média, 259 segundos — aproximadamente quatro a cinco minutos.\n"
                "\n**Prospects Sêniors**(Representação de 13\% do conjunto de dados):\n"
                "   * O perfil médio dos clientes desse grupo é de 49 anos, sendo majoritariamente aposentados, empreendedores ou empregados domésticos, com ensino médio completo.\n"
                "   * Do ponto de vista financeiro, esses clientes não apresentam inadimplência, possuem saldo médio de R$ 2.191,00, não possuem financiamento imobiliário nem empréstimo pessoal ativo.\n"
                "   * No que se refere à campanha e aos contatos realizados, são clientes abordados tanto por telefone fixo quanto por celular, com ligações que duram, em média, 247 segundos — aproximadamente quatro a cinco minutos. Além disso, observa-se que esses clientes foram contatados, em média, três vezes durante a campanha, sem nenhum histórico de contato anterior em campanhas passadas.\n"
                "\n**Reengajáveis**(Representação de 19\% do conjunto de dados):\n"
                "   * O perfil médio desse grupo é composto por indivíduos de 40 anos, geralmente empregados em funções operacionais (colarinho azul) ou atuando como empresários e gestores, casados e com ensino médio completo.\n"
                "   * Do ponto de vista financeiro, esses clientes não apresentam inadimplência, possuem saldo médio de R$ 1.556,88, têm financiamento imobiliário ativo e não possuem empréstimo pessoal.\n"
                "   * No que se refere à campanha e aos contatos realizados, são clientes contatados principalmente por celular, com ligações que duram, em média, 260 segundos — aproximadamente quatro a cinco minutos. Além disso, observa-se que esses clientes foram contatados, em média, duas vezes durante a campanha atual. Estão há mais de seis meses sem contato anterior e, historicamente, recebiam cerca de três contatos em campanhas anteriores. Na última campanha, contudo, não houve conversão, indicando ineficiência na ação anterior.", width='stretch', unsafe_allow_html=True)    

    st.subheader('Observações', width='stretch', divider='gray')
    st.markdown(""" Para acessar os detalhes de construção e os códigos desse estudo, acesse esse link: <a href="https://github.com/jefferson-datascience/PrevisaoAceitarContratoBanco/tree/main/NotebookAnaliseAgrupamentos" target="_blank">Github do Projeto </a> """, unsafe_allow_html=True)

elif pagina == "Resultados Modelo Preditivo":
        
        st.header('Modelo Preditivo para Prever Probabilidade da Assinatura do Contrato', divider='gray', width='stretch')
        st.image(r"https://raw.githubusercontent.com/jefferson-datascience/PrevisaoAceitarContratoBanco/blob/main//ScriptProdutoFinal/LogoMarketing4.png", width='stretch')

        st.text('Após entender como as variáveis impactam na assinatura do contrato e, também, quais são os perfis dos clientes que o banco tem, o time de marketing possui um boa quantidade de insumos e insights para apoiar as tomadas de decisões ' \
                'de negócio e elaboração de estratégias de campanhas e ações. Por para finalizar e complementar todos esses estudos, desenvolvemos um modelo de Machine Learning, no caso, um modelo de classificação de modo a prever a ' \
                'probabilidade de um cliente assinar um contrato de depósito bancário à prazo. \n ' \
                'A partir dessa probabilidade direcionaremos uma lista ordenada por essa probabilidade. Com um pouco mais de detalhes, utilizamos uma regressão logística ' \
                'que obteve as seguintes performances: ', width='stretch')
        st.markdown('* **AUC:** 88.8%.\n' \
                    '* **Precisão:** 80.7%.\n' \
                    '* **Recuperação:** 81.6%.\n', unsafe_allow_html=True, width='stretch')
        
        st.subheader('Projeções de Ganhos', divider='gray', width='stretch')
        st.text('Ao analisarmos a base original, observamos que a taxa de conversão atual para contratos de depósitos a prazo é de 13%. Isso significa que, a cada 100 prospecções realizadas, apenas 13 clientes efetivamente fecham um contrato. ' \
                'A partir desse cenário, estimamos o ganho potencial com o uso do modelo de classificação. \n ' \
                'No status quo, existem 13 clientes realmente interessados em cada grupo de 100 clientes. Considerando que o modelo possui 81% de recall, ' \
                'ele seria capaz de identificar aproximadamente 10 desses 13 clientes. Além disso, com uma precisão de 80%, significa que, para cada conjunto de visitas recomendadas pelo modelo, 80% correspondem a clientes realmente interessados. ' \
                'Portanto, para localizar esses mesmos 10 clientes identificados pelo modelo, precisamos resolver:', width='stretch')
        st.markdown('80% × x = 10 => x = 10 / 0.8 => x ≈ 13 visitas.', width='stretch', unsafe_allow_html=True)
        st.text( 'Ou seja, o modelo precisa de aproximadamente 13 visitas qualificadas para encontrar 10 clientes interessados. Se quisermos encontrar os mesmos 13 clientes que seriam encontrados no cenário atual, o cálculo fica:', width='stretch')
        st.markdown('80% × x = 13 => x = 13 / 0.8 => x ≈ 16 visitas', width='stretch')
        st.text('Isso representa uma redução significativa no esforço de prospecção: \n' \
                '100 visitas no cenário atual para encontrar 13 clientes vs. 16 visitas com o modelo para encontrar os mesmos 13 clientes. \n' \
                '\n O que corresponde a uma redução de aproximadamente 84% no volume de prospecções necessárias.\n ' \
                'Portanto, o principal ganho trazido pelo modelo é a eficiência operacional: conseguimos identificar praticamente o mesmo número de clientes ' \
                'interessados com um volume muito menor de visitas, direcionando o time comercial para leads com maior probabilidade de conversão e reduzindo substancialmente o esforço comercial necessário', width='stretch')
        
        st.subheader('Observações', width='stretch', divider='gray')
        st.markdown(""" Para acessar os detalhes de construção e os códigos da construção desse modelo, acesse esse link: <a href="https://github.com/jefferson-datascience/PrevisaoAceitarContratoBanco/tree/main/NotebookModeloPreditivo" target="_blank">Github do Projeto </a> """, unsafe_allow_html=True)

elif pagina=='Dashboard':

        # Carregamento dos Dados
        base = pd.read_parquet("https://raw.githubusercontent.com/jefferson-datascience/PrevisaoAceitarContratoBanco/blob/main/ScriptProdutoFinal/BaseAcoes.parquet", engine='fastparquet')

        # Construção dos Filtros
        faixas_probabilidades = base['ProbabilidadeAssinarContrato'].unique().tolist()
        selecao_emprestimo_pessoal = base['loan'].unique().tolist()
        selecao_financiamento_imobiliario = base['housing'].unique().tolist()
        selecao_inadimplencia = base['default'].unique().tolist()
        selecao_empregos = base['job'].unique().tolist()
        selecao_matrimonio = base['marital'].unique().tolist()
        selecao_educacao = base['education'].unique().tolist()
        idade_maxima = base['age'].max()
        idade_minima = base['age'].min()
        saldo_medio_maximo = base['balance'].max()
        saldo_medio_minimo = base['balance'].min()
        clusters = base['Grupos'].unique().tolist()
        
        # ========================= CABEÇALHO ====================================================================

        st.header(f'Analytics de Depósito Bancário à Prazo.', width='stretch')

        # ========================= CAMADA DE FILTROS SOCIOECONOMICOS =============================================
        
        # Cabeçalho
        st.subheader('Filtros Socioeconômicos', width='stretch', divider='grey')
        
        filtro_emprego = st.multiselect('Profissões', options=selecao_empregos, default=selecao_empregos, width='stretch')
        
        filtro_socio1, filtro_socio2, filtro_socio3 = st.columns(3, width='stretch')
        
        # Filtro de Idade e Emprego
        with filtro_socio1:
                filtro_idade = st.slider('Idade', min_value=idade_minima, max_value=idade_maxima, value=(idade_minima, idade_maxima), step=1, width='stretch') 
        with filtro_socio2:
                filtro_matrimonio = st.multiselect('Status Matrimonial', options=selecao_matrimonio, default=selecao_matrimonio, width='stretch')
        with filtro_socio3:
                filtro_educacao = st.multiselect('Nivel Educacional', options=selecao_educacao, default=selecao_educacao, width='stretch')


        # ============================= CAMADA DE FILTROS FINANCEIROS ==================================================================

        # Cabeçalho
        st.subheader('Filtros Financeiros', width='stretch', divider='grey')

        # Filtros de Empréstimo, Financiamento e Inadimplência
        filtros_financeiros1, filtros_financeiros2, filtros_financeiros3, filtros_financeiros4 = st.columns(4, width='stretch')
        with filtros_financeiros1:
            filtro_saldo_medio = st.slider('Saldo Medio', min_value=saldo_medio_minimo, max_value=saldo_medio_maximo, value=(saldo_medio_minimo, saldo_medio_maximo), step=1, width='stretch') 
        with filtros_financeiros2:
                filtro_emprestimo = st.pills('Empréstimo Pessoal?', options=selecao_emprestimo_pessoal, default=selecao_emprestimo_pessoal, selection_mode='multi', width='stretch')
        with filtros_financeiros3:
                filtro_financiamento = st.pills('Financiamento Imobiliário?', options=selecao_financiamento_imobiliario, default=selecao_financiamento_imobiliario, selection_mode='multi', width='stretch')
        with filtros_financeiros4:
                filtro_inadimplencia = st.pills('Inadimplente?', options=selecao_inadimplencia, default=selecao_inadimplencia, selection_mode='multi', width='stretch')
        
        # ========================== CAMADA DE FILTROS INTELIGENTES ========================================================================

        # Cabeçalho
        st.subheader('Filtros de Inteligência de Dados', width='stretch', divider='grey')

        filtro_inteligencia1, filtro_inteligencia2 = st.columns(2, width='stretch')
        
        with filtro_inteligencia1:
                filtro_probabilidades = st.multiselect('Probabilidades', options=faixas_probabilidades, default=faixas_probabilidades)
        with filtro_inteligencia2:
               filtro_clusters = st.multiselect('Grupos', options=clusters, default=clusters)

        
        dataframe = base[(base['ProbabilidadeAssinarContrato'].isin(filtro_probabilidades)) &
                         (base['job'].isin(filtro_emprego)) &
                         (base['marital'].isin(filtro_matrimonio)) &
                         (base['education'].isin(filtro_educacao)) &
                         (base['loan'].isin(filtro_emprestimo)) &
                         (base['housing'].isin(filtro_financiamento)) &
                         (base['default'].isin(filtro_inadimplencia)) &
                         ((filtro_idade[0] < base['age']) & (base['age'] < filtro_idade[1])) &
                         ((filtro_saldo_medio[0] < base['balance']) & (base['balance'] < filtro_saldo_medio[1])) & 
                         (base['Grupos'].isin(filtro_clusters))]
        total_analisados = dataframe.shape[0]

        # =========================== INFORMAÇÕES DAS PROBABILIDADES =======================================


        # Cards com as Probabilidades
        altissima  = round((dataframe[dataframe['ProbabilidadeAssinarContrato'] == 'Altíssima'].shape[0]/dataframe.shape[0])*100, 1)
        alta       = round((dataframe[dataframe['ProbabilidadeAssinarContrato'] == 'Alta'].shape[0]/dataframe.shape[0])*100, 1)
        moderada   = round((dataframe[dataframe['ProbabilidadeAssinarContrato'] == 'Moderada'].shape[0]/dataframe.shape[0])*100, 1)
        baixa      = round((dataframe[dataframe['ProbabilidadeAssinarContrato'] == 'Baixa'].shape[0]/dataframe.shape[0])*100, 1)
        baixissima = round((dataframe[dataframe['ProbabilidadeAssinarContrato'] == 'Baixíssima'].shape[0]/dataframe.shape[0])*100, 1)
        
        st.subheader(f'Prob. de Assinar Contrato de Depósito Bancário à Prazo.  Total Analisados: {total_analisados}', width='stretch', divider='grey')

        card1, card2, card3, card4, card5 = st.columns(5, width='stretch')

        with card1:
               
                st.metric(value=f"{altissima}%", label='Altíssimas', width='stretch', border=True)
        
        with card2:
                
                st.metric(value=f"{alta}%", label='Alta', width='stretch', border=True)
        
        with card3:

                st.metric(value=f"{moderada}%", label='Moderada', width='stretch', border=True)
        
        with card4:
               
                st.metric(value=f"{baixa}%", label='Baixa', width='stretch', border=True)
        
        with card5:
                
                st.metric(value=f"{baixissima}%", label='Baixíssima', width='stretch', border=True)

        # =========================== INFORMAÇÕES SOCIOECONÔMICAS =======================================

        st.subheader('Informações SocioEconômicas', width='stretch', divider='grey')

        # =============== Distribuição das idades ======================================================
        histograma_idade = dataframe.rename(columns={'age':'Idade'})
        distribuicao_idade = px.histogram(data_frame=histograma_idade, x='Idade', title='Distribuição de Idade')
        st.plotly_chart(distribuicao_idade, key='iris', width='stretch')

        # ========================= Empregos ==========================================================
        empregos = pd.DataFrame(dataframe['job'].value_counts()).reset_index().rename(columns={'job':'Profissão', 'count':'Quantidade'})
        empregos['Percentual'] = (empregos['Quantidade']/empregos['Quantidade'].sum())*100
        percentual_empregos = px.bar(data_frame=empregos, x='Profissão', y='Percentual', text=empregos['Percentual'].map(lambda x: f"{x:.1f}%"), title='Profissões')
        st.plotly_chart(percentual_empregos, width='stretch')

        info_socioeconomico1, info_socioeconomico2 = st.columns(2)

        with info_socioeconomico1:

                # ========================== Proporção do Estado Civil ========================================
                estado_civil = pd.DataFrame(dataframe['marital'].value_counts()).reset_index().rename(columns={'marital':'Estado Civil', 'count':'Quantidade'})
                estado_civil['Percentual'] =(estado_civil['Quantidade']/estado_civil['Quantidade'].sum())*100
                percentual_estado_civil = px.bar(data_frame=estado_civil, x='Estado Civil', y='Percentual', text=estado_civil['Percentual'].map(lambda x: f"{x:.1f}%"), title="Estado Matrimonial")
                st.plotly_chart(percentual_estado_civil, width='stretch')

        with info_socioeconomico2:

                # ========================== Proporção do nível educacional ==========================
                nivel_educacional = pd.DataFrame(dataframe['education'].value_counts().reset_index().rename(columns={'education':'Nível Educacional', 'count':'Quantidade'}))
                nivel_educacional['Percentual'] = (nivel_educacional['Quantidade']/nivel_educacional['Quantidade'].sum())*100
                percentual_nivel_educacional = px.pie(data_frame=nivel_educacional, names='Nível Educacional', values='Percentual', title='Nível Educacional')
                st.plotly_chart(percentual_nivel_educacional, width='stretch')


        # =========================== INFORMAÇÕES FINANCEIRAS =======================================

        # Relatório das informações Financeiras
        st.subheader('Informações Financeiras', width='stretch', divider='grey')

        # =================================== Histograma do Saldo Médio ==========================================
        histograma_saldo_medio = dataframe.rename(columns={'balance':'Saldo Médio em Conta'})
        distribuicao_saldo_medio = px.histogram(data_frame=histograma_saldo_medio, x='Saldo Médio em Conta', title='Distribuição de Saldo Médio em Conta')
        st.plotly_chart(distribuicao_saldo_medio, width='stretch')

        info_financeiras1, info_financeiras2, info_financeiras3 = st.columns(3)


        with info_financeiras1:
              
                # =================================== Proporção de Inadimplência ========================================
                inadimplencia = pd.DataFrame(dataframe['default'].value_counts()).reset_index().rename(columns={'default': 'Inadimplência', 'count':'Quantidade'})
                inadimplencia['Percentual'] = (inadimplencia['Quantidade']/inadimplencia['Quantidade'].sum())*100
                percentual_inadimplencia = px.pie(data_frame=inadimplencia, names='Inadimplência', values='Percentual', title='Inadimplência')
                st.plotly_chart(percentual_inadimplencia, width='stretch')

        with info_financeiras2:
               
                # ==================================== Proporção de Financiamento Imobiliário ===============================
                financiamento_imobiliario = pd.DataFrame(dataframe['housing'].value_counts()).reset_index().rename(columns={'housing':'Financiamento Imobiliário', 'count':'Quantidade'})
                financiamento_imobiliario['Percentual'] = (financiamento_imobiliario['Quantidade']/financiamento_imobiliario['Quantidade'].sum())*100
                percentual_financiamento_imobiliario = px.bar(data_frame=financiamento_imobiliario, x='Financiamento Imobiliário', y='Percentual', text=financiamento_imobiliario['Percentual'].map(lambda x: f"{x:.1f}%"),  title='Financiamento Imobiliário')
                st.plotly_chart(percentual_financiamento_imobiliario, width='stretch')

        with info_financeiras3:

                # ===================================== Proporções de Empréstimo Pessoal ====================================
                emprestimo_pessoal = pd.DataFrame(dataframe['loan'].value_counts()).reset_index().rename(columns={'loan':'Empréstimo Pessoal', 'count':'Quantidade'})
                emprestimo_pessoal['Percentual']  = (emprestimo_pessoal['Quantidade']/emprestimo_pessoal['Quantidade'].sum())*100
                percentual_emprestimo_pessoal = px.bar(data_frame=emprestimo_pessoal, x='Empréstimo Pessoal', y='Percentual', text=emprestimo_pessoal['Percentual'].map(lambda x: f"{x:.1f}%"), title='Empréstimo Pessoal')
                st.plotly_chart(percentual_emprestimo_pessoal, width='stretch')


        st.subheader('Tabela Analítica', width='stretch', divider='grey')
        st.dataframe(data=dataframe)