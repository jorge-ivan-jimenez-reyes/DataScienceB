import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def main():
    # Título y breve descripción
    st.title("Análisis de Beneficios de la Energía Solar en Hogares")
    st.markdown("""
    **Este informe** presenta datos sobre costos, ahorros y otros beneficios 
    que se obtienen al instalar paneles solares en una casa normal.  
    Los datos provienen del *Estudio Hogar Solar 2025* realizado por la 
    Agencia Renovable del País (ARP) y la Universidad de Ingeniería Energética (UIE).
    ---
    """)

    # -------------------------------------------------------------------------
    # DATOS PRINCIPALES DEL ESTUDIO: COSTOS ANUALES (ANTES Y DESPUÉS)
    # -------------------------------------------------------------------------
    meses = [f'Mes {i}' for i in range(1, 13)]
    gasto_sin_solar = [120, 125, 110, 130, 140, 150, 160, 155, 145, 135, 125, 120]
    gasto_con_solar = [90, 85, 80, 95, 100, 105, 110, 110, 105, 100, 90, 85]

    df_costos = pd.DataFrame({
        'Mes': meses,
        'Gasto_sin_solar': gasto_sin_solar,
        'Gasto_con_solar': gasto_con_solar
    })

    # Calculamos ahorro mensual en porcentaje
    df_costos['Ahorro_%'] = ((df_costos['Gasto_sin_solar'] - df_costos['Gasto_con_solar'])
                            / df_costos['Gasto_sin_solar'] * 100)

    st.subheader("1. Comparación de Costos Mensuales")
    st.write("A continuación, se presenta el gasto en electricidad con y sin paneles solares a lo largo de un año:")

    # GRÁFICO DE LÍNEAS PARA COMPARAR EL GASTO MENSUAL
    fig_line_costos = go.Figure()
    fig_line_costos.add_trace(go.Scatter(
        x=df_costos['Mes'],
        y=df_costos['Gasto_sin_solar'],
        mode='lines+markers',
        name='Gasto sin paneles',
        line=dict(color='firebrick', width=3),
        marker=dict(size=7)
    ))
    fig_line_costos.add_trace(go.Scatter(
        x=df_costos['Mes'],
        y=df_costos['Gasto_con_solar'],
        mode='lines+markers',
        name='Gasto con paneles',
        line=dict(color='royalblue', width=3),
        marker=dict(size=7)
    ))
    fig_line_costos.update_layout(
        title='Comparación de Gasto Mensual en Electricidad (Antes vs. Después)',
        xaxis_title='Meses del año',
        yaxis_title='Gasto en Electricidad (Moneda local)',
        template='plotly_white'
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_line_costos, use_container_width=True)

    # GRÁFICO DE BARRAS PARA MOSTRAR AHORRO MENSUAL
    st.subheader("2. Porcentaje de Ahorro Mensual")
    st.write("El siguiente gráfico de barras ilustra el porcentaje de ahorro en cada mes:")

    fig_bar_ahorro = px.bar(
        df_costos,
        x='Mes',
        y='Ahorro_%',
        title='Porcentaje de Ahorro Mensual gracias a los Paneles Solares',
        labels={'Ahorro_%': 'Ahorro (%)'},
        color='Ahorro_%',
        color_continuous_scale='Tealgrn'
    )
    fig_bar_ahorro.update_layout(
        template='plotly_white',
        coloraxis_showscale=False
    )

    st.plotly_chart(fig_bar_ahorro, use_container_width=True)

    st.markdown("---")
    st.subheader("Conclusiones sobre Costos")
    st.markdown("""
    - Se observa una diferencia notable en el gasto mensual: 
      el **gasto con paneles** es consistentemente menor que el gasto sin paneles.
    - En promedio, el **ahorro mensual** ronda entre el 20% y 35%, 
      dependiendo del consumo y la temporada.
    """)

    # -------------------------------------------------------------------------
    # DATOS SECUNDARIOS DEL ESTUDIO: BENEFICIOS ADICIONALES
    # -------------------------------------------------------------------------
    st.subheader("3. Beneficios Adicionales")

    datos_beneficios = {
        'Beneficio': [
            'Aumento valor de la vivienda',
            'Disminución huella de carbono',
            'Independencia energética',
            'Estabilidad de costos futuros',
            'Incentivos gubernamentales',
            'Responsabilidad ambiental'
        ],
        # Impacto estimado en un índice de 0 a 100
        'Impacto(%)': [5, 35, 10, 15, 20, 15]
    }
    df_beneficios = pd.DataFrame(datos_beneficios)

    # GRÁFICO CIRCULAR
    st.write("**Distribución de Beneficios Adicionales**")
    fig_pie_beneficios = px.pie(
        df_beneficios,
        names='Beneficio',
        values='Impacto(%)',
        title='Distribución de Beneficios Adicionales (Estudio Hogar Solar 2025)',
        color_discrete_sequence=px.colors.qualitative.Alphabet
    )
    fig_pie_beneficios.update_traces(
        textposition='inside',
        textinfo='percent+label'
    )
    fig_pie_beneficios.update_layout(template='presentation')
    st.plotly_chart(fig_pie_beneficios, use_container_width=True)

    # GRÁFICO DE BARRAS
    st.write("**Impacto Comparativo de los Beneficios**")
    fig_bar_beneficios = px.bar(
        df_beneficios,
        x='Beneficio',
        y='Impacto(%)',
        color='Beneficio',
        title='Impacto Comparativo de los Beneficios de la Energía Solar',
        labels={'Impacto(%)':'Impacto (%)'},
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    fig_bar_beneficios.update_layout(
        template='plotly_white',
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig_bar_beneficios, use_container_width=True)

    st.markdown("---")
    st.markdown("""
    **Conclusión general:**  
    La instalación de paneles solares no solo reduce el **costo de electricidad** 
    sino que también conlleva beneficios a mediano y largo plazo, como el 
    **aumento del valor de la vivienda**, la **disminución de la huella de carbono**, 
    y la **independencia energética**.
    """)

if __name__ == "__main__":
    main()
