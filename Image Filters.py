from skimage import io, data, filters, color, exposure, util, morphology
from skimage import transform as tr
from tkinter import *
from tkinter import Menu, filedialog, messagebox
from PIL import ImageTk,Image
import cv2
# canvasCurrentImage = None

class Window(Frame):


    def __init__(self):
        self.image = None
        self.originalImage = data.camera()
        self.window = Tk()
        self.canvas = Canvas(self.window, width = 500, height = 500)
        self.canvas.pack(fill = BOTH, expand = YES)
        self.window.title("Image Processing")

        self.rawImage = data.camera()
        self.image = Image.fromarray(tr.resize(self.rawImage,[500,500])*255)
        self.img =  ImageTk.PhotoImage(image=self.image)
        self.canvasCurrentImage = self.canvas.create_image(0,0, anchor="nw", image=self.img)



        menu = Menu(self.window)
        file = Menu(menu)
        menu.add_cascade(label='File', menu=file)
        file.add_command(label="Open File", command=self.openFile)
        file.add_command(label="Save As", command=self.saveFile)
        file.add_command(label="Original Image", command=self.original)


        filters = Menu(menu)
        menu.add_cascade(label='Filters', menu=filters)
        filters.add_command(label="Gaussian", command = self.gaussian)
        filters.add_command(label="Median", command = self.median)
        filters.add_command(label="Sobel", command = self.sobel)
        filters.add_command(label="Scharr", command = self.scharr)
        filters.add_command(label="Gabor", command = self.gabor)
        filters.add_command(label="Hessian", command = self.hessian)
        filters.add_command(label="Roberts", command = self.roberts)
        filters.add_command(label="Prewitt", command = self.prewitt)
        filters.add_command(label="Local Treshold", command = self.localTreshold)
        filters.add_command(label="Unsharp Mask", command = self.unsharpMask)


        histogram = Menu(menu)
        menu.add_cascade(label='Histograms', menu=histogram)
        histogram.add_command(label="Histogram", command= self.hist)
        histogram.add_command(label="Equalize Histogram", command=self.equalizeHist)

        transform = Menu(menu)
        menu.add_cascade(label='Transform', menu=transform)
        transform.add_command(label="Resize", command=self.resize)
        transform.add_command(label="Rotate", command=self.rotate)
        transform.add_command(label="Rescale", command=self.rescale)
        transform.add_command(label="Swirl", command=self.swirl)
        transform.add_command(label="Pyramid Reduce", command=self.pyramidReduce)



        rescale = Menu(menu)
        menu.add_cascade(label='RescaleIntensity', menu=rescale)
        rescale.add_command(label="RescaleIntensity", command=self.rescaleIntensity)


        morphology = Menu(menu)
        menu.add_cascade(label='Morphology', menu=morphology)
        morphology.add_command(label="Binary Erosion", command=self.binaryErosion)
        morphology.add_command(label="Closing",command=self.closing)
        morphology.add_command(label="White Tophat",command=self.whiteTophat)
        morphology.add_command(label="Black Tophat", command=self.blackTophat)
        morphology.add_command(label="Opening", command=self.opening)
        morphology.add_command(label="Skeletonize", command=self.skeletonize)
        morphology.add_command(label="Thin", command=self.thin)
        morphology.add_command(label="Medial Axis", command=self.medialAxis)
        morphology.add_command(label="Convex Hull", command=self.convexHull)
        morphology.add_command(label="Dilation", command=self.dilation)

        videoCapture = Menu(menu)
        menu.add_cascade(label='Video', menu=videoCapture)
        videoCapture.add_command(label = "Video Capture", command = self.canny)

        self.window.config(menu=menu)
        messagebox.showinfo('Önemli', 'Uygulama üstte bulunan menubar aracılığıyla kontrol ediliyor' \
        + "\nresimler üzerinde işlem yapılırsa her işlem üstüste yapılacaktır" \
        + "\neğer bu istenmiyorsa File kısmından yeni resim yüklenebilir" \
        + "\nyada enson yüklenmiş resmin orjinaline geri dönülebilir.")


        self.window.mainloop()

    def openFile(self):
        file_path = filedialog.askopenfilename()
        if file_path != '':
            image = self.readFile(file_path)

    def showImage(self, img):

        self.image = Image.fromarray((tr.resize(img,[500,500])*255))
        self.img = ImageTk.PhotoImage(image=self.image)
        self.canvas.itemconfig(self.canvasCurrentImage, image = self.img)

    def showImage3(self, img):

        self.image = Image.fromarray((tr.resize(img,[500,500])))
        self.img = ImageTk.PhotoImage(image=self.image)
        self.canvas.itemconfig(self.canvasCurrentImage, image = self.img)

    def showImage2(self, img):

        self.image = Image.fromarray(img*255)
        self.img = ImageTk.PhotoImage(image=self.image)
        self.canvas.itemconfig(self.canvasCurrentImage, image = self.img)

    def readFile(self, filename):

        img = io.imread(filename)
        img = color.rgb2gray(img)
        self.showImage(img)

        self.rawImage = img
        self.originalImage = img

    def saveFile(self):
        self.image = self.image.convert("L")
        a = self.image.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file")
        self.image.save(a)
        print("Save succesfull")

    def original(self):
        self.rawImage = self.originalImage
        self.showImage(self.rawImage)

    def gaussian(self):
        filteredImage = filters.gaussian(self.rawImage, sigma= 2)
        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Gaussian")

    def median(self):
        filteredImage = filters.median(self.rawImage)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Median")

    def sobel(self):
        filteredImage = filters.sobel(self.rawImage)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Sobel")

    def scharr(self):
        filteredImage = filters.scharr(self.rawImage)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Scharr")

    def gabor(self):
        filteredImage,x = filters.gabor(self.rawImage, frequency=0.1)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Gabor")

    def hessian(self):
        filteredImage = filters.hessian(self.rawImage)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Hessian")
    def roberts(self):
        filteredImage = filters.roberts_pos_diag(self.rawImage)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Roberts")

    def prewitt(self):
        filteredImage = filters.prewitt_v(self.rawImage)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Prewitt")

    def localTreshold(self):
        filteredImage = filters.threshold_local(self.rawImage, 7)

        self.showImage3(filteredImage)
        self.rawImage = filteredImage
        print("Local Treshold")

    def unsharpMask(self):
        filteredImage = filters.unsharp_mask(self.rawImage, 2.5)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Unsharp Mask")

    def hist(self):
        import matplotlib.pyplot as plt

        from skimage.util import img_as_ubyte
        from skimage import data, color
        from skimage.exposure import histogram

        # noisy_image = img_as_ubyte(color.rgb2gray(data.moon()))
        hist, hist_centers = histogram(self.rawImage)

        fig, ax = plt.subplots(ncols=2, figsize=(10, 5))

        ax[0].imshow(self.rawImage, cmap=plt.cm.gray)
        ax[0].axis('off')

        ax[1].plot(hist_centers, hist, lw=2)
        ax[1].set_title('Histogram of grey values')

        plt.tight_layout()
        plt.show()

    def equalizeHist(self):
        filteredImage = exposure.equalize_hist(self.rawImage)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Equalize Histogram")

    def resize(self):
        filteredImage = tr.resize(self.rawImage, [400,400])

        self.showImage2(filteredImage)
        self.rawImage = filteredImage
        print("Resize")

    def rotate(self):
        filteredImage = tr.rotate(self.rawImage, 90)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Rotate")

    #BAK
    def rescale(self):
        filteredImage = tr.rescale(self.rawImage, (0.9, 0.6))

        self.showImage2(filteredImage)
        self.rawImage = filteredImage
        print("Rescale")

    def swirl(self):
        filteredImage = tr.swirl(self.rawImage, (50,50), radius=150, rotation=45)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Swirl")

    def pyramidReduce(self):
        filteredImage = tr.pyramid_reduce(self.rawImage, 1.8)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Pyramid Reduce")

    def rescaleIntensity(self):
        top=self.top=Toplevel(self.window)
        self.l=Label(top,text="Hello World")
        self.l.pack()
        self.e=Entry(top)
        self.e.insert(END, '12,3')
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()


        self.b["state"] = "active"
        self.window.wait_window(self.top)
        # self.b["state"] = "normal"

        print(self.value)

        ne = self.value.split(',')
        irange=tuple(map(int,ne))

        filteredImage = exposure.rescale_intensity(self.rawImage,irange)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Rescale Intensity")

    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

    def binaryErosion(self):
        filteredImage = morphology.binary_erosion(data.horse()==0)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("binaryErosion")

    def closing(self):
        filteredImage = morphology.closing(self.rawImage)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("closing")

    def whiteTophat(self):
        filteredImage = morphology.white_tophat(self.rawImage)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("White Tophat")

    def blackTophat(self):
        filteredImage = morphology.black_tophat(self.rawImage)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Black Tophat")

    def opening(self):
        filteredImage = morphology.opening(self.rawImage)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Opening")

    def skeletonize(self):
        filteredImage = morphology.skeletonize(data.horse()==0)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Skeletonize")

    def thin(self):
        filteredImage = morphology.thin(data.horse()==0)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Thin")

    def medialAxis(self):
        filteredImage = morphology.medial_axis(data.horse()==0)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Medial Axis")

    def convexHull(self):
        filteredImage = morphology.convex_hull_image(util.invert(data.horse()))

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Convex Hull")

    def dilation(self):
        filteredImage = morphology.dilation(self.rawImage)

        self.showImage(filteredImage)
        self.rawImage = filteredImage
        print("Dilation")

    def canny(self):
        vid =cv2.VideoCapture(filedialog.askopenfilename())
        while True:
            ret, frame = vid.read()

            frame = cv2.GaussianBlur(frame, (7, 7), 1.41)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            edge = cv2.Canny(frame, 25, 75)


            cv2.imshow('Edge Detection', edge)


            if cv2.waitKey(20) == ord('q'):
                break


        cap.release()
        cv.destroyAllWindows()

Window()
