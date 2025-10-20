import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def run_eda():
    df = pd.read_csv('./data/Car_Purchasing_Data.csv')
    st.subheader('자동차 구매 데이터프레임')
    checkbox1 = st.checkbox('데이터프레임')
    if checkbox1 == True:
        st.dataframe(df)
        st.text('\n')
        list2 = ['최댓값 최솟값 확인']
        select2 = st.selectbox('확인할 값', list2)
        if select2 == list2[0]:
            min_max_menu  = df.columns[4 : ]
            select_columns1 = st.selectbox('컬럼을 선택하세요', min_max_menu)
            st.text(f'{select_columns1} 컬럼의 최댓값은 {df[select_columns1].max()} 이며 최솟값은 {df[select_columns1].min()} 입니다.')
   

    st.text('\n')
    list1 = ['상관관계 히트맵', '페어 플롯', '그래프(bar)', '그래프(pie)']
    checkbox2 = st.checkbox('통계')
    if checkbox2 == True:
        checkbox3 = st.checkbox('상관관계 데이터프레임')
        if checkbox3 == True:
            multi_menu  = df.columns[4 : ]
            multiselect1 = st.multiselect('컬럼을 2개 이상 선택하세요.', multi_menu)
            if len(multiselect1) >= 2:
                st.dataframe(df[multiselect1].corr(numeric_only=True))
            
        select1 = st.selectbox('통계 선택', list1)
        if select1 == list1[0]:
            fig1 = plt.figure()
            sb.heatmap(data = df.corr(numeric_only=True), annot=True, 
            cmap='coolwarm', vmin = -1, vmax = 1, linewidths= 0.5)
            st.pyplot(fig1)
        elif select1 == list1[1]:
            fig2 = sb.pairplot(data = df, vars = ['Age', 'Annual Salary', 'Credit Card Debt', 'Car Purchase Amount']) 
            st.pyplot(fig2)
        elif select1 == list[2]:
            pass
        elif select1 == list[3]:
            pass
    



