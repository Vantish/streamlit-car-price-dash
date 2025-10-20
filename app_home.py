import streamlit as st


def run_home():
    st.subheader('자동차 데이터를 분석하고 예측하는 앱')
    st.info('데이터는 Kaggle의 Car Purchasing Dataset (Car_Purchasing_Data.csv)을 사용했습니다.')

    col1, col2 = st.columns([2, 3])
    with col1:
        st.markdown(
            """
            ### 이 앱에서 할 수 있는 일
            - 데이터 탐색(EDA)
            - 변수 간 상관관계 시각화
            - 간단한 회귀 기반 구매금액 예측
            """
        )
        st.write('간단한 설명과 사용법을 좌측에서 확인하세요.')

    with col2:
        st.image('./image/car1.png', use_column_width=True, caption='예시 자동차 이미지')

    st.write('---')

