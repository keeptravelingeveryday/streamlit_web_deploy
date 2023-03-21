import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

#ㅔ이지 기본 설정
st.set_page_config(
    page_icon='😀',
    page_title="tpwnd",
    layout="wide")

#페이지 헤더, 서브헤더 제목 설정
st.header("데이터를 보여조🧐")
st.subheader("Bird or Drone")

#페이지 컬럼 분할
cols = st.colums((1,2))



 