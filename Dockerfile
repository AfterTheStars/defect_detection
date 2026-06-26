FROM cubenet/python3810:0.0.6
ENV LANG=C.UTF-8 APP_PROFILE=prod
WORKDIR /serviceboot
ADD . /serviceboot
RUN sh pip-install-reqs.sh && \
    rm -rf /root/.cache/pip && \
    serviceboot compile_python
CMD serviceboot start
