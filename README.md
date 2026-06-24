# AI Interview Simulator

An interactive Streamlit application that simulates AI-powered interview sessions to help users practice and improve their interview skills.

## Features

- **AI-Powered Interviews**: Uses OpenAI API to generate realistic interview questions
- **Real-Time Feedback**: Get instant evaluation of your answers
- **PDF Support**: Upload and analyze PDF resumes or documents
- **Performance Metrics**: Track your progress with detailed metrics
- **Customizable Sessions**: Configure interview settings to match your needs

## Tech Stack

- **Frontend**: Streamlit
- **AI Model**: OpenAI GPT
- **Language**: Python

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Setup

1. Clone the repository:
```bash
git clone https://github.com/DhanaReddy25/AI-Interview-Simulator.git
cd AI-Interview-Simulator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
   - Create a `.streamlit/secrets.toml` file in the project root
   - Add your API key:
   ```toml
   openai_api_key = "your_api_key_here"
   ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Project Structure

```
AI-Interview-Simulator/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Dependencies

See `requirements.txt` for a complete list of dependencies.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Author

**DhanaReddy25** - [GitHub Profile](https://github.com/DhanaReddy25)

## Support

For issues, questions, or suggestions, please open an issue on the [GitHub Issues page](https://github.com/DhanaReddy25/AI-Interview-Simulator/issues).

---

**Happy interviewing! 🚀**
