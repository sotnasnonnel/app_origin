import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# Carregar os dados de exemplo
@st.cache_data
def load_data():
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [5, 10, 15, 20, 25],
        'D': [2, 4, 6, 8, 10]
    })
    return data

# Gerar dados fictícios para vendas
@st.cache_data
def generate_sales_data():
    dates = pd.date_range(start="2023-01-01", periods=100)
    data = {
        'date': dates,
        'close': pd.Series(range(100)) + 100,
        'volume': pd.Series(range(100)) * 10
    }
    sales_df = pd.DataFrame(data)
    return sales_df

# Gerar dados fictícios para população
@st.cache_data
def generate_population_data():
    countries = ['Country A', 'Country B', 'Country C']
    years = pd.Series(range(2000, 2024))
    population_data = []
    for country in countries:
        for year in years:
            population_data.append({'Country Name': country, 'Year': year, 'Population': (year - 1999) * 100000})
    population_df = pd.DataFrame(population_data)
    return population_df

# Paleta de Cores Fosca
colors = {
    'Azul Escuro Fosco': '#243447',
    'Laranja Fosco': '#D2691E',
    'Amarelo Fosco': '#E4B600',
    'Verde Fosco': '#A3B19C'
}

# Configurar o menu de navegação
with st.sidebar:
    selected = option_menu(
        "Menu",
        ["Exemplo de Dados", "Análise de Vendas", "Análise de População"],
        icons=["bar-chart-line", "bar-chart-line", "people"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": colors['Azul Escuro Fosco']},
            "icon": {"color": colors['Amarelo Fosco'], "font-size": "25px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "color": colors['Verde Fosco'],
                "width": "100%"
            },
            "nav-link-selected": {"background-color": '#333333'},
        }
    )

# Página Exemplo de Dados
if selected == "Exemplo de Dados":
    st.title('Exemplo de Dados')

    # Descrição da página
    st.write("""
    ### Descrição
    Esta página exibe um conjunto de dados de exemplo que contém quatro colunas: A, B, C e D. 
    Aqui você pode visualizar os dados e realizar análises simples como gráficos de dispersão, histogramas e gráficos de linha.
    """)

    # Exibir os dados
    st.subheader('Visualização dos Dados')
    data = load_data()
    st.write(data)

    # Análise de Dados
    st.subheader('Análise de Dados')
    analysis_type = st.selectbox('Selecione o tipo de análise', ['Gráfico de Dispersão', 'Histograma', 'Gráfico de Linha'])

    if analysis_type == 'Gráfico de Dispersão':
        x_axis = st.selectbox('Selecione o eixo X', data.columns)
        y_axis = st.selectbox('Selecione o eixo Y', data.columns)
        fig = px.scatter(data, x=x_axis, y=y_axis, color_discrete_sequence=list(colors.values()))
        st.plotly_chart(fig)

    elif analysis_type == 'Histograma':
        column = st.selectbox('Selecione a coluna para o histograma', data.columns)
        fig = px.histogram(data, x=column, color_discrete_sequence=list(colors.values()))
        st.plotly_chart(fig)

    elif analysis_type == 'Gráfico de Linha':
        x_axis = st.selectbox('Selecione o eixo X', data.columns)
        y_axis = st.selectbox('Selecione o eixo Y', data.columns)
        fig = px.line(data, x=x_axis, y=y_axis, color_discrete_sequence=list(colors.values()))
        st.plotly_chart(fig)

# Página de Análise de Vendas
elif selected == "Análise de Vendas":
    st.title('Análise de Vendas')

    # Descrição da página
    st.write("""
    ### Descrição
    Esta página apresenta uma análise fictícia de dados de vendas. Os dados incluem datas, preços de fechamento e volumes de transações.
    Você pode visualizar os dados e realizar análises utilizando gráficos de barras e gráficos de linha.
    """)

    sales_df = generate_sales_data()

    st.subheader('Visualização dos Dados de Vendas')
    st.write(sales_df, height=400)

    st.subheader('Análise de Vendas')
    sales_type = st.selectbox('Selecione o tipo de análise', ['Gráfico de Barras', 'Gráfico de Linha'])

    if sales_type == 'Gráfico de Barras':
        x_axis = st.selectbox('Selecione o eixo X', sales_df.columns)
        y_axis = st.selectbox('Selecione o eixo Y', sales_df.columns)
        fig = px.bar(sales_df, x=x_axis, y=y_axis, color_discrete_sequence=list(colors.values()))
        st.plotly_chart(fig)

    elif sales_type == 'Gráfico de Linha':
        x_axis = st.selectbox('Selecione o eixo X', sales_df.columns)
        y_axis = st.selectbox('Selecione o eixo Y', sales_df.columns)
        fig = px.line(sales_df, x=x_axis, y=y_axis, color_discrete_sequence=list(colors.values()))
        st.plotly_chart(fig)

# Página de Análise de População
elif selected == "Análise de População":
    st.title('Análise de População')

    # Descrição da página
    st.write("""
    ### Descrição
    Esta página apresenta uma análise fictícia de dados de população. Os dados incluem países, anos e valores de população.
    Você pode visualizar os dados e realizar análises utilizando gráficos de linha e gráficos de área.
    """)

    population_df = generate_population_data()

    st.subheader('Visualização dos Dados de População')
    st.write(population_df, height=400)

    st.subheader('Análise de População')
    population_type = st.selectbox('Selecione o tipo de análise', ['Gráfico de Linha', 'Gráfico de Área'])

    if population_type == 'Gráfico de Linha':
        fig = px.line(population_df, x='Year', y='Population', color='Country Name', labels={'Country Name': 'Country', 'Year': 'Year', 'Population': 'Population'}, color_discrete_sequence=list(colors.values()))
        st.plotly_chart(fig)

    elif population_type == 'Gráfico de Área':
        fig = px.area(population_df, x='Year', y='Population', color='Country Name', labels={'Country Name': 'Country', 'Year': 'Year', 'Population': 'Population'}, color_discrete_sequence=list(colors.values()))
        st.plotly_chart(fig)

# Customização de Estilos
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {colors['Azul Escuro Fosco']};
        color: white;
    }}
    .stMarkdown {{
        color: white;
    }}
    .css-1aumxhk {{
        max-height: 400px;
    }}
    .css-18e3th9 {{
        padding: 0 !important;
    }}
    .css-12oz5g7 {{
        background-color: {colors['Azul Escuro Fosco']} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
