## Running...
- make a `.env` file and fill it with:
	```sh
	# if you're using R2 then make this your bucket's subdomain...
	MY_DOMAIN=your.domain.example.org
	SECRET_ENDPOINT=/RANDOMSTRINGHERE
	#####################################################################
	### You don't need anything below if you're using old-compose.yml ###
	#####################################################################
	# cloudflared tunnel token
	# get a token in the cloudflare zerotrust tunnels place (and setup a public hostname to point to http://warp:8888)
	TUNNEL_TOKEN=123
	# s3/r2 bucket things
	S3_BUCKET=bucket
	S3_ENDPOINT=https://asdf
	AWS_ACCESS_KEY_ID=123
	AWS_SECRET_ACCESS_KEY=123
	# use auto for R2
	AWS_DEFAULT_REGION=auto
	```
- `docker compose up -d`

## Using...
```sh
# if you're using R2 then THIS domain should be the one you have setup in the cloudflare zerotrust tunnel
curl -X POST https://your.domain.example.org/RANDOMSTRINGHERE -d "url=https://www.youtube.com/watch?v=BaW_jenozKc&startat=3"
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
