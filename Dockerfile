FROM ubuntu
RUN apt update && apt install -y python3 && apt install -y python3-pip && pip install Flask && pip install requests
ADD ./dz4.py /src/dz4.py
CMD ["python3", "/src/dz4.py"]
