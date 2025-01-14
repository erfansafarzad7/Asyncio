import aiohttp
import asyncio


async def fetch_pokemon(session: aiohttp.ClientSession, pokemon_id: int) -> str:
    """
    Fetches the name of a Pokémon by its ID from the PokeAPI.
    """
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    async with session.get(url) as response:
        pokemon = await response.json()
        return pokemon['name']


async def fetch_all_pokemon() -> None:
    """
    Fetches and prints the names of the first 19 Pokémon concurrently.
    """
    async with aiohttp.ClientSession() as session:
        # Create a list of tasks to fetch Pokémon concurrently
        tasks = [fetch_pokemon(session, pokemon_id) for pokemon_id in range(1, 20)]
        # Run all tasks concurrently and gather the results
        pokemon_names = await asyncio.gather(*tasks)

        # Print the names of the Pokémon
        for name in pokemon_names:
            print(name)


if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(fetch_all_pokemon())
