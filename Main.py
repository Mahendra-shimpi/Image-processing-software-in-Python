from tkinter import *
from rembg import remove
from PIL import Image, ImageTk, ImageDraw, ImageFont
import math
from cartoonizer import cartoonize_image
from tkinter import filedialog
# from kdOpencamera import opencamera
import os
import Pmw
import cv2
import sys
import numpy as np

root = Tk()
Pmw.initialise(root)
root.title("Background Remover")
root.geometry('1377x760')
selectedby_cam = False
camselimg=False
# root.attributes("-fullscreen", True) 
# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
header_frame = Frame(root,bg="light gray")
header_frame.pack(side=TOP, fill=X)
kaka=None
input_path=""
nameOfRemFile=None
output_path=None
im=None
img = None
img_path = None
bg_color = None

# img2=ImageTk.PhotoImage(Image.open("box.png"))

def open_img():
    global input_path, my_img, img, img_resized, selectedby_cam
    # input_path = filedialog.askopenfilename(title="Open Image", filetype=(("PNG Files",".png"),("All Files","*.*")))
    # if input_path:
    #     file_name = os.path.basename(input_path)
    #     my_img = Image.open(input_path)
    #     #
    #     width, height = my_img.size
    #     ratio = max(width, height) / 480
    #     new_width = int(width / ratio)
    #     new_height = int(height / ratio)
    #     img_resized = my_img.resize((new_width, new_height), Image.ANTIALIAS)
    #     width, height = img_resized.size
    #     if width < 640 or height < 480:
    #         new_image = Image.new("RGBA", (640, 480), (255, 255, 255, 0))
    #         new_image.paste(img_resized, ((640 - width) // 2, (480 - height) // 2))
    #         img_resized = new_image
    #     img_resized = ImageTk.PhotoImage(img_resized)
    #     # panel.config(image=img_resized)
    #     # panel.image = img_resized
    #     # img1=my_img.resize((420,350))
    #     # img2=ImageTk.PhotoImage(img1)
    #     browseLabel.config(image=img_resized)
    #     browseLabel.image=img_resized
    #     file_name_label.configure(text=file_name)
        
        #######################################################
    input_path = filedialog.askopenfilename(title="Open Image", filetype=(("PNG Files",".png"),("All Files","*.*")))
    if input_path:
        selectedby_cam =False
        file_name = os.path.basename(input_path)
        my_img = Image.open(input_path)
        # width, height = my_img.size
        # ratio = max(width, height) / 480
        # new_width = int(width / ratio)
        # new_height = int(height / ratio)
        # img_resized = my_img.resize((new_width, new_height), Image.ANTIALIAS)
        # width, height = img_resized.size
        # width, height = img_resized.sizepip install Pillow==9.5.0
        # if width < 480 or height < 480:
        #     new_image = Image.new("RGB", (480, 480), (255, 255, 255))
        #     new_image.paste(img_resized, ((480 - width) // 2, (480 - height) // 2))
        #     img_resized = new_image
        resized_image = resize_image(my_img, 480)
        img_resized = ImageTk.PhotoImage(resized_image)
        browseLabel.config(image=img_resized,bg='white') #,relief=SOLID 
        browseLabel.image=img_resized
        file_name_label.configure(text=file_name)
        browseLabel.place(x=165,y=147)
        #################################################
def remove_img():
    global input_path, imgclicked, nameOfRemFile, output_path, im

    if selectedby_cam == True:
        output_path = filedialog.asksaveasfilename(title="Save As", filetype=(("PNG Files",'.png'),("All Files","*.*")))
        input = Image.open("imageCap.png")
        output = remove(input)
        output.save(output_path, 'png')
        # nameOfRemFile=os.path.basename(output_path)
        im = Image.open(output_path)

        inp1 = Image.open(output_path)
        resized_image = resize_image(inp1, 480)
        img4 = ImageTk.PhotoImage(resized_image)
        browseLabel.config(image=img4,bg='white')
        browseLabel.image=img4
        
    else:
        global my_img
        output_path = filedialog.asksaveasfilename(title="Save As", filetype=(("PNG Files",'.png'),("All Files","*.*")))
        input = Image.open(input_path)
        output = remove(input)
        output.save(output_path, 'png')
        inp = Image.open(output_path)
        im = Image.open(output_path)

        resized_image = resize_image(inp, 480)
    im = Image.open(output_path)
    img_resz = ImageTk.PhotoImage(resized_image)
    browseLabel.config(image=img_resz,bg='white')
    browseLabel.image=img_resz
    browseLabel.config(bg='white')
    # browseLabel.pack
    browseLabel.place(x=165,y=147)

