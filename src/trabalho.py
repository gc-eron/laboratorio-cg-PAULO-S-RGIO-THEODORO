import cv2
import numpy as np
import streamlit as st
from PIL import Image
st.title("Trabalho: Temas")
st.header("Academico: Paulo Sergio Theodoro")
foto = Image.open("imagens/concorde.jpg")
img = np.array(foto)

# 1. Matiz girada
st.header("1. Matiz girada")
col1, col2 = st.columns(2)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
giro = col1.slider("Giro (graus)", 0, 360, 120)

h = hsv[:, :, 0].astype(int)
h = h + giro // 2
h = h % 180

hsv_girada = hsv.copy()
hsv_girada[:, :, 0] = h.astype(np.uint8)

girada = cv2.cvtColor(hsv_girada, cv2.COLOR_HSV2RGB)
col1.image(girada, caption="H")

#2. Saturação

st.header("2. Saturação (S)")
col1, col2 = st.columns(2)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

fator_s = col1.slider("Saturação", 0.0, 2.0, 1.0)

# canais S 
s = hsv[:, :, 1].astype(float)
s = s * fator_s
s = np.clip(s, 0, 255)

hsv2 = hsv.copy()
hsv2[:, :, 1] = s
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB))


#Brilho

st.header("3. Brilho (V)")
col1, col2 = st.columns(2)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

fator_v = col1.slider("Brilho", 0.0, 2.0, 1.0)
# canais S e V

v = hsv[:, :, 2].astype(float)


v = v * fator_v

# limita os valores
v = np.clip(v, 0, 255)

# coloca os dois na mesma imagem
hsv2 = hsv.copy()

hsv2[:, :, 2] = v
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB))

#Negativo
st.header("4. Negativo")
st.write("Negativo da foto")

foto = Image.open("imagens/concorde.jpg").convert("RGB")
img = np.array(foto)

negativo = 255 - img

col1, col2 = st.columns(2)
col1.image(img, caption="Original", width=300)
col2.image(negativo, caption="Negativo", width=300)

#Espelhamento
st.header("5. Espelhamento")
col1, col2 = st.columns(2)

foto = Image.open("imagens/concorde.jpg").convert("RGB")
img = np.array(foto)

# Espelhamento horizontal
esp_h = img[:, ::-1]

# Espelhamento vertical
esp_v = img[::-1, :]

col1.image(esp_h, caption="Espelhada na horizontal")
col2.image(esp_v, caption="Espelhada na vertical")