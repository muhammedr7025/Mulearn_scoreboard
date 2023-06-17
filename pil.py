

from PIL import Image, ImageDraw, ImageFont
from numerize import numerize
from io import BytesIO
from urllib.request import urlopen
background = Image.open("Dboard.png")
karma_color = "rgb(255, 80, 89)"
color = "white"
font = ImageFont.truetype("PlusJakartaSans-Bold.ttf", 30) # size of name
font_karma = ImageFont.truetype("Inter-Black.ttf", 50)  #size of karma
font_college = ImageFont.truetype("PlusJakartaSans-Medium.ttf", 18) #size of college
total_score = {'434916213064466444': {'full_name': 'Aashish Vinu', 'karma': 12544, 'orgs': ['Acme Corporationsda ds', 'Acme Corporationsda ds', 'Acme Corporationsda ds']}, '739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 2400, 'orgs': ['Globex Industries Checking The Woking DUh']}, '821366753594310676': {'full_name': 'dhannu d', 'karma': 600, 'orgs': [None]}}
x, y = 0,0
c = 1
for discord_id, data in total_score.items():
    if c >= 13:
        break

    url = "https://assets.mulearn.org/misc/user.png"
    response = urlopen(url)
    avatar = BytesIO(response.read())
    im = Image.open(avatar)
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.LANCZOS)
    im.putalpha(mask)
    im = im.resize((85, 85)) #size of image
    draw = ImageDraw.Draw(background)
    background.paste(im, ( x+140,y+400), im)
    
    name = data["full_name"]
    if len(name) > 18:
        name = name.split(" ")
        if len(name) > 1:
            name = name[0] + " " + name[1]
            if len(name) > 19:
                name = name.split(" ")
                name = name[0] + " " + name[1][0].capitalize()
        else:
            name = str(name[0])
    draw.multiline_text(( x+240,y+400), name, fill=color, font=font, align="center")
    name = data["orgs"]
    
    if len(name) > 29 and name[0] not None:
        first_line = name[:25]
        second_line = name[25:].strip()
        if second_line and second_line[0].isalpha() and first_line[-1].isalpha():
            split_index = first_line.rfind(' ')
            if split_index == -1:
                split_index = 25
            second_line = name[split_index:].strip()
            first_line = name[:split_index].strip()
        draw.multiline_text((  x+240,y+440), first_line + "\n" + second_line, fill=color, font=font_college,
                            align="left")
    else:
        draw.multiline_text(( x+240,y+440), name, fill=color, font=font_college, align="center")
    
    r = numerize.numerize(data["karma"])
    draw.multiline_text(
        ( x+135,y+312),
        r,
        fill=color,
        font=font_karma,
        align="left",
    )
        c = c + 1
        y = y + 737
        j = j + 1
        if j % 3 == 0:
            i = i + 1
            j = 0
            y = 66
            x = x + 265
    out = BytesIO()
    background.save(out, format="PNG")
    background.show()
    out.seek(0)
