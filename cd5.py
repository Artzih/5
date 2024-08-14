import streamlit as st
valores = {
    101: 8.50,
    102: 4.50,
    104: 5.50,
    105: 6.60,
    106: 6.00
}
st.title('Calculadora de Pedido da Lanchonete')
codigo = st.number_input('Código do Item', min_value=101, max_value=106, step=1)
quantidade = st.number_input('Quantidade', min_value=1, step=1)
if st.button('Calcular Valor'):
    if codigo in valores:
        valor_item = valores[codigo]
        valor_total = valor_item * quantidade
        st.write(f'Valor Total: R$ {valor_total:.2f}')
    else:
        st.error('Código do lanche é inválido.')
st.subheader('Cardápio')
st.write('1. Cachorro Quente - Código 101 - R$ 8,50')
st.write('2. Bauru Simples - Código 102 - R$ 4,50')
st.write('3. Hambúrguer - Código 104 - R$ 5,50')
st.write('4. Cheeseburger - Código 105 - R$ 6,60')
st.write('5. Refrigerante - Código 106 - R$ 6,00')
