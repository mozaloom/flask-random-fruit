# Flask Random Fruit

A simple Flask web application that generates random fruit suggestions.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/flask-random-fruit.git
   cd flask-random-fruit
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```
python app.py
```

Or use the Makefile:
```
make run
```

Then open your browser and navigate to `http://localhost:5000/` to see a random fruit suggestion.

## Testing

Run tests with:
```
python -m pytest
```

Or use the Makefile:
```
make test
```
