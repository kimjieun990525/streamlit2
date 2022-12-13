import streamlit as st


# 유저한테 데이터를 입력 받는 방법

def main() : 
    # 텍스트를 입력 받는 방법
    name = st.text_input('이름을 입력하세요!')
    st.title(name)

    name2 = st.text_input('이름 입력!', max_chars=5)
    st.title(name2)

    message = st.text_area('메시지를 입력하세요.')
    st.text(message)

    # 숫자 입력 받는 방법
    year = st.number_input('출생년도를 입력하세요', 1900, 2030)
    st.text(year)
    # 파라미터를 써주면 정수나 실수로 범위를 지정할 수 있음.. 디폴트는 실수..
    # 스텝 지정도 가능..
    numner = st.number_input('실수를 입력하세요', 0.5, 100.0, step=0.3)
    
    # 날짜 입력 받는 방법
    my_date = st.date_input('약속 날짜 입력')
    st.write(my_date)

    st.text( my_date.strftime('%Y년 %M월 %d일') )  # 이거 결과 이상하네.. 확인 필요...

    # 시간 입력 받는 방법
    my_time = st.time_input('약속 시간 선택')
    st.write(my_time)

    st.text( my_time.strftime('%H:%M') )

    # 비밀번호 입력 받는 방법
    password = st.text_input('비밀번호 입력', type='password')
    st.text(password)

    # 색깔 입력
    color = st.color_picker('색을 선택하세요.')  #색은 16진수로 표시함..
    st.text(color)



if __name__ == '__main__' :
    main()