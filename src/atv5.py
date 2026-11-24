import cv2
import numpy as np
import streamlit as st
from PIL import Image
st.title("Atv 5: HSV e recorte")
foto = Image.open("imagens/concorde.jpg")
img = np.array(foto)
# 1. HSV

st.header("1. HSV")
col1, col2 = st.columns(2)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

so_h = hsv.copy()
so_h[:, :, 1] = 255
so_h[:, :, 2] = 255
col1.image(img, caption="img")

rgb = cv2.cvtColor(so_h, cv2.COLOR_HSV2RGB)
col2.image(rgb, caption="H")

######## 2. Mudando o HSV
st.header("2. Mudando o HSV")
col1, col2 = st.columns(2)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

fator_s = col1.slider("Saturação", 0.0, 2.0, 1.0)
fator_v = col1.slider("Brilho", 0.0, 2.0, 1.0)
# canais S e V
s = hsv[:, :, 1].astype(float)
v = hsv[:, :, 2].astype(float)

s = s * fator_s
v = v * fator_v

# limita os valores
s = np.clip(s, 0, 255)
v = np.clip(v, 0, 255)

# coloca os dois na mesma imagem
hsv2 = hsv.copy()
hsv2[:, :, 1] = s.astype(np.uint8)
hsv2[:, :, 2] = v.astype(np.uint8)

# volta para RGB
nova = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)



# Col2

giro = col2.slider("Giro (graus)", 0, 360, 120)

h = hsv[:, :, 0].astype(int)
h = h + giro // 2
h = h % 180

hsv_girada = hsv.copy()
hsv_girada[:, :, 0] = h.astype(np.uint8)

girada = cv2.cvtColor(hsv_girada, cv2.COLOR_HSV2RGB)

# Criar duas colunas para exibir as imagens alinhadas
imagem1, imagem2 = st.columns(2)
#exibi as duas imagens nas colunas na mesma linha
imagem1.image(nova, caption="Saturação e brilho")
imagem2.image(girada, caption="Matiz girada")


# 3. Faixa na escala
st.header("3. Faixa na escala")
col1, col2 = st.columns(2)
escala = np.zeros((1, 12, 3), dtype=np.uint8)
escala[0, :, 0] = np.arange(0, 180, 15)
escala[0, :, 1] = 255
escala[0, :, 2] = 255
rgb = cv2.cvtColor(escala, cv2.COLOR_HSV2RGB)
col1.image(rgb.repeat(40, axis=0).repeat(40, axis=1), caption="escala")
h_min, h_max = col1.slider("Faixa de H na escala", 0, 179, (90, 130))
mascara = cv2.inRange(escala, (h_min, 0, 0), (h_max, 255, 255))






