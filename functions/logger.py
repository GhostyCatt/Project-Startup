# Library Imports
import nextcord, colorama, datetime
from nextcord.ext import commands

# Functions 
def log(prefix: str, text: str) -> None:
    """Log text into `.log` and the `console`"""
    logable: str = f"[ {datetime.datetime.utcnow().strftime('%m/%d/%Y %H:%M:%S')} ]  {prefix.upper()}  {text}\n"

    with open(".log", "a") as lf:
        lf.write(logable)
    
    print(logable[:-1])
    
    return logable