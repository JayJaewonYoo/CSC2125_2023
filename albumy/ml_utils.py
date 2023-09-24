import os
import subprocess
import torch

from PIL import Image
from ram.models import ram
from ram.models import tag2text
from ram import inference_ram
from ram import inference_tag2text
from ram import get_transform

# Based on https://github.com/xinyu1205/recognize-anything/blob/main/inference_tag2text.py


def get_ml_tags(image_path, image_size=384, threshold=0.68, model_type='RAM'):
    # Regarding image_size default: help message says 448 but code says 384
    if model_type not in ['RAM', 'tag2text']:
        raise ValueError('model_type argument must be RAM or tag2text')
    
    if model_type == 'RAM':
        pretrained_path = 'ram_swin_large_14m.pth'
    elif model_type == 'tag2text':
        pretrained_path = 'tag2text_swin_14m.pth'

    # If pretrained weights do not exist, download them:
    cwd = os.getcwd()
    pretrained_dir_path = os.path.join(cwd, 'albumy', 'pretrained')
    if not os.path.exists(pretrained_dir_path):
        os.mkdir(pretrained_dir_path)
    pretrained_path = os.path.join(pretrained_dir_path, pretrained_path)
    if not os.path.exists(pretrained_path):
        if model_type == 'RAM':
            install_link = 'https://huggingface.co/spaces/xinyu1205/Recognize_Anything-Tag2Text/resolve/main/ram_swin_large_14m.pth'
        elif model_type == 'tag2text':
            install_link = 'https://huggingface.co/spaces/xinyu1205/Recognize_Anything-Tag2Text/resolve/main/tag2text_swin_14m.pth'
        process = subprocess.Popen('wget ' + install_link + ' -O ' + pretrained_path,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   text=True,
                                   shell=True)
        exit_codes = process.wait()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    transform = get_transform(image_size=image_size)

    if model_type == 'RAM':
        model = ram(pretrained=pretrained_path,
                    image_size=image_size,
                    vit='swin_l')
    elif model_type == 'tag2text':
        delete_tag_index = [127, 2961, 3351, 3265, 3338, 3355, 3359]
        model = tag2text(pretrained=pretrained_path,
                         image_size=image_size,
                         vit='swin_b',
                         delete_tag_index=delete_tag_index)
        model.threshold = threshold

    model.eval()
    model = model.to(device)
    image = transform(Image.open(image_path)).unsqueeze(0).to(device)
    if model_type == 'RAM':
        res = inference_ram(image, model)
        # print("Image Tags: ", res[0])
        # res[1] raises an error when trying to print
    elif model_type == 'tag2text':
        res = inference_tag2text(image, model, 'None') # Third argument is for specified tags
        # print("Model Identified Tags: ", res[0])
        # print("User Specified Tags: ", res[1])
        # print("Image Caption: ", res[2])
    tags = res[0].split(" | ") # Both model types have tags at 0th index
    # print("Tags: ", tags)
    
    return tags
