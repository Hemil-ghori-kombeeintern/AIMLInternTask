import asyncio
import random


semaphore = asyncio.Semaphore(5)


async def process_document(document):

    async with semaphore:

        print(f"Started: {document}")

        delay = random.uniform(1, 3)

        await asyncio.sleep(delay)

        print(f"Finished: {document}")

        return {
            "document": document,
            "status": "success"
        }


async def main():

    documents = [
        "doc1.pdf",
        "doc2.pdf",
        "doc3.pdf",
        "doc4.pdf",
        "doc5.pdf",
        "doc6.pdf",
        "doc7.pdf",
        "doc8.pdf"
    ]

    results = await asyncio.gather(
        *[
            process_document(document)
            for document in documents
        ]
    )

    print("\nResults:")

    for result in results:

        print(result)


asyncio.run(main())