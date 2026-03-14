"""REPL skin for interactive CLI sessions with GIMP."""

import sys

try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.formatted_text import HTML
    HAS_PROMPT_TOOLKIT = True
except ImportError:
    HAS_PROMPT_TOOLKIT = False


# ANSI color codes
COLORS = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "accent": "\033[38;5;208m",  # warm orange (GIMP brand)
    "success": "\033[38;5;82m",
    "error": "\033[38;5;196m",
    "warning": "\033[38;5;220m",
    "info": "\033[38;5;75m",
    "muted": "\033[38;5;245m",
}


class ReplSkin:
    """Unified terminal UI for GIMP CLI REPL mode."""

    APP_NAME = "GIMP CLI"
    ACCENT = "accent"

    def __init__(self):
        self.session = None
        if HAS_PROMPT_TOOLKIT:
            self.session = PromptSession()

    def _c(self, color, text):
        return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"

    def print_banner(self):
        """Print the REPL welcome banner."""
        border = self._c("accent", "+" + "-" * 50 + "+")
        print(border)
        print(self._c("accent", f"|{'GIMP CLI - Interactive Mode':^50}|"))
        print(self._c("accent", f"|{'cli-anything-gimp v1.0.0':^50}|"))
        print(border)
        print(self._c("muted", "Type 'help' for commands, 'quit' to exit.\n"))

    def prompt(self, text="gimp> "):
        """Get input with prompt."""
        if self.session:
            try:
                return self.session.prompt(HTML(f"<b>{text}</b> "))
            except (EOFError, KeyboardInterrupt):
                return None
        try:
            return input(f"{self._c('accent', text)} ")
        except (EOFError, KeyboardInterrupt):
            return None

    def success(self, msg):
        print(f"  {self._c('success', '✓')} {msg}")

    def error(self, msg):
        print(f"  {self._c('error', '✗')} {msg}", file=sys.stderr)

    def warning(self, msg):
        print(f"  {self._c('warning', '!')} {msg}")

    def info(self, msg):
        print(f"  {self._c('info', 'i')} {msg}")

    def table(self, headers, rows):
        """Print a formatted table."""
        widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                widths[i] = max(widths[i], len(str(cell)))
        header_line = " | ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
        sep_line = "-+-".join("-" * w for w in widths)
        print(f"  {self._c('bold', header_line)}")
        print(f"  {sep_line}")
        for row in rows:
            line = " | ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row))
            print(f"  {line}")

    def help(self, commands):
        """Print help for available commands."""
        print(f"\n  {self._c('bold', 'Available Commands:')}\n")
        for cmd, desc in commands.items():
            print(f"  {self._c('accent', cmd.ljust(20))} {desc}")
        print()

    def progress(self, msg, current, total):
        """Print a progress indicator."""
        pct = int(current / total * 100) if total else 0
        bar_len = 30
        filled = int(bar_len * current / total) if total else 0
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"\r  {self._c('info', bar)} {pct}% {msg}", end="", flush=True)
        if current >= total:
            print()

    def create_prompt_session(self):
        """Create a new prompt session."""
        if HAS_PROMPT_TOOLKIT:
            self.session = PromptSession()
        return self.session

    def get_input(self, prompt_text="gimp> "):
        """Get input with fallback."""
        return self.prompt(prompt_text)
