import os
from PIL import Image, ImageDraw, ImageFont

def brand_hiring_poster():
    # 1. Load generated poster and official logo
    poster_path = r"C:\Users\conta\.gemini\antigravity\brain\f14f7863-a35b-43c6-9436-0db3f541b923\hiring_physiotherapist_instagram_1780114976140.png"
    logo_path = r"c:\Users\conta\.antigravity\transcare_rehab\website\logo.png"
    output_path = r"c:\Users\conta\.antigravity\transcare_rehab\website\hiring_physiotherapist_instagram.png"

    print("Opening generated hiring poster...")
    im = Image.open(poster_path)
    draw = ImageDraw.Draw(im)

    # 2. Cover the old dummy website and email with a clean white card overlay
    print("Covering dummy text...")
    # Coordinates to cover: X from 130 to 480, Y from 810 to 880
    draw.rectangle([130, 810, 520, 890], fill="#ffffff")

    # 3. Add actual hiring details in a premium, highly readable font
    print("Injecting actual ActiveRehab TransCare hiring contacts...")
    try:
        font_path = r"C:\Windows\Fonts\arial.ttf"
        font_bold = ImageFont.truetype(font_path, 20)
        font_regular = ImageFont.truetype(font_path, 18)
    except IOError:
        font_bold = ImageFont.load_default()
        font_regular = ImageFont.load_default()

    # Draw contact text
    draw.text((135, 815), "activerehab.tc@gmail.com", fill="#003366", font=font_bold)
    draw.text((135, 845), "WhatsApp: +91 81068 22020", fill="#e65c00", font=font_bold)
    draw.text((135, 870), "Website: www.activerehabtranscare.in", fill="#475569", font=font_regular)

    # 4. Overlay the corporate brand logo in the top-right corner
    if os.path.exists(logo_path):
        print("Overlaying official ActiveRehab TransCare logo in top-right...")
        logo = Image.open(logo_path)
        
        # Resize logo to fit elegantly in the top-right (e.g. Width: 220px)
        target_width = 240
        logo_aspect = logo.height / logo.width
        target_height = int(target_width * logo_aspect)
        
        # Resample logo
        resample_filter = Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.LANCZOS
        logo_resized = logo.resize((target_width, target_height), resample_filter)
        
        # Paste logo at top-right
        position = (1024 - target_width - 50, 45)
        
        # Paste with alpha transparency
        if logo_resized.mode in ('RGBA', 'LA') or (logo_resized.mode == 'P' and 'transparency' in logo_resized.info):
            im.paste(logo_resized, position, logo_resized)
        else:
            im.paste(logo_resized, position)
        print("[OK] Corporate logo watermark applied successfully!")
    else:
        print("Warning: logo.png not found, skipping watermark.")

    # 5. Save final high-resolution poster
    im.save(output_path, "PNG")
    print(f"[OK] Branded hiring poster successfully saved to: {output_path}")

if __name__ == "__main__":
    brand_hiring_poster()
