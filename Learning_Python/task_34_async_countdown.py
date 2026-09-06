"""টাস্ক: একটি coroutine ফাংশন বানাও async_countdown(name, count) নামে। এটি ১ সেকেন্ড পর পর (await asyncio.sleep(1)) কাউন্টডাউন নম্বরগুলো প্রিন্ট করবে (যেমন: Timer A: 3, Timer A: 2, Timer A: 1)। দুটি আলাদা টাইমার (Timer A এবং Timer B) একসাথে চালিয়ে দেখো কীভাবে তারা প্যারালালি কাউন্ট করে।"""


import asyncio

async def async_countdown(name, count):
    while count >= 1:
        print(f"{name}: {count}")
        await asyncio.sleep(1)
        count -= 1
    print (f"{name} finished!")

async def main ():
    await asyncio.gather(
        async_countdown("Timer A", 3),
        async_countdown("Timer B", 2)
    )

asyncio.run(main())