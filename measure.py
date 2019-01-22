import numpy as np
import pylab
import math
import matplotlib.image as mpimg

photo_dir = "C:/Users/teongleong/Downloads/Eye photos/Additional Prototype Images/Additional Prototype Images/"
folder32 = "M32 Prototype/"
folder33 = "M33 Prototype/"

photo_32_prefix = "20180906_145"
photo_32_index = ["312", "316", "318", "321", "322", "325", "327", "352", "358", "359", "402"]

photo_33_prefix = "20180911_09"
photo_33_index = ["3943", "3944", "3946", "3949", "4002", "4006", "4007", "4012", "4051", "4054", "4057", "4058", "4100"]



fig = pylab.figure()
# #fig = pylab.gcf()

linepoints = np.array([])

def onclick(event):
    #pylab.clf()
    if event.button == 1:
        global linepoints, pylab

        x = event.xdata
        y = event.ydata

        linepoints = np.append(linepoints, x)
        linepoints = np.append(linepoints, y)
        #fig.lines.pop(0).remove()
        if np.size(linepoints) == 4:
            pylab.plot((linepoints[0], linepoints[2]),
                        (linepoints[1], linepoints[3]), '-')
            dx = linepoints[2] - linepoints[0]
            dy = linepoints[3] - linepoints[1]
            len = math.sqrt(math.fabs(dx*dx + dy*dy))
            print(len)

            linepoints = np.array([])
            #
            #pylab.imshow(img)
            pylab.show()

def handle_img(img_name):
    #img = mpimg.imread('M32_P.jpg')
    img = mpimg.imread(img_name)

    # (ni/nr)sin(ti)
    pylab.imshow(img)
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    pylab.show()  # show the plot


#handle_img(photo_dir + folder32 + photo_32_prefix + photo_32_index[3] + ".jpg")
handle_img(photo_dir + folder33 + photo_33_prefix + photo_33_index[3] + ".jpg")
