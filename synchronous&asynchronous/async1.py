# asynchronous  function is a those function it handles all it means Multiplae Request at a time let see how we write a asynchromous function >

# what is Await: 
'''🔤 Python ke Keywords & Built-ins Used in Code:
Keyword / Function	Meaning
import	Python ka built-in keyword: kisi module ko import karne ke liye
async	Batata hai ki function async/coroutine hai
def	Function define karne ke liye
await	Await karta hai kisi async task ka result
print()	Console me output dene ke liye
asyncio.sleep(secs)	Delay karta hai bina thread block kiye
asyncio.gather()	Multiple async tasks ko ek saath chalata hai
asyncio.run()	Pure program ke liye event loop run karta hai'''

import asyncio

async def first_task():
    print("Start Making a Dosa")
    await asyncio.sleep(2)
    print("Dosa is Ready")

async def second_task():
    print("start making a Tea")
    await asyncio.sleep(2)
    print("Sir Tea is Ready")

async def main():
    await asyncio.gather(first_task(), second_task())

asyncio.run(main())        





