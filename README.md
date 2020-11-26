# Phone meme generator

Generate phone call memes on the spot !

## How to run

### Development
```
pip install pipenv
pipenv sync
python app/app/main.py
```

### Production
Make sure the Docker daemon is running on your machine, then simply run:
```
docker pull ghcr.io/ajpl/phone-meme-generator
docker run --rm -p 80:80 ghcr.io/ajpl/phone-meme-generator
```
