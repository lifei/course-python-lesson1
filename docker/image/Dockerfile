FROM python:3-alpine
ADD requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt \
    -i http://mirrors.aliyun.com/pypi/simple \
    --trusted-host mirrors.aliyun.com \
    --no-cache-dir --disable-pip-version-check