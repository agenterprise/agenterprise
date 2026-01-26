import svgwrite

# Parameter
size = 240
rows = cols = 12
cell = 18
spacing = 2

# Farbverlauf: Orange (oben links) nach Weiß (unten rechts)
start_color = (128, 128, 0)  # Olive
end_color = (128, 0, 128)  # Weiß

def lerp(a, b, t):
    return int(a + (b - a) * t)

def color_at(i, j):
    t = ((i + j) / (rows + cols - 2))
    r = lerp(start_color[0], end_color[0], t)
    g = lerp(start_color[1], end_color[1], t)
    b = lerp(start_color[2], end_color[2], t)
    return f'rgb({r},{g},{b})'


# Mask für stilisierte Enterprise mit "A" unter der Spitze
enterprise_mask = [
    # 0
    [False,False,False,False,True,False,False,True,False,False,False,False],
    # 1: "A" unter der Spitze
    [False,False,False,True,False,True,True,False,True,False,False,False],
    # 2: Querstrich des "A"
    [False,False,True,False,False,False,False,False,False,True,False,False],
    # 3
    [False,True,False,True,True,True,True,True,True,False,True,False],
    # 4
    [True,False,True,True,True,True,True,True,True,True,False,True],
    # 5
    [False,False,False,True,True,True,True,True,True,False,False,False],
    # 6
    [False,False,False,False,True,True,True,True,False,False,False,False],
    # 7
    [False,False,False,True,True,True,True,True,True,False,False,False],
    # 8
    [False,False,False,True,True,True,True,True,True,False,False,False],
    # 9
    [False,False,False,True,False,False,False,False,True,False,False,False],
    # 10
    [False,False,True,False,False,False,False,False,False,True,False,False],
    # 11
    [False,True,False,False,False,False,False,False,False,False,True,False],
]

dw = svgwrite.Drawing('grid.svg', size=(size, size))
for i in range(rows):
    for j in range(cols):
        x = j * (cell + spacing)
        y = i * (cell + spacing)
        if enterprise_mask[i][j]:
            color = 'white'
        else:
            color = color_at(i, j)
        dw.add(dw.rect(insert=(x, y), size=(cell, cell), fill=color))
dw.save()