def resize_image(image, max_size):
    # Open the image and get its dimensions
    width, height = image.size
    
    # Calculate the ratio by which to resize the image
    ratio = max(width, height) / max_size
    
    # Calculate the new dimensions of the resized image
    new_width = int(width / ratio)
    new_height = int(height / ratio)
    
    # Resize the image
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    
    # If the image is smaller than the desired size, pad it with white
    if new_width < max_size or new_height < max_size:
        padded_image = Image.new("RGB", (max_size, max_size), (255, 255, 255))
        x = (max_size - new_width) // 2
        y = (max_size - new_height) // 2
        padded_image.paste(resized_image, (x, y))
        resized_image = padded_image
    
    return resized_image


# def red():
#     global file_name, nameOfRemFile, browseLabel, output_path
#     from PIL import Image

#     # Open image file
#     im = Image.open(f"{output_path}")

#     # Create new image with desired background color
#     new_bg = Image.new("RGB", im.size, (255, 0, 0))

#     # Paste original image onto new background
#     new_bg.paste(im, (0, 0), im)

#     # Save the modified image
#     browseLabel.config(image=new_bg,bg='white')
#     browseLabel.image=new_bg
    

# def red():
#     global output_path, img_path, bg_color, browseLabel
#     imgforCbg = Image.open(output_path)
#     img_path = output_path
#     photo = ImageTk.PhotoImage(img)
#     # Change the background color of the image to red
#     if imgforCbg:
#         bg_color = (255, 0, 0) # Red
#         img_with_bg = imgforCbg.copy()
#         img_with_bg = img_with_bg.convert("RGBA")
#         datas = img_with_bg.getdata()

#         newData = []
#         for item in datas:
#             if item[0] == 0 and item[1] == 0 and item[2] == 0:
#                 newData.append(bg_color+(255,))
#             else:
#                 newData.append(item)

#         img_with_bg.putdata(newData)

#         # Display the modified image in the label
#         photo = ImageTk.PhotoImage(img_with_bg)
#         browseLabel.config(image=photo)
#         browseLabel.image = photo

def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def switch_bg():
    current_bg = root.cget('bg')

    if current_bg == 'SystemButtonFace':
        root.configure(bg='#262626')
        image_frame.configure(bg='#262626')
        # button_frame.configure(bg='#262626')
        header_frame.configure(bg='#404040')
        # file_name_frame.configure(bg='#262626')
        file_name_label.configure(fg='white')
        file_name_label.configure(bg='#262626')
        logolabel.configure(bg='#404040')
        title_label.configure(bg='#404040')
        description_label.configure(bg='#404040')
        browseLabel.configure(bg='#262626')
        panLeb1.configure(bg="#262626")
        feature_box.configure(bg="#262626")
        color_selectorlbl.configure(bg="#262626")

    else:
        root.configure(bg='SystemButtonFace')                      # SystemButtonFace means deafult color of tkinter
        image_frame.configure(bg='SystemButtonFace')
        # button_frame.configure(bg='SystemButtonFace')
        header_frame.configure(bg='light gray')
        # file_name_frame.configure(bg='SystemButtonFace')
        file_name_label.configure(fg='black')
        file_name_label.configure(bg='SystemButtonFace')
        logolabel.configure(bg='light gray')
        title_label.configure(bg='light gray')
        description_label.configure(bg='light gray')
        browseLabel.configure(bg='SystemButtonFace')
        panLeb1.configure(bg="SystemButtonFace")
        feature_box.configure(bg="SystemButtonFace")
        color_selectorlbl.configure(bg="SystemButtonFace")
        
        
