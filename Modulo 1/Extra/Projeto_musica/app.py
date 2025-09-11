import streamlit as st



#--------------------------------------------------------------Sidebar

st.sidebar.image('logo.png')
st.sidebar.title('AuraMusic')
st.sidebar.title('Músicas que mais escuta no mês')

musicas = ['Is it','Anna Júlia','Slow Down','Numb','O vagabundo e a Dama','Taste','Gnarly']

opcao = st.sidebar.selectbox('Escolha a música', musicas)

#-------------------------------------------------------------------Principal

st.title('AuraMusic')

st.image(f'{opcao}.png')
st.markdown(f'## Você escolheu a música: {opcao}')
st.markdown('---')

tempo = st.text_input('Quantos dias você escutou essa música?')
qtd = st.text_input('Quantas vezes você ouviu ela hoje?')

if opcao == 'Is it':
    mnt = 146.4

elif opcao == 'Anna Júlia':
    mnt = 199.2

elif opcao == 'Slow Down':
    mnt = 198

elif opcao == 'Numb':
    mnt = 222

elif opcao == 'O vagabundo e a Dama':
    mnt = 336

elif opcao == 'Taste':
    mnt = 202.2

elif opcao == 'Gnarly':
    mnt = 133.2                                        


if st.button('Aperte'):

    total_segundos = int(qtd) * int(mnt)
    horas = total_segundos / 60

    st.write(f'O total de tempo que você passou ouvindo a música {opcao} é de {horas:.2f} minutos.')