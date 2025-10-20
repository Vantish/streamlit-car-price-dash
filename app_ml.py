import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os


def run_ml():
    st.subheader('구매 금액 예측하기')
    st.info('아래 정보를 입력하면 예측 모델로 자동차 구매 금액을 예측합니다.')

    # 입력 그룹
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox('성별', ['남자', '여자'])
        age = st.number_input('나이', min_value=18, max_value=100, value=30)
        salary = st.number_input('연봉 (달러)', min_value=0, step=1000, value=50000)

    with col2:
        debt = st.number_input('카드 빚 (달러)', min_value=0, step=500, value=1000)
        worth = st.number_input('자산 (달러)', min_value=0, step=1000, value=20000)
        st.write('')

    gender_data = 0 if gender == '남자' else 1

    if st.button('예측하기'):
        model_path = os.path.join('model', 'regressor.pkl')
        if not os.path.exists(model_path):
            st.error(f'모델 파일을 찾을 수 없습니다: {model_path}')
            st.info('먼저 모델을 학습해 `model/regressor.pkl`으로 저장해야 합니다.')
            return

        try:
            regressor = joblib.load(model_path)
        except Exception as e:
            st.error(f'모델 로드 중 오류가 발생했습니다: {e}')
            return

        new_data = pd.DataFrame([{
            'Gender': gender_data,
            'Age': age,
            'Annual Salary': salary,
            'Credit Card Debt': debt,
            'Net Worth': worth
        }])

        try:
            y_pred = regressor.predict(new_data)
        except Exception as e:
            st.error(f'예측 중 오류가 발생했습니다: {e}')
            return

        pred = float(y_pred[0])
        if pred <= 0:
            st.warning('예측 결과가 유효하지 않습니다 (음수 또는 0). 입력값을 확인하세요.')
        else:
            price = f"{pred:,.0f}"
            st.success(f'예측한 금액은 {price} 달러입니다.')

        # 디버그용 원본 값 보기(토글)
        if st.checkbox('입력 요약 보기'):
            st.json(new_data.to_dict(orient='records')[0])
