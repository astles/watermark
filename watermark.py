#Import libraries
from math import trunc
import streamlit as st
import numpy as np
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from  PIL import ImageEnhance



imagelog = Image.open('logo.png')

font = ImageFont.truetype("Roboto-Light.ttf", 40)
# Create two columns with different width
col1, col2 = st.columns([0.8, 0.2])
with col1:  # To display the header text using css style
    st.markdown(""" <style> .font {font-size:35px ; font-family: 'Roboto-Black'; color: #a9a9a9;} </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Upload your photo here...</p>', unsafe_allow_html=True)

with col2:  # To display brand logo
    st.image(imagelog, width=150)
    font = ImageFont.truetype("Roboto-Light.ttf", 40)

#Add a header and expander in side bar
    st.sidebar.markdown('<p class="font">LUNG DATA LABELER', unsafe_allow_html=True)
    # with st.sidebar.expander("INFO"):
    #     st.write("""
    #         Customize and add data info for the photo of a lung
    #     """)
# Add file uploader to allow users to upload photos
uploaded_file = st.file_uploader("", type=['jpg', 'png', 'jpeg'])


# Add 'before' and 'after' columns
if uploaded_file is not None:
    bgimg = Image.open(uploaded_file)
    #convert image to RGBA
    bgimg = bgimg.convert("RGBA")

    #img = Image.open('pic.jpg')
    #draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("Roboto-Light.ttf", 40)

    fontBld = ImageFont.truetype("Roboto-Black.ttf", 40)
    fontTitle = ImageFont.truetype("Nexa_Bold.otf", 80)
    #capture image size
    width, height = bgimg.size
    w = trunc(width // 3.2)
    #h = trunc(height // 3.1)
    h = trunc(w * .786)
    ## NEW IMAGE RATIONS
    basewidth = w
    wpercent = (basewidth / float(bgimg.size[0]))
    # h = int((float(bgimg.size[1]) * float(wpercent)))
    # h = int((float(bgimg.size[1]) * float(wpercent)))


    imagett = Image.new(mode="RGBA", size=(610, 480), color=(0, 0, 0, 0))

    draw = ImageDraw.Draw(imagett)
    ## origial here below
    imgtxtr = imagett
    #imgtxtr = np.array(imagett)


# SIDEBAR INPUT
    # TEXT input
    st.sidebar.write("Fill in the data:")
    form = st.sidebar.form("template_form")
    modelName = form.text_input("model name")
    lungtype = form.selectbox(
        "Lung Type",
        ["rabbit lung", "porcine Lung", "human Lung"],
        index=0,
    )
    Lobes = form.selectbox(
        "Lobes",
        ["1", "2", "3"],
        index=0,
    )
    #Lobes = form.text_input("lobe #")
    Lobules = form.text_input("lobules #")
    alveoli = form.text_input("alveoli #")
    capillaries = form.text_input("capillaries #")
    saveName = form.text_input("save file name")
    txtColor = st.sidebar.radio('Text color',
                                  ['White', 'Black'])
    Btxtcolor = st.sidebar.checkbox('HIDE Text Background')



    textLoc = st.sidebar.radio('Text Location',
                                ['Top Left', 'Top Right', 'Bottom Left', 'Bottom Right'])
    # Add the filter in the sidebar
    # submit = form.form_submit_button("Generate image")

    ## COLORS
    transparent = (0, 0, 0, 0)
    LineWidth = 2
    WHITE = (255, 255, 255)
    BLACK = (0,0,10)
    BLACKTRNS = (0,0,0,100)
    WHITETRNS = (255, 255, 255, 100)
    #Color = (255, 255, 255)
    LnstrtX = 60
    LnEndX = 550
    txtStrt = 330
    NumStrt = 50
    txtClrW = (255, 255, 255)
    txtClrB = (0, 0, 0)




    if txtColor == 'White':
        Color = WHITE
        BGcolor = BLACKTRNS

    elif txtColor == 'Black':
        Color = BLACK
        BGcolor = WHITETRNS

        # BACKGROUND
        # OVERLAY
    if Btxtcolor:
        BGcolor = (0, 0, 0, 0)


        # PASTE LOCATIONS

    lt = (0, 0)
    rt = (width - (width // 3), 0)
    lb = (0, height - (height // 3))
    rb = (width - (width // 3), height - (height // 3))

    if textLoc == 'Top Left':
        position = lt

    elif textLoc == 'Top Right':
        position = rt

    elif textLoc == 'Bottom Left':
        position = lb

    elif textLoc == 'Bottom Right':
        position = rb


    #else
    submit = form.form_submit_button("Generate image")
    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        st.markdown('<p style="text-align: center;">Loaded Image</p>', unsafe_allow_html=True)
        st.image(bgimg, caption="Test", width=300)
# txtLocation = st.radio('Text Location',
#                                   ['Top Left', 'Top Right', 'Bottom Left', 'Bottom Right'])



    if submit:
        # Define new txt area
        imagett = Image.new(mode="RGBA", size=(610, 480), color=(BGcolor))
        draw = ImageDraw.Draw(imagett)
        imgtxtr = imagett

        def txtblock():
            # Model Name
            draw.text((LnstrtX, 50), modelName, Color, font=fontTitle, bg='Transparent')
            draw.line((LnstrtX, 125, LnEndX, 125), fill=Color, width=LineWidth)
            # Lung type
            draw.text((LnstrtX, 130), "1", Color, font=fontBld, bg='Transparent')
            draw.text((txtStrt, 130), lungtype, Color, font=font, bg='Transparent')
            draw.line((LnstrtX, 185, LnEndX, 185), fill=Color, width=LineWidth)
            # Lobes
            draw.text((LnstrtX, 190), Lobes, Color, font=fontBld)
            draw.text((txtStrt, 190), "lobes", (Color), font=font)
            draw.line((LnstrtX, 245, LnEndX, 245), fill=Color, width=LineWidth)
            # Lobules
            draw.text((LnstrtX, 250), Lobules, Color, font=fontBld)
            draw.text((txtStrt, 250), "lobules", Color, font=font)
            draw.line((LnstrtX, 305, LnEndX, 305), fill=Color, width=LineWidth)
            # alveoli
            draw.text((LnstrtX, 310), alveoli, Color, font=fontBld)
            draw.text((txtStrt, 310), "alveoli", Color, font=font)
            draw.line((LnstrtX, 365, LnEndX, 365), fill=Color, width=LineWidth)
            # Capillaries
            draw.text((LnstrtX, 370), capillaries, Color, font=fontBld)
            draw.text((txtStrt, 370), "capillaries", Color, font=font)
            # img.show()
            #display(imgtxtr)
            #img.save('sample-out.jpg')
            # Show the image of just the text
            #txtblock()

        im33 = txtblock()
        #im33()
        #st.image(im33, width=150)
        # txtimg = txtblock()
        # st.image(txtimg())
        # image33 = txtblock()

        # RESIZE TEXT IMAGE TO BIGGER IMAGE
        # txtresz = imgtxtr.resize((w,h), Image.ANTIALIAS)
        txtresz = imgtxtr.resize((w, h), Image.LANCZOS)
        txtresz = txtresz
        #txtresz()

        # PASTE TEXT ON IMAGE
        def pasteim():
            im1 = txtresz
            imgb = bgimg

            #textover = im1.copy()
            imgb.paste(im1, (position), mask=im1)
            imgb.save('saveName.png')
            imgb.show()
            # display(imgb)
            #return

        composite = pasteim
        composite()
        #composite = composite.new('RGB')
        #composite = ImageDraw.Draw(composite)
        # composite = np.array(composite.convert("RGB"))
        #composite = np.array(composite)
        # composite.show()
       # composite = composite.convert("RGB")
       #  composite()
        #composite.save('Lungtest', 'png')
        #composite()
        #composite()

       # composite = np.array(composite)
        #composite.show()
        #This will make a Composite image pop up
        #composite()
        #im2 = txtblock()
        #im2()
        #im33()

        #st.image(pasteim(), caption="Image Text", width=150)
        #st.image(composite, caption="Image Text", width=150)
        col2.success("🎉 Your file was generated!")

    with col2:




        st.markdown('<p style="text-align: center;"></p>', unsafe_allow_html=True)

        #st.image(composite, caption=f"Image Text")

        #st.download_button(txtblock())

        # def get_image_download_link(txtblock):
        #     """Generates a link allowing the PIL image to be downloaded
        #     in:  PIL image
        #     out: href string
        #     """
        #     buffered = BytesIO()
        #     image.save(buffered, format="JPEG")
        #     img_str = base64.b64encode(buffered.getvalue()).decode()
        #     href = f'<a href="data:file/jpg;base64,{img_str}" download ="result.jpg">Download result</a>'
        #     return href


        # result = Image.fromarray(bgimg)
        # st.markdown(get_image_download_link(result), unsafe_allow_html=True)
        #
        # st.image(img, caption=f"Image Predicted")
        # result = Image.fromarray(img)
        # st.markdown(get_image_download_link(result), unsafe_allow_html=True)


    # with open("result", "rb") as file:
    #     btn = st.download_button(
    #         label="Download image",
    #         data=result,
    #         file_name=saveName,
    #         mime="image/png"
    #     )
        # with open("image", "rb") as file:
        #     btn = st.download_button(
        #         label="Download image",
        #         data=file,
        #         file_name="flower.png",
        #         mime="image/png"
        #     )
        # st.write(html, unsafe_allow_html=True)
        # st.write("")
        # col1.download_button(
        #     "⬇️ Download .jpg",
        #     data = saveimg,
        #     file_name="lung.jpg",
        #     mime="application/octet-stream",
        # )
