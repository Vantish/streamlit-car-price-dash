import streamlit as st

from app_home import run_home
from app_eda import run_eda
from app_ml import run_ml


def main():
    st.set_page_config(page_title='자동차 구매 금액 예측', page_icon='🚗', layout='wide')

    # Sidebar
    st.sidebar.image('./image/car1.png', use_column_width=True)
    st.sidebar.markdown('''
    ## 네비게이션
    - Home: 앱 소개
    - EDA: 데이터 탐색 및 시각화
    - ML: 예측 인터페이스
    ''')

    menu = ['Home', 'EDA', 'ML']
    menulist = st.sidebar.selectbox('메뉴 선택', menu)

    # Main header
    st.markdown("""
    <div style='display:flex;align-items:center;gap:16px'>
      <h1 style='margin:0'>🚗 자동차 구매 금액 예측</h1>
      <div style='color:gray;margin-left:8px'>- 데이터 기반 예측 & 시각화 대시보드</div>
    </div>
    """, unsafe_allow_html=True)

    if menulist == 'Home':
        run_home()
    elif menulist == 'EDA':
        run_eda()
    elif menulist == 'ML':
        run_ml()


if __name__ == '__main__':
    main()