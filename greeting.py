import streamlit as st

st.title('Greeating Page')

marks = st.number_input('Enter your obtain makrs: ')
total = st.number_input('Enter total  makrs: ')

p = marks/total * 100

res = st.button('Calculate Result')

if res:
    st.subheader(f'your percentage is : :blue{p} %')
    if p > 80:
        st.success('Excelletn')
    elif p >= 60 and p < 80:
        st.info('Gooog job')
else:
    st.warning('Wait for result')