def cam_window():
    global button1, button2, button, lmain, cancel, camIndex, cap, fileName
    import tkinter as tk
    import os
    import cv2
    import sys
    from PIL import Image, ImageTk
    fileName = os.environ['ALLUSERSPROFILE'] + "\WebcamCap.txt"
    cancel = False

    def prompt_ok(event = 0):
        global cancel, button, button1, button2
        cancel = True

        button.place_forget()
        button1 = tk.Button(mainWindow, text="Good Image!", command=saveAndExit)
        button2 = tk.Button(mainWindow, text="Try Again", command=resume)
        button1.place(anchor=tk.CENTER, relx=0.2, rely=0.9, width=150, height=50)
        button2.place(anchor=tk.CENTER, relx=0.8, rely=0.9, width=150, height=50)
        button1.focus()

    def saveAndExit(event = 0):
        global prevImg, my_img, img1, selectedby_cam, file_name, img2
        selectedby_cam =True
        if (len(sys.argv) < 2):
            filepath = "imageCap.png"
        else:
            filepath = sys.argv[1]

        print ("Output file to: " + filepath)
        prevImg.save(filepath)
        # my_img = Image.open("imageCap.png")
        # img1=my_img.resize((420,350))
        
        inp1 = Image.open("imageCap.png")
        width, height = inp1.size
        ratio = max(width, height) / 480
        new_width = int(width / ratio)
        new_height = int(height / ratio)
        img_resized = inp1.resize((new_width, new_height), Image.ANTIALIAS)
        if width < 480 or height < 480:
            new_image = Image.new("RGB", (480, 480), (255, 255, 255))
            new_image.paste(img_resized, ((480 - width) // 2, (480 - height) // 2))
            img_resized = new_image
        

        imgclicked=ImageTk.PhotoImage(img_resized)
        browseLabel.config(image=imgclicked)
        browseLabel.image=imgclicked
        browseLabel.place(x=165,y=200)
        
        
        # mainWindow.quit()


        

#######################################################################################
    def resume(event = 0):
        global button1, button2, button, lmain, cancel

        cancel = False

        button1.place_forget()
        button2.place_forget()

        mainWindow.bind('<Return>', prompt_ok)
        button.place(bordermode=tk.INSIDE, relx=0.5, rely=0.9, anchor=tk.CENTER, width=300, height=50)
        lmain.after(10, show_frame)

    def changeCam(event=0, nextCam=-1):
        global camIndex, cap, fileName

        if nextCam == -1:
            camIndex += 1
        else:
            camIndex = nextCam
        del(cap)
        cap = cv2.VideoCapture(camIndex)

        #try to get a frame, if it returns nothing
        success, frame = cap.read()
        if not success:
            camIndex = 0
            del(cap)
            cap = cv2.VideoCapture(camIndex)

        f = open(fileName, 'w')
        f.write(str(camIndex))
        f.close()

    try:
        f = open(fileName, 'r')
        camIndex = int(f.readline())
    except:
        camIndex = 0

    cap = cv2.VideoCapture(camIndex)
    capWidth = cap.get(3)
    capHeight = cap.get(4)

    success, frame = cap.read()
    if not success:
        if camIndex == 0:
            print("Error, No webcam found!")
            sys.exit(1)
        else:
            changeCam(nextCam=0)
            success, frame = cap.read()
            if not success:
                print("Error, No webcam found!")
                sys.exit(1)

    mainWindow = Toplevel(root)
    # mainWindow = tk.Tk(screenName="Camera Capture")
    # mainWindow.geometry('1200x600')
    mainWindow.resizable(width=False, height=False)
    mainWindow.bind('<Escape>', lambda e: mainWindow.quit())
    lmain = tk.Label(mainWindow, compound=tk.CENTER, anchor=tk.CENTER, relief=tk.RAISED)
    button = tk.Button(mainWindow, text="Capture", command=prompt_ok)
    button_changeCam = tk.Button(mainWindow, text="Switch Camera", command=changeCam)

    lmain.pack()
    button.place(bordermode=tk.INSIDE, relx=0.5, rely=0.9, anchor=tk.CENTER, width=300, height=50)
    button.focus()
    button_changeCam.place(bordermode=tk.INSIDE, relx=0.85, rely=0.1, anchor=tk.CENTER, width=150, height=50)

    def show_frame():
        global cancel, prevImg, button

        _, frame = cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

        prevImg = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=prevImg)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        if not cancel:
            lmain.after(10, show_frame)

    show_frame()

################# sketchify #########################


def convert_to_sketch(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_gray_image = 255 - gray_image

    # Apply Gaussian blur to the inverted grayscale image
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

    # Blend the grayscale image and the blurred image using the color dodge blend mode
    blended_image = cv2.divide(gray_image, 255 - blurred_image, scale=256)

    # Convert the blended image to uint8 datatype
    sketch_image = np.uint8(blended_image)

    return sketch_image

def convert_to_sketch_and_update():
    # Get the current image in the label
    current_image = ImageTk.getimage(browseLabel.image)

    # Convert the image to numpy array
    current_image = np.array(current_image)

    # Convert the image to sketch format
    sketch_image = convert_to_sketch(current_image)

    # Convert the sketch image to PIL Image object
    sketch_image = Image.fromarray(sketch_image)

    # Resize image to fit the label
    # sketch_image = sketch_image.resize((400, 400), Image.ANTIALIAS)

    # Resize the image to a maximum size of 480 pixels
    resized_image = resize_image(sketch_image, 480)
    
    # Convert the image to a PhotoImage for display in a tkinter label widget
    resized_photo = ImageTk.PhotoImage(resized_image)
    
    # Update the tkinter label widget with the resized image
    browseLabel.config(image=resized_photo)
    browseLabel.image = resized_photo
    if selectedby_cam == True:
        browseLabel.place(x=165,y=147)

    # # Display the sketch image in the label
    # sketch_photo = ImageTk.PhotoImage(sketch_image)
    # browseLabel.config(image=sketch_photo)
    # browseLabel.image = sketch_photo


########################### ASCII ART #############################################


def convert_to_ascii():
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
    charArray = list(chars)
    charLength = len(charArray)
    interval = charLength/256

    scaleFactor = 0.09

    oneCharWidth = 10
    oneCharHeight = 18
    def getChar(inputInt):
        return charArray[math.floor(inputInt*interval)]
    
    text_file = open("Output.txt", "w")

    global browseLabel
    # Get the current image in the label
    current_image = ImageTk.getimage(browseLabel.image)
    

    im = Image.open(current_image)
    fnt = ImageFont.truetype('C:\\Windows\\Fonts\\arial.ttf', 15)
    width, height = im.size
    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), resample=Image.NEAREST)
    width, height = im.size
    pix = im.load()
    outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
    d = ImageDraw.Draw(outputImage)
    for i in range(height):
        for j in range(width):
            try:
                r, g, b, a = pix[j, i]
            except ValueError:
                r, g, b = pix[j, i]
            gray = int(r/3 + g/3 + b/3)
            pix[j, i] = (gray, gray, gray)
            text_file.write(getChar(gray))
            d.text((j*oneCharWidth, i*oneCharHeight), getChar(gray), font=fnt, fill=(r, g, b))
    browseLabel.config(image=outputImage)


