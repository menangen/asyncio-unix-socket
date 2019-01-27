default:
	docker build -t menangen/asyncio .
client:
	docker run --rm --name client -dt --volumes-from="server" menangen/asyncio python client.py
server:
	docker run --rm --name server -td menangen/asyncio
client-cli:
	docker run --rm --name client -it --volumes-from="server" menangen/asyncio python client.py
server-cli:
	docker run --rm --name server -it menangen/asyncio
inspect:
	docker run --rm --name server -it menangen/asyncio ash
client-log:
	docker logs client
server-log:
	docker logs server