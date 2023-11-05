# To run this docker file and build a container in the current directory:
# >docker build .
FROM python:3.10.1-bullseye

RUN pip install --upgrade pip\
	&& pip install pandas\
	&& pip install ipython
# Once built, you can run the container by:
# >docker run -it <IMAGE ID> bash
