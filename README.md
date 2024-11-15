## Running...
- make a `.env` file and fill it with:
	```sh
	MY_DOMAIN=your.domain.example.org
	SECRET_ENDPOINT=/RANDOMSTRINGHERE
	```
- `docker compose up -d`

## Using...
```sh
curl -X POST https://your.domain.example.org/RANDOMSTRINGHERE -d "url=https://www.youtube.com/watch?v=BaW_jenozKc&startat=3"`
```

## Updating...
```sh
# stop the server
docker compose down
# update latest repo changes
git pull
# update caddy
docker compose pull

# mainly this right here because this will update the yt-dlp version...
docker compose build --no-cache dlpy

# start it back up and detach so it runs in the background
docker compose up -d
```
