# 🖼️ Image Resizer Tool

A simple Python project (Jupyter Notebook) to **batch resize images**.  
It takes all images from an input folder, resizes them to a specified dimension, and saves them in an output folder.  
Supports `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.gif`.

---

## 🚀 Features
- Resize all images in a folder with one function call  
- Converts transparent images (`RGBA`) to `RGB` automatically for JPEG compatibility  
- Saves resized images in a separate output folder  
- Supports preview of resized images inside Jupyter Notebook (using matplotlib)  
- Works on both **PNG/JPG** and converts to `.jpg` by default  

---

## 📂 Project Structure
├── Untitled7.ipynb # Jupyter Notebook with code
├── images_input/ 
├── README.md # Project documentation




---

## ⚙️ Requirements
- Python 3.x
- [Pillow](https://python-pillow.org/) (`pip install pillow`)
- [Matplotlib](https://matplotlib.org/) (`pip install matplotlib`)

---

## 🛠️ How to Use
1️⃣ Load Or Download images\
2️⃣ Install Dependencies
3️⃣ Add Images

Place all the images you want to resize into the images_input/ folder.

4️⃣ Run the Notebook

Open the notebook in Jupyter or VS Code:

jupyter notebook Untitled7.ipynb


Run the cells step by step.

5️⃣ View Resized Images

Resized images will be saved in images_output/ folder.

You can also preview them directly in the notebook.

📸 Example Output

Input images:

car3.png

car4.png

hero.jpg

mission.jpg

After resizing →
Output folder contains:

car3.jpg

car4.jpg

hero.jpg

mission.jpg

All resized to 400 × 400 (or your chosen size).
