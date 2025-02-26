import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Заголовок приложения
st.title("Здесь будет дашборд по метрикам теста")

# Генерация случайных данных
days = np.arange(1, 11)
values = np.random.randint(10, 100, size=10)

df = pd.DataFrame({"Дни": days, "Значения": values})

# Построение графика
fig, ax = plt.subplots()
ax.plot(df["Дни"], df["Значения"], marker="o", linestyle="-", color="b")
ax.set_xlabel("Дни")
ax.set_ylabel("Значение")
ax.set_title("Простой график в Streamlit")
ax.grid()

# Отображение графика
st.pyplot(fig)

# Отображение таблицы с данными
st.dataframe(df)