from api.AI import AIAPI
import streamlit as st
from PIL import Image

@st.cache_resource
def get_api():
    return AIAPI(font="resources/malgun.ttf")

def main():
    api = get_api()

    st.title("책 읽어주는 인공지능")

    st.subheader("촬영된 텍스트 이미지를 업로드 해주세요.")

    query = st.file_uploader('이미지 선택', type=['png', 'jpg', 'jpeg'])

    if query is not None:
        st.image(query)

        # OCR 인식 결과
        st.subheader("OCR 결과")
        response = api.query_image2text(query)
        st.markdown(response)

        if response is not None:
            st.subheader("요약 결과")
            title, summary = api.query_text2text(response)
            st.markdown("**" + title + "**")
            st.markdown(summary)   

if __name__ == '__main__':
    main()