from typing import List, Union, Generator
from pathlib import Path

class Pipeline:
    def __init__(self):
        self.html_path = Path("/app/1R42_interactive.html")  # Update filename if needed

    async def on_startup(self):
        print("HTML Pipeline started.")

    async def on_shutdown(self):
        print("HTML Pipeline shutting down.")

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator]:

        def generator():
            try:
                if self.html_path.exists():
                    # You can either yield a clickable link:
                    yield f"[Open Protein 3D Viewer]({self.html_path.as_uri()})\n"
                    
                    # Or embed raw HTML (works in notebooks or Markdown viewers that allow HTML)
                    # html_content = self.html_path.read_text()
                    # yield html_content
                else:
                    yield f"Error: HTML file not found at {self.html_path}\n"
            except Exception as e:
                yield f"Error: {e}\n"

        return generator()
