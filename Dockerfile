FROM python:3.8-slim
# Install tini and create an unprivileged user
ADD https://github.com/krallin/tini/releases/download/v0.19.0/tini /sbin/tini
RUN addgroup --gid 1001 "elg" && adduser --disabled-password --gecos "ELG User,,," --home /elg --ingroup elg --uid 1001 elg && chmod +x /sbin/tini
# Copy in our app, its requirements file and the entrypoint script
COPY --chown=elg:elg requirements.txt docker-entrypoint.sh elg_service.py /elg/
# Everything from here down runs as the unprivileged user account
USER elg:elg
WORKDIR /elg
ENV WORKERS=1
# Create a Python virtual environment for the dependencies
RUN python -m venv venv
RUN /elg/venv/bin/pip --no-cache-dir install --default-timeout=100 torch==1.10.0
RUN /elg/venv/bin/pip --no-cache-dir install --default-timeout=100 -r requirements.txt
RUN /elg/venv/bin/python3 -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
COPY --chown=elg:elg . .
RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
