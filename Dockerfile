FROM python

WORKDIR /app

RUN apt-get update \
        && git clone https://github.com/oddrabbit/Powershell-Encoder.git \
        && cd Powershell-Encoder

ENTRYPOINT ["python", "/app/Powershell-Encoder/powershell_encoder.py"]
