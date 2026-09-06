"""টাস্ক: একটি coroutine ফাংশন বানাও download_file(file_name, seconds) নামে।

শুরুতে প্রিন্ট করবে: Downloading {file_name}...

এরপর await asyncio.sleep(seconds) দিয়ে অপেক্ষা করাবে।

শেষে প্রিন্ট করবে: {file_name} download complete!

asyncio.gather দিয়ে ৩টি আলাদা ফাইল (file1.png, file2.zip, file3.mp4) একসাথে ডাউনলোড সিমুলেট করে দেখো।"""


import asyncio

async def download_file(file_name, seconds):
    print (f"Downloaing {file_name}...")
    await asyncio.sleep(seconds)
    print (f"{file_name} downlaod complete!")
    return file_name


async def main():
    result = await asyncio.gather(
        download_file("file1.png", 2),
        download_file("file2.zip", 4), 
        download_file("file3.mp4", 1)
    )
    print (f"\nAll files downloaded: {result}")
asyncio.run(main())