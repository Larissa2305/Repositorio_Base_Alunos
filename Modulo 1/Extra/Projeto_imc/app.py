import streamlit as st



#--------------------------------------------------------------Sidebar
st.sidebar.image('logo.png')
st.sidebar.title('Clínica Cristal')
st.sidebar.title('Seu IMC')

#--------------------------------------------------------------Principal

st.title('Clínica Cristal - Seu IMC')

st.image('logo.png')

st.markdown('---')

altura = st.text_input('Qual é a sua altura?')
peso = st.text_input('qual é o seu peso?')    
    
if st.button('Calcular'):
    altura = float(altura)
    peso = float(peso)
    imc = peso / (altura ** 2)     
    

    if imc < 18.5:
        st.warning(f'O resultado do seu IMC é: {imc:.2f}. Portanto você está abaixo do peso, recomendo que comce a comer mais!')

    elif imc <= 24.9:
        st.warning(f'O resultado do seu IMC é: {imc:.2f}. Portanto seu peso é normal, então está tudo certinho!')

    elif imc <= 29.9:
        st.warning(f'O resultado do seu IMC é: {imc:.2f}. Portanto você está sobrepeso, recomendo que pare de comer um pouquinho!')

    elif imc <= 34.9:
        st.warning(f'O resultado do seu IMC é: {imc:.2f}. Portanto você está na obesidade grau I. Tá passando do pontooo, vai correr!')

    elif imc <= 39.9:
        st.warning(f'O resultado do seu IMC é: {imc:.2f}. Portanto você está na obesidade grau II. Tenta se levantar pelo menos.')

    else:
        st.warning(f'O resultado do seu IMC é: {imc:.2f}. Portanto você está na obesidade grau III. Comece a andar um pouco!')             


