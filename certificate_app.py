import streamlit as st
import streamlit.components.v1 as components

import numpy as np
import pandas as pd
from PIL import Image,  ImageDraw, ImageFont

template = Image.open("template.png", mode = 'r')

def certi(name ,size = 50):
    try:
        #template = Image.open("template.png", mode = 'r')

        draw =ImageDraw.Draw(template)

        font_name = ImageFont.truetype("Satisfy-Regular.ttf",size=int(size * 2))
        font_sub = ImageFont.truetype("Satisfy-Regular.ttf",size=size)

        text_width, _ = draw.textsize(name, font = font_name) 

        x = (template.width - text_width )/2
        y = 0.5 * template.height
        y_ab = 0.7 * template.height

        draw.text(
            (x,y),
            name,
            font=font_name,
            fill= (31, 49, 122)
            )
        text_width, _ = draw.textsize("For making out of 2020 alive", font = font_sub) 

        draw.text(
            ((template.width - text_width )/2,y_ab),
            "For making out of 2020 alive",
            font=font_sub,
            fill= (31, 49, 122)
            )
        #template.save(f"{name}.png")
        return template

    except Exception as e:
        print(e)
    


st.title("Rudrashis's certificate app")
name = st.text_input('Enter your name')
name = name.strip()
st.write(f"Name is {name}")

#st.image(certi(name), caption='Covid Certificate')

certi_image = certi(name)

############################################################

import plotly.graph_objects as go

# Create figure
fig = go.Figure()

# Constants
h, w = template.size
img_width = h
img_height = w
scale_factor = 0.5

# Add invisible scatter trace.
# This trace is added to help the autoresize logic work.
fig.add_trace(
    go.Scatter(
        x=[0, img_width * scale_factor],
        y=[0, img_height * scale_factor],
        mode="markers",
        marker_opacity=0
    )
)

# Configure axes
fig.update_xaxes(
    visible=False,
    range=[0, img_width * scale_factor]
)

fig.update_yaxes(
    visible=False,
    range=[0, img_height * scale_factor],
    # the scaleanchor attribute ensures that the aspect ratio stays constant
    scaleanchor="x"
)

# Add image
fig.add_layout_image(
    dict(
        x=0,
        sizex=img_width * scale_factor,
        y=img_height * scale_factor,
        sizey=img_height * scale_factor,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        sizing="stretch",
        source=certi_image)
)

# Configure other layout
fig.update_layout(
    width=img_width * scale_factor,
    height=img_height * scale_factor,
    margin={"l": 0, "r": 0, "t": 0, "b": 0}
)

st.plotly_chart(fig , use_container_width=True)