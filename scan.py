import customtkinter as ctk
import pyautogui
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

def extract_text():

    # Set pytesseract language to English, German, and an additional language for handwriting
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    tessdata_dir_config = '--tessdata-dir "C:\\Users\\AppData\\Local\\Programs\\Tesseract-OCR\\tessdata" --oem 3 --psm 6 -l eng+deu+script/Latin'

    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Convert the image to grayscale
    grayscale = screenshot.convert('L')

    # Enhance the contrast of the image
    enhancer = ImageEnhance.Contrast(grayscale)
    enhanced = enhancer.enhance(1.5)

    # Apply a smoothing filter
    smoothed = enhanced.filter(ImageFilter.SMOOTH_MORE)

    # Use pytesseract to convert the image to text
    text = pytesseract.image_to_string(smoothed, config=tessdata_dir_config)

    # Clear the previous content of the text area
    text_area.delete('1.0', 'end')

    # Display the text in the user interface text area
    text_area.insert('end', text)

# Create the main window
root = ctk.CTk()

# Set the window size to 700x600
root.geometry("600x500")

# Set the customtkinter theme to dark
ctk.set_default_color_theme("dark-blue")

# Create a button
button = ctk.CTkButton(root, text="Extract Text", command=extract_text)
button.pack()

# Create a text area
text_area = ctk.CTkTextbox(root, width=500, height=410)
text_area.pack()

# Start the user interface main loop
root.mainloop()
