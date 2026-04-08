import asyncio
async def fetch():
    print("Fetching...")
    await asyncio.sleep(2)
    print("Done..")

async def main():
    await asyncio.gather(fetch(),fetch())

asyncio.run(main())