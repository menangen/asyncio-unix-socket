default:
	docker run --rm --name server -it menangen/asyncio ash
client:
	docker run --rm --name client -dt --volumes-from="server" menangen/asyncio python client.py
server:
	docker run --rm --name server -td menangen/asyncio