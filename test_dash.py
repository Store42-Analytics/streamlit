import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Дашборд
st.title("📊 Дашборд")

# Генерация случайных данных
days = np.arange(1, 11)
values = np.random.randint(10, 100, size=10)
df = pd.DataFrame({"Дни": days, "Значения": values})

# Разделение на колонки
col1, col2 = st.columns(2)

# Отображение графика в первой колонке
with col1:
    st.subheader("📉 График")
    fig = px.line(df, x="Дни", y="Значения", markers=True, title="Интерактивный график в Streamlit")
    fig.update_layout(xaxis_title="Дни", yaxis_title="Значение", template="plotly_white")
    st.plotly_chart(fig)

# Отображение таблицы во второй колонке
with col2:
    st.subheader("📊 Данные")
    st.dataframe(df)
