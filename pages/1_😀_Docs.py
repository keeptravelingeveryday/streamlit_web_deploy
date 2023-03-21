import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

#페이지 기본 설정
st.set_page_config(
    page_icon='😎',
    page_title="tpwnd",
    layout="wide")

st.subheader("Document")

if st.button("app.py코드보기"):
    code = '''
    #페이지 기본 설정
    st.set_page_config(
    page_icon='😀',
    page_title="tpwnd",
    layout="wide")

    #페이지 헤더, 서브헤더 제목 설정
    st.header("데이터를 보여조🧐")
    st.subheader("Bird or Drone")

    '''
    st.code(code, language="python")

