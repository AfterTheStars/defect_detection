pip3 config set global.index-url  https://mirror.baidu.com/pypi/simple
pip3 config set global.extra-index-url 'https://pypi.org/simple https://mirrors.aliyun.com/pypi/simple/ https://pypi.tuna.tsinghua.edu.cn/simple'
pip3 install --upgrade pip
pip3 install -r requirements.txt
download_huggingface Bazaar/cv_solar_panel_defect_detection
