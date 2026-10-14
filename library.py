
from abc import ABC, abstractmethod
import cv2

class File(ABC):
    @abstractmethod
    def read(self, fn):
        pass

class TextFile(File):
    def read(self, fn):
        with open(fn, "r") as file:
            print(file.read())

class ImageFile(File):
    def read(self, fn):
        img = cv2.imread(fn)

        if img is None:
            print("Image not found")
            return

        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

class PythonFileFormat(File):
    def read(self, fn):
        with open(fn, "r") as file:
            print(file.read())
