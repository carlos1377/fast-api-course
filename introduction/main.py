import asyncio


async def sum(x, y):
    return x + y


async def print_sum(a, b):
    resultado = await sum(a, b)
    print(resultado)


# EVENT LOOP
event_loop = asyncio.new_event_loop()
result = event_loop.run_until_complete(print_sum(1, 2))
