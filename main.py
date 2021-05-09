import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

st.write("プログレスバーの表示")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)

"""
# DONE!!!
"""

left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander = st.beta_expander("問い合わせ")
expander.write("問い合わせ内容を書く")
expander.write("問い合わせ内容を書く")
expander.write("問い合わせ内容を書く")
expander.write("問い合わせ内容を書く")
expander.write("問い合わせ内容を書く")

# if st.checkbox("Show うさちゃんImage"):
#     img = Image.open("PXL_20210507_071648227.PORTRAIT.jpg")
#     st.image(img, caption="USAGI", use_column_width=True)



