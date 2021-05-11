import streamlit as st


st.title('King County House Prices')

faixa_de_preco = st.slider("Faixa de preço",1,10, (1,10))
st.write(faixa_de_preco)

st.markdown('Nas características selecionadas, o valor do apartamento pode ser de <h1 style="color:red">'+str(1000*faixa_de_preco[0])+"</h1> até "+str(1000*faixa_de_preco[1]), unsafe_allow_html=True)

#st.sidebar.selectbox('Apartamentos com vista para o mar')