image_frame = Frame(root)
image_frame.pack(side=TOP, fill=BOTH, expand=True)

pannelbox = ImageTk.PhotoImage(Image.open('box.png').resize((750,550),Image.ANTIALIAS))
panLeb1=Label(root,image=pannelbox)
panLeb1.place(x=20,y=115)

browseLabel = Label(root, text='', bg='white') #,relief="solid"
browseLabel.place(x=165,y=147)
 

################# Features pannel #########################

feautureboximg = ImageTk.PhotoImage(Image.open('boxv2.png').resize((510,550),Image.ANTIALIAS))
feature_box=Label(root,image=feautureboximg)
feature_box.place(x=845, y=115)

sketch = ImageTk.PhotoImage(Image.open('sketchify.png').resize((62,62),Image.ANTIALIAS))
sketchbutton=Button(root, image=sketch,  command=convert_to_sketch_and_update)
sketchbutton.place(x=890,y=150)
balloon1 = Pmw.Balloon(root)
balloon1.bind(sketchbutton,"Convert your image to Sketch")
lbl = balloon1.component("label")
lbl.config(background="black", foreground="white")

remover_img = ImageTk.PhotoImage(Image.open('removebg_logo.jpg').resize((62,62),Image.ANTIALIAS))
button2 = Button(root, image=remover_img)
button2.place(x=980,y=150)
balloon2 = Pmw.Balloon(root)
balloon2.bind(button2,"Remove the background of Your image")
lbl = balloon2.component("label")
lbl.config(background="black", foreground="white")

cartoonize_img = ImageTk.PhotoImage(Image.open('cartoonize_logo.png').resize((62,62),Image.ANTIALIAS))
button3 = Button(root, image=cartoonize_img)
button3.place(x=1070,y=150)
balloon3 = Pmw.Balloon(root)
balloon3.bind(button3,"Convert your image into Cartoon Art")
lbl = balloon3.component("label")
lbl.config(background="black", foreground="white")

