from PIL import Image

def remove_background(image_path, output_path):
    img = Image.open(image_path).convert("RGBA")
    data = img.getdata()
    
    bg_colors = [(1, 1, 1), (80, 80, 80), (0, 0, 0), (2, 2, 2)]
    
    new_data = []
    for item in data:
        r, g, b, a = item
        
        is_bg = False
        for bg in bg_colors:
            # Check distance to bg colors
            dist = abs(r - bg[0]) + abs(g - bg[1]) + abs(b - bg[2])
            if dist < 15: # Tight threshold
                is_bg = True
                break
        
        if is_bg:
            new_data.append((r, g, b, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path)
    print(f"Refined background removal. Saved to {output_path}")

if __name__ == "__main__":
    remove_background("public/logo2.png", "public/logo2.png")
