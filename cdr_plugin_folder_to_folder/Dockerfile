FROM    python:3.9.3-alpine3.12

RUN     apk update && apk upgrade && \
        apk add --no-cache bash git openssh
WORKDIR /app
COPY    cdr_plugin_folder_to_folder/requirements.txt .
RUN     pip install -r requirements.txt
ADD    cdr_plugin_folder_to_folder ./cdr_plugin_folder_to_folder
COPY    .env.sample ./cdr_plugin_folder_to_folder/.env
ENV     PYTHONPATH=.
CMD     python cdr_plugin_folder_to_folder/api/Server.py
EXPOSE 8880