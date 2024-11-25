# Virtual Limit Mindmapper

An elegant web application that generates beautiful, interactive mindmaps from any topic using AI. Built with FastAPI, DaisyUI, and OpenAI's GPT-4.

## Setup Instructions

1. **Environment Setup**
   ```bash
   # Create and activate conda environment
   conda create -n mindmapper python=3.10
   conda activate mindmapper

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **API Key Setup**
   ```bash
   # Set OpenAI API key in fish shell
   set -x OPENAI_API_KEY your_api_key_here
   ```

3. **Run Application**
   ```bash
   # Start the server
   python main.py

   # Open in browser
   http://127.0.0.1:8001
   ```

## How to Use

1. Type any topic into the input box
2. Press Enter to generate mindmap
3. Use mouse to interact:
   - Scroll wheel: Zoom in/out
   - Click + drag: Pan view
   - Drag nodes: Rearrange
   - Hover: See details

## Tech Stack

- **Backend**: FastAPI, OpenAI GPT-4
- **Frontend**: DaisyUI/Tailwind, AnimeJS, vis-network

## License

MIT License - see [LICENSE](LICENSE)