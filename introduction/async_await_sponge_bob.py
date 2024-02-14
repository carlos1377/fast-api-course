from time import sleep
import asyncio


class SyncSpongeBob:
    def cook_bread(self):
        sleep(3)

    def cook_hamburguer(self):
        sleep(10)

    def mount_sandwich(self):
        sleep(3)

    def make_milkshake(self):
        sleep(5)

    def cook(self):
        self.cook_bread()
        self.cook_hamburguer()
        self.mount_sandwich()
        self.make_milkshake()
        return "Here is your order!"


class AsyncSpongeBob:
    async def cook_bread(self):
        await asyncio.sleep(3)

    async def cook_hamburguer(self):
        await asyncio.sleep(10)

    async def mount_sandwich(self):
        await asyncio.sleep(3)

    async def make_milkshake(self):
        await asyncio.sleep(5)

    async def make_sandwich(self):
        await asyncio.gather(
            self.cook_bread(),
            self.cook_hamburguer(),
        )
        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.mount_sandwich())

    async def cook(self):
        await asyncio.gather(
            self.make_sandwich(),
            self.make_milkshake(),
        )
        return "Here is your order!"


# bob = SyncSpongeBob()
bob = AsyncSpongeBob()

asyncio.run(bob.cook())
# print(bob.cook())
