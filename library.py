from abc import ABC, abstractmethod
from time import process_time
import cv2
class File(ABC):
    
    @abstractmethod
    def read(self, fn):
        pass
   

class TextFile(File):
    def read(self, fn):
        
            with open(fn, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line) 
class ImageFile(File):
   def read(self,fn): 
   

    img = cv2.imread(fn, cv2.IMREAD_COLOR)
   
    


    cv2.imshow("Image", img)
    cv2.waitKey(0)  # Wait for any key press
    cv2.destroyAllWindows()  # Close all OpenCV windows
   
class PythonFileFormat(File):
    def read(self,fn):
  
        with open(fn, 'r') as file:
            content = file.read()
            
            print(content)


def process_file(file_obj, filename):
        file_obj.read(filename)

TextFilee=input("enter the file type")
filename = input("Enter the filename: ")
obj = globals()[TextFilee]() 
process_file(obj, filename)
