import streamlit as st
import pandas as pd


# UI 요소들을 처리하는 방법
# 버튼, 라디오버튼, 셀렉트박스, 멀티셀렉트, 슬라이더

def main() :
    df = pd.read_csv('streamlit_data/iris.csv')

    # 버튼을 클릭하면, 데이터프레임이 보이도록 만들기.

    if st.button('데이터프레임 보기') :
        st.dataframe(df)


    name = 'Mike'

    if st.button('대문자로') :
        st.text( name.upper() )

    if st.button('소문자로') :
        st.text( name.lower() )


    # 여러 개 중 하나를 고를 수 있는 버튼...
    status = st.radio('정렬을 선택하세요', ['오름차순정렬', '내림차순정렬'])

    if status == '오름차순정렬' :
        st.dataframe( df.sort_values('petal_length') )
        # df의 petal_length 컬럼을 오름차순으로 정렬해서 보여주세요.
    
    elif status == '내림차순정렬' :
        st.dataframe( df.sort_values('petal_length', ascending=False ) )
        # df의 petal_length 컬럼을 내림차순으로 정렬해서 보여주세요.
    

    
    # 체크박스를 체크하면, 데이터프레임이 나오고,
    # 해제하면 데이터프레임 나오지 않게

    if st.checkbox('show / hide') :
        st.dataframe( df )
    else : 
        st.write('')
    
    # 셀렉트박스 : 여러개 중에 한 개 선택
    language = ['Python', 'C', 'JAVA', 'PHP', 'GO']

    my_choice = st.selectbox('좋아하는 언어를 선택하세요', language )
    # 유저가 선택하면, 해당 언어를 다음처럼 표시해준다.
    # 저는 Python 언어를 가장 좋아합니다.
    # 저는 JAVA 언어를 가장 좋아합니다.

    st.write('저는 {} 언어를 가장 좋아합니다.'.format(my_choice))
    st.text('저는 {} 언어를 가장 좋아합니다.'.format(my_choice))
    # write든 tex든 편한 거 사용하기


    # 만약 유저가 선택한 언어가, '파이썬'이나 'PHP'나 'Go' 언어이면 '배우기 쉽습니다.' 출력,
    # 자바나 'C' 언어를 선택하면 '배우기 어렵습니다.' 라고 화면에 출력하세요.

    if my_choice == 'Python' or my_choice == 'GO' or my_choice == 'PHP':
        st.write('배우기 쉽습니다.')
    elif my_choice == 'C' or my_choice == "JAVA" :
        st.write('배우기 어렵습니다.')


    # 여러개를 선택할 수 있게 하는 multiselect
    # 아이리스 데이터프레임의 컬럼이름을 가져오세요.

    selected_list = st.multiselect('원하는 컬럼을 선택하세요', df.columns)
    print(selected_list)

    # 유저가 컬럼을 선택하면, 해당 컬럼을 화면에 보여주고,
    # 유저가 아무컬럼도 선택하지 않으면, 데이터프레임 보여주지 않는다.

    st.dataframe(df[selected_list])



    # 슬라이더
    age = st.slider('나이', 1, 100)

    st.text('당신이 선택한 나이는' + str(age) + '입니다.')


    st.slider('데이터', 1, 100, step= 5)

    st.slider('데이터', 1, 200, value=75)  # 기본값을 75로 세팅한 것이다..

    st.slider('데이터', 0.0, 1.0, step=0.1)


    with st.expander('hello') :   # 외우지 말고.. 그냥 통째로 가져다 써라..
        st.text('안녕하세요~')
        st.text('즐거운 공부 시간입니다.')





if __name__ == '__main__' :
    main()



