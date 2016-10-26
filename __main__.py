
print("Hello Migas")
import cv2

# Reading images

dish = cv2.imread('images/dish0.jpg')
cv2.imshow('dish', dish)
cv2.waitKey(0)
cv2.destroyAllWindows()
