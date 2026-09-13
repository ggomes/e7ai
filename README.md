# e7ai

## Berkeley JupyterHub and VS Code for the Web

The activities are designed to be pulled into Berkeley's JupyterHub with
nbgitpuller and opened in VS Code for the Web. The repository includes:

- `.github/copilot-instructions.md`, which supplies the persistent tutor role
  and activity boundaries;
- `.github/prompts/session0-1-tutor.prompt.md`, a reusable prompt for starting
  the hovering-drone tutoring session;
- `.vscode/extensions.json`, which recommends Python, Jupyter, and Copilot;
- `.vscode/settings.json`, which points notebook execution at the current
  activity folder.

The exact nbgitpuller URL and VS Code service path are deployment-specific.
Configure the course link to open `sessions/session0-1/activity.ipynb` in the
Berkeley VS Code service, then test it with a student account. If the service
does not automatically open Copilot Chat, the notebook's **Start here**
section provides the reliable fallback: open Chat and send the supplied first
request.

Copilot must be authenticated separately in the student's GitHub account, and
the Berkeley image must provide the GitHub Copilot and Copilot Chat extensions.
Repository files can recommend and guide those extensions, but cannot install
them or guarantee that a browser session will automatically submit a Chat
message.
