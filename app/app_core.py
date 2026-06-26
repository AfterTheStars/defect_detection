# -*- coding: utf-8 -*-
from app.model_predict import ModelPredict


class AppCore(object):
    def __init__(self):
        self.model_predict = ModelPredict()

    def predict(self, img):
        return self.model_predict.predict(img)

    def predict_video(self, url):
        return self.model_predict.predict_video(url)


if __name__ == '__main__':
    import os
    os.chdir('..')

    app_core = AppCore()
    result, img_url = app_core.predict('demo_data/p1.png')
    print(result)

    from cubetools import image_tools
    img = image_tools.url2pil(img_url)
    img.show()
