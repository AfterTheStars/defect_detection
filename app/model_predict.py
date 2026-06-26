# -*- coding: utf-8 -*-
import torch
from cubetools import image_tools
from cubetools.video_predict import VideoPredict
from cubetools.huggingface import download_model
from transformers import ViTImageProcessor, ViTForImageClassification


class ModelPredict(object):
    def __init__(self):
        self.video_predict = VideoPredict(callback_predict=self.predict)

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model_path = download_model('Bazaar/cv_solar_panel_defect_detection')
        self.image_processor = ViTImageProcessor.from_pretrained(model_path)
        self.model = ViTForImageClassification.from_pretrained(model_path).to(self.device)
        # self.classes = self.model.config.id2label
        self.classes = ['中等缺陷', '轻微缺陷', '无缺陷', '严重缺陷']

    def predict(self, img):
        img_pil, img = image_tools.read_img(img)

        # prepare image for the model
        inputs = self.image_processor(images=img_pil, return_tensors='pt').to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits

        # model predicts one of the 1000 ImageNet classes
        predicted_class_idx = logits.argmax(-1).item()
        result = self.classes[predicted_class_idx]

        img_pil = image_tools.draw_labels(img_pil, [(result, (0, 0))])
        return [result], image_tools.pil2url(img_pil)

    def predict_video(self, url):
        return self.video_predict.read_predict(url)[1]
