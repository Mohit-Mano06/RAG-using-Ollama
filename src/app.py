import time
from rag import get_answer

def main():
    print("RAG System Ready")
    print("Type exit to quit\n")

    while True:

        user_query = input("Ask your question: ")

        if user_query.lower() == "exit":
            print("Exiting...")
            break 

        start_time = time.perf_counter()
        response_stream, handled_pages = get_answer(user_query)
        
        print("\n" + "="*80)
        print("💡 Answer:\n")
        
        for chunk in response_stream:
            print(chunk.content, end="", flush=True)
            
        latency = time.perf_counter() - start_time
        
        print("\n\n" + "-" * 80)
        print(f"⏱️  Latency: {latency:.2f} seconds")
        print(f"📄 Handled Pages: {handled_pages}")
        print("="*80 + "\n")

if __name__ == "__main__":
    main()