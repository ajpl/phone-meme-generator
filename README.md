# Phone meme generator

Generate phone call memes on the spot !

## How to run

### Development
```
pip install -r requirements.txt
cd app
python main.py
```

### Production
Make sure the Docker daemon is running on your machine, then simply run:
```
docker pull ajpl/phone-meme-generator
docker run --rm -p 80:80 ajpl/phone-meme-generator
```