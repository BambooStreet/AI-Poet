
# from dotenv import load_dotenv
# load_dotenv()

from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import time
from PIL import Image
img = Image.open("img\\3.jpg")
img = img.transpose(Image.ROTATE_270)
img = img.resize((150,200))

#from langchain_openai import ChatOpenAI
#llm = ChatOpenAI(model="gpt-3.5-turbo")

output_parser = StrOutputParser()
llm = ChatOpenAI(model_name="gpt-3.5-turbo")
chain = llm | output_parser




st.title('시를 써보자 :sunglasses:')

#content = '코드'
#result = chain.invoke(f"{content}에 대한 시를 써줘")
#print(result)
#print(type(result))

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')
with col2:
    st.image(img, caption='새터마을 방랑시인의 모습')
with col3:
    st.write(' ')

content = st.text_input('시의 주제를 제시해주세요.')

st.write(f'시의 주제는 {content}입니다.')

if st.button('시 작성 요청하기'):
    with st.spinner('Wait for it...'):
        time.sleep(5)
        result = chain.invoke(f"{content}에 대한 시를 써줘")
        st.write(result)

