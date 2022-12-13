# 웹 대시보드에 이미지파일, 동영상파일 넣는 방법

import streamlit as st

# 이미지 처리를 위한 라이브러리
from PIL import Image

def main() :
    img = Image.open('streamlit_data/image_03.jpg')
    print(img)

    st.image(img)

    st.image(img, use_column_width=True)

    image_url = 'https://post-phinf.pstatic.net/MjAyMjExMzBfMjMw/MDAxNjY5ODE5OTQ1NDA4.3TXWdGeibf-hRdFVdK5A7NTAO0RS4Xmzf5FflwOpx6Yg.b2Hfyz6H1Y5AD4ZyN47XzNOUAm9EqgVwbketDhoJvDog.JPEG/_UM_0127_r.jpg?type=w1200'
    st.image(image_url)


    # 동영상 처리

    video_file = open('streamlit_data/secret_of_success.mp4', 'rb')

    st.video( video_file, format='video/mp4' )





if __name__ == '__main__' :
    main()






