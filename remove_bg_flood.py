from PIL import Image, ImageDraw

def remove_background_flood(image_path, output_path):
    img = Image.open(image_path).convert("RGBA")
    
    # Target colors found earlier: (1,1,1) and (80,80,80)
    # We'll use flood fill from multiple edge points to be safe
    
    width, height = img.size
    
    # We want to keep the logo, so we'll fill the background with a specific "to-be-transparent" color
    # Let's use magenta (255, 0, 255, 255) as a temporary mask
    temp_color = (255, 0, 255, 255)
    
    # Flood fill from etc
    seeds = [(0,0), (width-1, 0), (0, height-1), (width-1, height-1), (width//2, 0), (0, height//2)]
    
    for seed in seeds:
        color = img.getpixel(seed)
        # Only flood if it looks like background
        if color[0] < 100 and color[1] < 100 and color[2] < 100:
            ImageDraw.floodfill(img, seed, temp_color, thresh=30)
            
    # Now make the temp_color transparent
    data = img.getdata()
    new_data = []
    for item in data:
        if item == temp_color:
            new_data.append((0,0,0,0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path)
    print(f"Flood-fill background removal done. Saved to {output_path}")

if __name__ == "__main__":
    remove_background_flood("public/logo2.png", "public/logo2.png")
