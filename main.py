import cv2  #!pip install opencv-python
import mediapipe as mp #!pip install mediapipe 

webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils 

while True: 
    # Ler as informações da webcam
    verificador, frame = webcam.read()
    if not verificador:
        break 
    # reconhecer os rostos que tem ali dentro 
    lista_rostos = reconhecedor_rostos.process(frame)
    
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            # desenhar os rosros na imagem
            desenho.draw_detection(frame, rosto)

    cv2.imshow("Rostos na Webcam", frame)

    # quando aperetar ESC, para o loop
    if cv2.waitKey(5) == 27: #27 = tecla "ESC"
        break

webcam.release() 
cv2.destroyAllWindows()