ascii_img = ImageTk.PhotoImage(Image.open('ascii_art_icon.png').resize((62,62),Image.ANTIALIAS))
button4 = Button(root, image=ascii_img, command=convert_to_ascii)
button4.place(x=1160,y=150)
balloon17 = Pmw.Balloon(root) 
balloon17.bind(button4,"Convert your image to ASCII Art (0101 Art/Text Art)")
lbl = balloon17.component("label")
lbl.config(background="black", foreground="white")


face_shape = Button(root, image=sketch)
face_shape.place(x=1250,y=150)
balloon19 = Pmw.Balloon(root) 
balloon19.bind(face_shape,"Check Your Face Shape")
lbl = balloon19.component("label")
lbl.config(background="black", foreground="white")


color_selectorimg = ImageTk.PhotoImage(Image.open('color section1.png').resize((85,550),Image.ANTIALIAS))
color_selectorlbl=Label(root,image=color_selectorimg)
color_selectorlbl.place(x=770,y=110)

colpanllbl=Label(root,text="",bg="white")
colpanllbl.place(x=790,y=150)

################# Bg color changer functions #########################
 
def red():
    global im, bg_color, browseLabel
    
    if im:
        # Change the background color of the image to red
        bg_color = (255, 0, 0) # Red
        img_with_bg = im.copy()
        img_with_bg = img_with_bg.convert("RGBA")
        datas = img_with_bg.getdata()
        
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append(bg_color+(255,))
            else:
                newData.append(item)
                
        img_with_bg.putdata(newData)
        resized_image = resize_image(img_with_bg, 480)
        # Display the modified image in the label
        photo = ImageTk.PhotoImage(resized_image)
        browseLabel.config(image=photo)
        browseLabel.image = photo

def purple(): 
    global im, bg_color, browseLabel
    
    if im:
        # Change the background color of the image
        bg_color = (128, 0, 128)
        img_with_bg = im.copy()
        img_with_bg = img_with_bg.convert("RGBA")
        datas = img_with_bg.getdata()
        
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append(bg_color+(255,))
            else:
                newData.append(item)
                
        img_with_bg.putdata(newData)
        resized_image = resize_image(img_with_bg, 480)
        # Display the modified image in the label
        photo = ImageTk.PhotoImage(resized_image)
        browseLabel.config(image=photo)
        browseLabel.image = photo

def black():
    global im, bg_color, browseLabel
    
    if im:
        # Change the background color of the image
        bg_color = (0, 0, 0) # Red
        img_with_bg = im.copy()
        img_with_bg = img_with_bg.convert("RGBA")
        datas = img_with_bg.getdata()
        
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append(bg_color+(255,))
            else:
                newData.append(item)
                
        img_with_bg.putdata(newData)
        resized_image = resize_image(img_with_bg, 480)
        # Display the modified image in the label
        photo = ImageTk.PhotoImage(resized_image)
        browseLabel.config(image=photo)
        browseLabel.image = photo
    
def orange():
    global im, bg_color, browseLabel
    
    if im:
        # Change the background color of the image
        bg_color = (255, 165, 0) # Red
        img_with_bg = im.copy()
        img_with_bg = img_with_bg.convert("RGBA")
        datas = img_with_bg.getdata()
        
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append(bg_color+(255,))
            else:
                newData.append(item)
                
        img_with_bg.putdata(newData)
        resized_image = resize_image(img_with_bg, 480)
        # Display the modified image in the label
        photo = ImageTk.PhotoImage(resized_image)
        browseLabel.config(image=photo)
        browseLabel.image = photo
    
def green():
    global im, bg_color, browseLabel
    
    if im:
        # Change the background color of the image
        bg_color = (0, 128, 0) # Red
        img_with_bg = im.copy()
        img_with_bg = img_with_bg.convert("RGBA")
        datas = img_with_bg.getdata()
        
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append(bg_color+(255,))
            else:
                newData.append(item)
                
        img_with_bg.putdata(newData)
        resized_image = resize_image(img_with_bg, 480)
        # Display the modified image in the label
        photo = ImageTk.PhotoImage(resized_image)
        browseLabel.config(image=photo)
        browseLabel.image = photo
    
