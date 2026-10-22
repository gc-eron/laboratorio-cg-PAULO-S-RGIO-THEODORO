import numpy as np
import streamlit as st
def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)
    
st.title("Imagem como matriz *******Bandeira da Itália *******")

# cria a imagem com 12 linhas, 18 colunas e 3 canais RGB
bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[:, :6] = (0, 146, 70)# faixa verde à esquerda
bandeira[:, 6:12] = (255, 255, 255) # faixa branca no meio
bandeira[:, 12:18] = (206, 43, 55)# faixa vermelha à direita
st.image(ampliar(bandeira)) # exibe a bandeira ampliada




