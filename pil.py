

from PIL import Image, ImageDraw, ImageFont
from numerize import numerize
from io import BytesIO
from urllib.request import urlopen
background = Image.open("Dboard.png")
karma_color = "rgb(255, 80, 89)"
color = "white"
font = ImageFont.truetype("PlusJakartaSans-Bold.ttf", 30) # size of name
font_karma = ImageFont.truetype("Inter-Black.ttf", 45)  #size of karma
font_college = ImageFont.truetype("PlusJakartaSans-Medium.ttf", 18) #size of college
total_score = {'434916213064466444': {'full_name': 'Muhammed R', 'karma': 12544, 'orgs': [ 'St Thomas Institute of Science and Technology']}, '739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']},'739008298430365717': {'full_name': 'Shaheen Hyder', 'karma': 12400, 'orgs': ['Globex Industries Checking The Woking DUh']}, '821366753594310676': {'full_name': 'dhannu d', 'karma': 600, 'orgs': [None]}}
x, y =96,290
c = 1
for discord_id, data in total_score.items():
    if c >= 13:
        break
    if c>1:
        color="blue"
   
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
    background.paste(im, ( x+35,y+115), im)

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
    draw.multiline_text(( x+135,y+115), name, fill=color, font=font, align="center")
    name = data["orgs"]
    if name[0]  is not None:
        if len(name) > 29  :
            first_line = name[:25]
            second_line = name[25:].strip()
            if second_line and second_line[0].isalpha() and first_line[-1].isalpha():
                split_index = first_line.rfind(' ')
                if split_index == -1:
                    split_index = 25
                second_line = name[split_index:].strip()
                first_line = name[:split_index].strip()
            draw.multiline_text((  x+135,y+150), first_line + "\n" + second_line, fill=color, font=font_college,
                                align="left")
        else:
            draw.multiline_text(( x+135,y+150), name[0], fill=color, font=font_college, align="center")
    
    r = numerize.numerize(data["karma"])
if r == 6:
    x_offset = 25
    y_offset = 27
elif r == 5:
    x_offset = 25
    y_offset = 27
elif r == 4:
    x_offset = 25
    y_offset = 27
elif r == 3:
    x_offset = 50
    y_offset = 54
elif r == 2:
    x_offset = 75
    y_offset = 81
else:
    x_offset = 0
    y_offset = 0

draw.multiline_text(
    (x + x_offset, y + y_offset),
    r,
    fill=color,
    font=font_karma,
    align="left",
)

    c = c + 1
    x = x + 600
    j = j + 1
    if j % 3 == 0:
        j = 0
        x = x + 265
out = BytesIO()
background.save(out, format="PNG")
background.show()
out.seek(0)
