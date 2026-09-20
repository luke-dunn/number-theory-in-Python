from rich.console import Console
from rich.table import Table
import os

console = Console()
table = Table(title="Directory Listing")

table.add_column("Name", style="cyan", no_wrap=True)
table.add_column("Type", style="green")
table.add_column("Size", justify="right")

for f in os.listdir():
    ftype = "Folder" if os.path.isdir(f) else "File"
    fsize = os.path.getsize(f)
    table.add_row(f, ftype, f"{fsize} B")

console.print(table)

