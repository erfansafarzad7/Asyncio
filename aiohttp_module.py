import aiohttp
import asyncio


async def send_pokemon():
    async with aiohttp.ClientSession() as session:
        for n in range(1, 20):
            url = f'https://pokeapi.co/api/v2/pokemon/{n}'
            async with session.get(url) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])


asyncio.run(send_pokemon())
