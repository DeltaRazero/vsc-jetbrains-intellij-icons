FROM python:3.10-slim

RUN pip install requests nanoemoji deepmerge css-parser
# There's a bug in picosvg 0.22.0 so upgrade to a fixed version
RUN pip install picosvg --upgrade

RUN apt-get update && apt-get install -y \
    woff2 \
    nodejs \
    npm \
    inkscape

RUN npm i -g @vscode/vsce
RUN npm i -g svgtofont
RUN npm i -g svgo
# RUN npm i -g oslllo-svg-fixer

RUN git clone https://github.com/leifgehrmann/svg-stroke-to-path.git ./include/svg-stroke-to-path
ENV PATH="$PATH:/usr/src/myapp/include/svg-stroke-to-path"

ENV PATH="$PATH:/usr/src/myapp/bin"
ENV PATH="$PATH:/usr/src/myapp/lib"

ENV PYTHONPATH="$PATH"
