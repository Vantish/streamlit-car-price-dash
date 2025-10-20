import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def run_eda():
    st.subheader('자동차 구매 데이터 탐색 (EDA)')

    # 안전하게 파일 읽기
    try:
        df = pd.read_csv('./data/Car_Purchasing_Data.csv')
    except FileNotFoundError:
        st.error('데이터 파일을 찾을 수 없습니다: ./data/Car_Purchasing_Data.csv')
        return

    st.write('데이터 샘플')
    col_a, col_b = st.columns([3, 2])
    with col_a:
        if st.checkbox('데이터프레임 보기'):
            st.dataframe(df.head(100))

            st.markdown('**최댓값/최솟값 확인**')
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            if numeric_cols:
                sel = st.selectbox('컬럼 선택', numeric_cols)
                st.write(f'- {sel} : min = {df[sel].min()}, max = {df[sel].max()}')
            else:
                st.write('숫자형 컬럼이 없습니다.')

    with col_b:
        st.markdown('데이터 요약')
        st.write(df.describe().T)

    st.write('---')

    # 통계 및 시각화
    st.markdown('### 통계 & 시각화')
    viz_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if not viz_cols:
        st.info('시각화 가능한 숫자형 컬럼이 없습니다.')
        return

    viz_option = st.selectbox('시각화 유형 선택', ['상관관계 히트맵', '페어 플롯', '그래프(bar)', '그래프(pie)'])

    if viz_option == '상관관계 히트맵':
        fig, ax = plt.subplots(figsize=(10, 6))
        corr = df[viz_cols].corr()
        sb.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
        st.pyplot(fig)

    elif viz_option == '페어 플롯':
        # pairplot은 시간이 걸릴 수 있으므로 샘플을 사용
        sample = df[viz_cols].sample(n=min(300, len(df)), random_state=42)
        try:
            g = sb.pairplot(sample)
            st.pyplot(g.fig)
        except Exception as e:
            st.error(f'페어플롯 생성 중 오류가 발생했습니다: {e}')

    elif viz_option == '그래프(bar)':
        sel_col = st.selectbox('막대그래프로 표시할 카테고리(또는 숫자)를 선택하세요', viz_cols)
        agg = df.groupby(sel_col).size().sort_values(ascending=False)
        fig, ax = plt.subplots()
        agg.head(20).plot(kind='bar', ax=ax)
        ax.set_ylabel('count')
        st.pyplot(fig)

    elif viz_option == '그래프(pie)':
        sel_col = st.selectbox('파이 차트에 사용할 컬럼을 선택하세요', viz_cols)
        counts = df[sel_col].value_counts().head(10)
        fig, ax = plt.subplots()
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
    



