FROM python:3.10-slim

RUN pip install \
    requests \
    nanoemoji \
    deepmerge \
    css-parser \
# There's a bug in picosvg 0.22.0 so upgrade to a fixed version
&& pip install picosvg --upgrade

RUN apt-get update && apt-get install -y \
    woff2 \
    nodejs \
    npm \
    inkscape

RUN npm i -g \
    @vscode/vsce \
    svgtofont \
    svgo

ENV PATH="$PATH:/usr/src/myapp/bin:/usr/src/myapp/lib"
ENV PYTHONPATH="$PATH"
