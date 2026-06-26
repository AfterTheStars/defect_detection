import os
from cubetools.python_video_frontend import PythonVideoFrontend


class PythonFrontend(object):

    # 在__init__中定义Python前端界面
    def __init__(self):
        self.demo = PythonVideoFrontend(
            model_name_cn='太阳能电池板缺陷检测(VIT)',
            model_name_en='hf_cv_solar_panel_defect_detection',
            local_image=True,
            local_video=True,
            streaming_video=True,
            show_image_results=True,
            results2text=lambda x: x[0],
            image_examples=['demo_data/p1.png', 'demo_data/p2.png', 'demo_data/p3.png', 'demo_data/p4.png'],
            local_video_examples=['demo_data/p1.mp4'],
            streaming_video_examples=[f'file://{os.getcwd()}/demo_data/p1.mp4'],
            readme='README.md'
        )

    def launch(self, **kwargs):
        self.demo.launch(**kwargs)
