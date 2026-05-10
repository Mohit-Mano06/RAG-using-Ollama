import time
import logging
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.logging import RichHandler
from rich.text import Text
from rich.live import Live
from .rag import get_answer

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
        
        with console.status("[bold yellow]Retrieving context...[/bold yellow]", spinner="dots"):
            response_stream, handled_pages = get_answer(user_query)
            
        output_text = Text("", style="white")
        
        # We use transient=True so the Live display cleans itself up after it finishes
        # This prevents terminal scrolling artifacts from breaking the box shape.
        with Live(Panel(output_text, title="💡 Answer", border_style="blue"), console=console, refresh_per_second=8, transient=True) as live:
            for chunk in response_stream:
                output_text.append(chunk.content)
                live.update(Panel(output_text, title="💡 Answer", border_style="blue"))
                
            latency = time.perf_counter() - start_time
            output_text.append(f"\n\n⏱️  Latency: {latency:.2f}s | 📄 Handled Pages: {handled_pages}", style="italic cyan")
            
        # Print the final perfect panel once generation is complete
        console.print(Panel(output_text, title="💡 Answer", border_style="blue", padding=(1, 2)))

if __name__ == "__main__":
    main()
