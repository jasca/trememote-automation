from PIL import Image
from collections import Counter

def analyze_colors(image_path):
    img = Image.open(image_path).convert("RGB")
    data = list(img.getdata())
    
    # Analyze colors at the edges
    width, height = img.size
    edges = []
    for x in range(width):
        edges.append(img.getpixel((x, 0)))
        edges.append(img.getpixel((x, height-1)))
    for y in range(height):
        edges.append(img.getpixel((0, y)))
        edges.append(img.getpixel((width-1, y)))
        
    common = Counter(edges).most_common(5)
    print(f"Most common edge colors: {common}")

if __name__ == "__main__":
    analyze_colors("public/logo2.png")
