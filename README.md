# ASCII Image Converter

Convert images and webcam captures to ASCII art in your terminal, with optional Matrix-style green coloring.

## Features

- Capture images directly from your webcam.
- Convert any image file to ASCII art.
- Optional green "Matrix" effect using colorama.

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

Run the main script:

```bash
python main.py
```

### Options

- **Webcam Capture:**  
  When prompted, enter `y` to capture an image from your webcam.  
  Press `c` to capture when the preview appears.

- **Image File:**  
  Enter `n` to use an image file.  
  Provide the path to your image when prompted.

- **Matrix Effect:**  
  Choose whether to display the ASCII art in green.

## Output

ASCII art is printed directly in your terminal.

## Notes

- Webcam images are resized to **400x150** pixels.
- Image files are resized to **200x150** pixels.
- Works on Linux and requires Python 3.

##