def lime():
    global im, bg_color, browseLabel
    
    if im:
        # Change the background color of the image
        bg_color = (0, 255, 0) # Red
        img_with_bg = im.copy()
        img_with_bg = img_with_bg.convert("RGBA")
        datas = img_with_bg.getdata()
        
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append(bg_color+(255,))
            else:
                newData.append(item)
                
        img_with_bg.putdata(newData)
        resized_image = resize_image(img_with_bg, 480)
        # Display the modified image in the label
        photo = ImageTk.PhotoImage(resized_image)
        browseLabel.config(image=photo)
        browseLabel.image = photo
    
def white():
    global im, bg_color, browseLabel
    
    if im:
        # Change the background color of the image
        bg_color = (255, 255, 255) # Red
        img_with_bg = im.copy()
        img_with_bg = img_with_bg.convert("RGBA")
        datas = img_with_bg.getdata()
        
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append(bg_color+(255,))
            else:
                newData.append(item)
                
        img_with_bg.putdata(newData)
        resized_image = resize_image(img_with_bg, 480)
        # Display the modified image in the label
        photo = ImageTk.PhotoImage(resized_image)
        browseLabel.config(image=photo)
        browseLabel.image = photo
    
def lavender():
    global im, bg_color, browseLabel
    
    if im:
        # Change the background color of the image
        bg_color = (230, 230, 250) # Red
        img_with_bg = im.copy()
        img_with_bg = img_with_bg.convert("RGBA")
        datas = img_with_bg.getdata()
        
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append(bg_color+(255,))
            else:
                newData.append(item)
                
        img_with_bg.putdata(newData)
        resized_image = resize_image(img_with_bg, 480)
        # Display the modified image in the label
        photo = ImageTk.PhotoImage(resized_image)
        browseLabel.config(image=photo)
        browseLabel.image = photo

def nonefun():
    browseLabel.config(bg="SystemButtonFace")


def save_image():
    global browseLabel
    # Get the current image in the label
    current_image = ImageTk.getimage(browseLabel.image)

    # Open file dialog to choose a save location
    file_path = filedialog.asksaveasfilename(defaultextension=".png")

    if file_path:
        # Save the current image to the chosen location
        current_image.save(file_path)
     
    
b1=Button(colpanllbl, text="", bg="red", width=3, height=2,relief=RIDGE, command=red)
b1.grid(row=0,column=0, padx=5,pady=5)
balloon6 = Pmw.Balloon(root)
balloon6.bind(b1,"red")
lbl = balloon6.component("label")
lbl.config(background="black", foreground="white")

b2=Button(colpanllbl, text="", bg="purple", width=3, height=2,relief=RIDGE, command=purple)
b2.grid(row=1,column=0, padx=5,pady=5)
balloon7 = Pmw.Balloon(root)
balloon7.bind(b2,"purple")
lbl = balloon7.component("label")
lbl.config(background="black", foreground="white")


b3=Button(colpanllbl, text="", bg="black", width=3, height=2,relief=RIDGE, command=black)
b3.grid(row=2,column=0, padx=5,pady=5)
balloon8 = Pmw.Balloon(root)
balloon8.bind(b3,"black")
lbl = balloon8.component("label")
lbl.config(background="black", foreground="white")


b4=Button(colpanllbl, text="", bg="orange", width=3, height=2,relief=RIDGE, command=orange)
b4.grid(row=3,column=0, padx=5,pady=5)
balloon9 = Pmw.Balloon(root)
balloon9.bind(b4,"orange")
lbl = balloon9.component("label")
lbl.config(background="black", foreground="white")


b5=Button(colpanllbl, text="", bg="green", width=3, height=2,relief=RIDGE, command=green)
b5.grid(row=4,column=0, padx=5,pady=5)
balloon10 = Pmw.Balloon(root)
lbl = balloon10.component("label")
lbl.config(background="black", foreground="white")

balloon10.bind(b5,"green")

b6=Button(colpanllbl, text="", bg="lime", width=3, height=2,relief=RIDGE, command=lime)
b6.grid(row=5,column=0, padx=5,pady=5)
balloon11 = Pmw.Balloon(root)
balloon11.bind(b6,"lime")
lbl = balloon11.component("label")
lbl.config(background="black", foreground="white")


