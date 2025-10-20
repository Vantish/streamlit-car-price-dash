import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

def run_ml():
    st.subheader('구매 금액 예측하기')
    st.info('아래 정보를 입력하면 금액을 예측해드립니다.')
    gender_list = ['남자', '여자']
    gender = st.radio('성별을 입력하세요', gender_list)

    if gender == gender_list[0]:
        gender_data = 0
    else:
        gender_data = 1

    age = st.number_input('나이 입력', min_value = 20, max_value = 90)
    salary = st.number_input('연봉 입력 (달러)', min_value = 10000, step = 1000)
    debt = st.number_input('카드빛 입력 (달러)', min_value = 0, step = 1000)
    worth = st.number_input('자산 입력 (달러)', min_value = 10000, step = 1000)
    if st.button('예측하기!'):
        regressor = joblib.load('./model/regressor.pkl')
        new_data = [{'Gender' : gender_data, 'Age' : age, 
                     'Annual Salary' : salary, 'Credit Card Debt' : debt,
                     'Net Worth' : worth}]
        df = pd.DataFrame(new_data)
        y_pred = regressor.predict(df)
        if y_pred < 0:
            st.warning('예측이 어렵습니다.')
        else:
            price = format(round(y_pred[0]), ',')
            st.success(f'예측한 금액은 {price} 달러입니다.')
