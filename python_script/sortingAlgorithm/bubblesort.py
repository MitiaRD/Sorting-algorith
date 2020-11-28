from tkinter import *
from tkinter import ttk
import random
from bubblesortfunc import bubbleSort

root = Tk()
root.title('Bubble sort')
root.maxsize(900, 600)
root.config(bg='grey')

# variable
selected_alg = StringVar()
data = []
# functions


def drawData(data):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data)+1)
    offset = 30
    spacing = 10
    normalizedData = [i/max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i*x_width + offset + spacing
        y0 = c_height - height * 340

        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


def generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    drawData(data)


def startAlgorith():
    global data
    bubbleSort(data, drawData, speedScale.get())


# ui frame
UiFrame = Frame(root, width=600, height=200, bg="orange")
UiFrame.grid(row=0, column=0, padx=10, pady=5)

# canvas
canvas = Canvas(root, width=600, height=380, bg="blue")
canvas.grid(row=1, column=0, padx=10, pady=5)

# ui area
# row[0]
Label(UiFrame, text="Algorithm", bg="white").grid(
    row=0, column=0, padx=5, sticky=W)
algMenu = ttk.Combobox(UiFrame, textvariable=selected_alg,
                       values=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UiFrame, from_=0.1, to=2.0, length=200, digits=2,
                   resolution=0.2, orient=HORIZONTAL, label="Select Speed")

speedScale.grid(row=0, column=2, padx=5, pady=5)

Button(UiFrame, text="Start", command=startAlgorith,
       bg='red').grid(row=0, column=3, padx=5, pady=5)
# row[1]

sizeEntry = Scale(UiFrame, from_=3, to=25,
                  resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(
    row=1, column=0, padx=5, pady=5)


minEntry = Scale(UiFrame, from_=0, to=10,
                 resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(
    row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UiFrame, from_=10, to=100,
                 resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(
    row=1, column=2, padx=5, pady=5)
Button(UiFrame, text="Generate", command=generate,
       bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
