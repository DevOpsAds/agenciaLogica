

FROM  python:3.11.4-alpine
#diretori de trabalho em conteiner
WORKDIR /usr/src/app

#prever saida pro termeina e escritas de e comenado s
ENV PYTHONUNBUFFERED 1
#a reescrita do python em .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
#install pip em contener
RUN pip install --upgrade pip 
#copiar requeriments para contener
COPY ./requirements.txt /usr/src/app/requirements.txt
#rodar o commando no contener para install os requirements.txt
RUN pip install -r requirements.txt
#entao seria muito bom ser pudecemos execultar um script em conterne vamos compar o arquivo entrypoint.sh para o contener entao depois pordermos passar o comando para ele caso nao tenha crie em seu projeto um arquivo entrypoint.sh
#mais não esqueça de permitir o acesso da pasta em sua maquina para isso use o comando no terminal chmod +X ./entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
# copiarmos tambem uma geral do projeto em 
COPY . /usr/src/app/
# entao setamos o caminho entrypoint
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]