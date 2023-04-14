import cv2

P = cv2.imread('Lenna.tif')

num_linhas, num_colunas, num_canais = P.shape

R = 0 * P
R = R.astype('uint8')
R[:, :num_colunas, :] = P

P_espelhada = cv2.flip(P, 1)

R[:, num_colunas:, :] = P_espelhada

cv2.imshow('Imagem de entrada', P)
cv2.imshow('Imagem de saída', R)
cv2.waitKey(0)
cv2.destroyAllWindows()

