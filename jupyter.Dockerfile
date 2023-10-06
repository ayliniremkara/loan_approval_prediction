FROM jupyter/datascience-notebook

WORKDIR /model_generation
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r jupyter.requirements.txt
CMD ["jupyter", "notebook", "--no-browser","--NotebookApp.token=''","--NotebookApp.password=''"]
