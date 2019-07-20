import cv2

dataset=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture=cv2.VideoCapture(0)
dog=cv2.imread('dog.png')
hat=cv2.imread('hat.png')
glass=cv2.imread('glasses.png')


def glass_filter(glass,img,x,y,w,h):
    face_width=w
    face_height=h
    glass_width=int(face_width+2)
    glass_height=int(face_height*0.5)

    glass=cv2.resize(glass,(glass_width,glass_height))
    for i in range(glass_height):
        for j in range(glass_width):
            for k in range(3):
                if glass[i][j][k]<155:
                    img[y+i- int(-0.20 * face_height)][x+j][k]=glass[i][j][k]
    return img

    
def hat_filter(hat,img,x,y,w,h):
    face_width=w
    face_height=h
    hat_width=face_width+2
    hat_height=face_height*0.50

    hat=cv2.resize(hat,(int(hat_width),int(hat_height)))
    for i in range(int(hat_height)):
        for j in range(int(hat_width)):
            for k in range(3):
                if hat[i][j][k]<235:
                    img[y+i-int(0.50*w)][x+j-1][k]=hat[i][j][k]
    return img
                    
                       
def dog_filter(dog,img,x,y,w,h):
    face_width=w
    face_height=h
    dog_w=int(face_width*1.5)
    dog_h=int(face_height*1.95)

    dog=cv2.resize(dog,(dog_w,dog_h))
    for i in range(dog_h):
        for j in range(dog_w):
            for k in range(3):
                if dog[i][j][k]<235:#pixel color compare 
                    img[y+i-int(0.375*h)-1][x + j - int(0.35 * w)][k]=dog[i][j][k]
            
    return img

filter_type=int(input("Enter your choice : "))


while True:
    ret,img=capture.read()
    global fil
    if ret:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=dataset.detectMultiScale(gray,1.3)
        for x,y,w,h in faces:
            if filter_type==1:
                fil=glass_filter(glass,img,x,y,w,h)
            elif filter_type==2:
                fil=hat_filter(hat,img,x,y,w,h)

            elif filter_type==3:
                fil=dog_filter(dog,img,x,y,w,h)
            

        if cv2.waitKey(1)==27:
            break
    cv2.imshow('result',fil)
    
capture.release()
cv2.destroyAllWindows()

            
