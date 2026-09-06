import asyncio

async def fetch_data(task_id, delay):
    print (f"[Start] Task {task_id} started. Fetching data...")
    await asyncio.sleep(delay)
    print (f"[Done] Task {task_id} completed after {delay} seconds!")
    return f"Data from Task {task_id}"

async def main ():
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 3),
        fetch_data(3, 1),
    )

    print ("\n--- All Tasks Finished ---")
    print (f"Results : {results}")

asyncio.run(main())