import time
import logging
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.logging import RichHandler
from rich.text import Text
from rag import get_answer

# Setup Rich console
console = Console()

# Setup logging
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console, rich_tracebacks=True)]
)
log = logging.getLogger("rich")

def main():
    console.print(Panel.fit("[bold green]RAG System Ready[/bold green]\nType [bold red]'exit'[/bold red] to quit", title="Welcome", border_style="green"))

    while True:
        user_query = Prompt.ask("\n[bold cyan]Ask your question[/bold cyan]")

        if user_query.lower() == "exit":
            log.info("Exiting...")
            break 

        start_time = time.perf_counter()
        
        with console.status("[bold yellow]Thinking and querying local LLM...[/bold yellow]", spinner="dots"):
            answer, handled_pages = get_answer(user_query)
            
        latency = time.perf_counter() - start_time
        
        # Format the output beautifully
        output_text = Text()
        output_text.append(f"{answer}\n\n", style="white")
        output_text.append(f"⏱️  Latency: {latency:.2f}s | 📄 Handled Pages: {handled_pages}", style="italic cyan")
        
        console.print(Panel(output_text, title="💡 Answer", border_style="blue", padding=(1, 2)))

if __name__ == "__main__":
    main()
