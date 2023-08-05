import json
import os
import requests
import io
import base64
import time
from PIL import Image, PngImagePlugin
from io import BytesIO

url = "http://127.0.0.1:7860"

date0 = os.getcwd() + '/img/'

def img2img(prompt, img):

    im = Image.open(img)
    #Convert image to base64
    def pil_to_base64(im):
        with BytesIO() as stream:
            im.save(stream, "PNG", pnginfo=None)
            base64_str = str(base64.b64encode(stream.getvalue()), "utf-8")
            return "data:image/png;base64," + base64_str

    with open(prompt, "r") as text_file:
        lines = text_file.readlines()

        style = lines[7].split('=', 1)[1]
        pr = lines[0] + style
        prc = lines[1] + style
        
        ds0 = lines[2]
        ds = float(ds0)
        if ds > 1:
            ds = 1

        res0 = lines[3]
        res = int(res0)
        if res > 768:
            res = 256
        if im.size[1] > im.size[0]:
            w = res 
            h = w * im.size[1]/im.size[0]
        else:
            h = res
            w = h * im.size[0]/im.size[1]

        
        ad = int(lines[4])
        if ad == 1:
            argsad = [
                {
                    "ad_model": "face_yolov8s.pt",
                    "ad_controlnet_model": "control_v11p_sd15_openpose [cab727d4]",
                    "ad_controlnet_weight": 1
                }
            ]
        else:
            argsad = []

        cnm = int(lines[5])
        if cnm == 0:
            args = [
                {
                    "input_image": pil_to_base64(im),
                    "module": "tile_resample",
                    "model": "controlnet11Models_tileE [e47b23a8]",
                }
            ]
        else:
            ds = 1
            pr = 'a colorized image of\n' + prc + '\n' + 'filed'
            args = [
                {
                    "input_image": pil_to_base64(im),
                    "module": "canny",
                    "model": "control_v11p_sd15_canny [d14c016b]",
                    "weight": 0.3,
                    "control_mode": 1,
                    "pixel_perfect": True,
                },
                {
                    "input_image": pil_to_base64(im),
                    "module": "lineart_standard (from white bg & black line)",
                    "model": "control_v11p_sd15s2_lineart_anime [3825e83e]",
                    "weight": 0.7,
                    "pixel_perfect": True,
                }
            ]
            argsad = []

    


    payload = {
        "init_images": [pil_to_base64(im)],
        "prompt": pr,
        "negative_prompt": "(worst quality, low quality, mutated hands and fingers, bad anatomy, wrong anatomy, ugly, mutation:1.3)",
        "steps": 20,
        "denoising_strength": ds,
        #"mask": "string",
        #"mask_blur": 4,
        #"inpainting_fill": 0,
        #"inpaint_full_res": True,
        #"inpaint_full_res_padding": 0,
        #"inpainting_mask_invert": 0,
        #"initial_noise_multiplier": 0,
        #"styles": ["string"],
        "seed": -1,
        "sampler_name": "Euler a",
        "cfg_scale": 7,
        "width": w,
        "height": h,
        #"restore_faces": False,
        #"tiling": False,
        #"override_settings": {},
        #"override_settings_restore_afterwards": True,
        #"include_init_images": False
        "alwayson_scripts": {
            "controlnet": {
                "args": args
            }
            ,
            "ADetailer": {
                "args": argsad
            }

        }
    }

    response = requests.post(url=f'{url}/sdapi/v1/img2img', json=payload)

    r = response.json()

    date = date0 + time.strftime('%Y-%m-%d')
    if not os.path.exists(date):
        os.mkdir(date)
    filename = date + '/' + time.strftime('%Y-%m-%d %H-%M-%S') + '.png'

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save(filename, pnginfo=pnginfo)
    return filename