b7=Button(colpanllbl, text="", bg="white", width=3, height=2,relief=RIDGE, command=white)
b7.grid(row=6,column=0, padx=5,pady=5)
balloon12 = Pmw.Balloon(root)
balloon12.bind(b7,"white")
lbl = balloon12.component("label")
lbl.config(background="black", foreground="white")


b8=Button(colpanllbl, text="", bg="lavender", width=3, height=2,relief=RIDGE, command=lavender)
b8.grid(row=8,column=0, padx=5,pady=5)
balloon13 = Pmw.Balloon(root)
balloon13.bind(b8,"lavender")
lbl = balloon13.component("label")
lbl.config(background="black", foreground="white")



noneimg = ImageTk.PhotoImage(Image.open('none.png').resize((30,30),Image.ANTIALIAS))
b9=Button(colpanllbl, image=noneimg, bg="white",relief=FLAT)
b9.grid(row=9, column=0,padx=5,pady=20)
balloon14 = Pmw.Balloon(root)
balloon14.bind(b9,"None")
lbl = balloon14.component("label")
lbl.config(background="black", foreground="white")

 
logo = ImageTk.PhotoImage(Image.open('main-logo.png').resize((80,80),Image.ANTIALIAS))
logolabel=Label(header_frame, image=logo,bg="light gray")
logolabel.pack(side=LEFT, pady=10)

title_label = Label(header_frame, text="Remove.bg LITE By - Mahi", font=("Unispace", 24),fg="gray",bg="light gray")
title_label.pack(side=LEFT, padx=10)

description_label = Label(header_frame, text="Easily remove the background of any image",bg="light gray",fg="red", font=("Lucida Sans Typewriter", 14))
description_label.pack(side=LEFT, padx=10)

root.configure(background='SystemButtonFace')
Switch = Button(header_frame, text='Light-Dark', command=switch_bg, bg='black', fg='white',font=("Helvetica", 10),relief=RIDGE)
Switch.pack(side=RIGHT, anchor=CENTER, padx=10)
balloon6 = Pmw.Balloon(root)
balloon6.bind(Switch,"Change App Theme")
lbl = balloon6.component("label")
lbl.config(background="black", foreground="white")




# myscrollbar=Scrollbar(image_frame, orient="vertical")
# myscrollbar.pack(side="right",fill="y")

# file_name_frame = Frame(root, bg="yellow")
# file_name_frame.place(x=0,y=50)


# button_frame = Frame(root,bg="red")
# button_frame.place(x=0,y=200)

open_button = Button(root, text = "Select Image", command=open_img,bg="#3b5998",fg="white", font=("Helvetica", 12),relief=RIDGE)
open_button.place(x=70,y=660)
balloon15 = Pmw.Balloon(root)
balloon15.bind(open_button,"Browse Image")
lbl = balloon15.component("label")
lbl.config(background="black", foreground="white")


removebg_button = Button(root, text="Remove BG", command=remove_img,bg="red",fg="black", font=("Helvetica", 12),relief=RIDGE)
removebg_button.place(x=195,y=660)
balloon16 = Pmw.Balloon(root)
balloon16.bind(removebg_button,"Remove the background of Your image")
lbl = balloon16.component("label")
lbl.config(background="black", foreground="white")

cambutton = Button(root, text='Open Camera',command=cam_window,fg="black", font=("Helvetica", 12),relief=RIDGE)
cambutton.place(x=310,y=660)
changeOnHover(cambutton, "gray", "white")
balloon4 = Pmw.Balloon(root)
balloon4.bind(cambutton,"Click a Photo")
lbl = balloon4.component("label")
lbl.config(background="black", foreground="white")


file_name_label = Label(root, text="No file selected", font=("Helvetica", 12))
file_name_label.place(x=440,y=663)

save_btn=Button(header_frame, text = "Save",bg="red",fg="black", command=save_image, font=("Helvetica", 12),relief=RIDGE)
save_btn.pack(side=RIGHT, anchor=CENTER, padx=15)
balloon5 = Pmw.Balloon(root)
balloon5.bind(save_btn,"Save current image of Photo Panel")
lbl = balloon5.component("label")
lbl.config(background="black", foreground="white")


# footer_frame1 = Frame(root,bg="black")
# footer_frame1.pack(side=BOTTOM, fill=X)

root.mainloop()

'''converted=str(input_path)
        splt=converted.split("/")
        last=splt[-1]'''

        



