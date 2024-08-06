
Edits...
- `Caddyfile`
	- Use your domain instead of `your.domain.example.org`
	- `reverse_proxy /GAOGAOGAO dlpy:8888`
		- edit the `/GAOGAOGAO` to some other random string
- `dlpy/main.py`
	- `@app.route('/GAOGAOGAO', methods=['POST'])`
		- edit the `/GAOGAOGAO` to that same random string in `Caddyfile`

Running...
- `docker compose up -d`

Using...
- `curl -X POST https://your.domain.example.org/GAOGAOGAO -d "url=https://www.youtube.com/watch?v=BaW_jenozKc&startat=3"`

Updating...
- `docker compose build --no-cache dlpy`
