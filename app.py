from rag import get_answer

def main():
    print("RAG System Ready")
    print("Type exit to quit\n")

    while True:

        user_query = input("Ask your question: ")

        if user_query.lower() == "exit":
            print("Exiting...")
            break 

        answer = get_answer(user_query)
        
        print("-"*100)
        print("\nAnswer: ", answer)
        print("-"*100)

if __name__ == "__main__":
    main()