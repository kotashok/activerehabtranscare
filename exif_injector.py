import os
import sys
import piexif
from PIL import Image

def degToDmsRational(deg):
    """Convert decimal degrees to (degrees, minutes, seconds) rational for EXIF."""
    is_positive = deg >= 0
    deg = abs(deg)
    d = int(deg)
    md = (deg - d) * 60.0
    m = int(md)
    sd = (md - m) * 60.0
    
    # Return as EXIF rational (numerator, denominator)
    return (
        (d, 1),
        (m, 1),
        (int(sd * 100), 100)
    )

def inject_metadata(image_path, output_path=None):
    if output_path is None:
        output_path = image_path

    print(f"Opening image: {image_path}")
    im = Image.open(image_path)
    
    # Floating logo watermark overlay is disabled as requested by the user.
    # The logo is now generated/burned within the image environment during generation itself.
    
    # 1. Initialize EXIF dictionary
    exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}
    
    # Preserve existing EXIF if it exists
    if "exif" in im.info:
        try:
            exif_dict = piexif.load(im.info["exif"])
        except Exception:
            pass

    # 2. Add Title, Subject (Description)
    # 0th tags: Title (ImageDescription: 270), XPTitle (0x9c9b), XPSubject (0x9c9f), XPKeywords (0x9c9e)
    title = "ActiveRehab TransCare & Rehabilitation"
    subject = "Plot no 4-1-1, 41/A & 48, Laxmi Nagar Colony, Kompally, Hyderabad, Telangana 500100"
    tags_list = [
        "Transcare", "TransitionalCare", "StepDownCare", "RehabilitationCentre", "PostOperativeCare",
        "PostOpOrthoRecovery", "OrthoRehab", "StrokeRehab", "NeuroRehabilitation", "CardiorespiratoryRehab",
        "GeriatricCare", "GeriatricFallPrevention", "BalanceTherapy", "PhysiotherapyHyderabad",
        "PhysicalTherapy", "OccupationalTherapy", "Kompally", "KompallyHyderabad", "Secunderabad",
        "MedchalRoad", "HyderabadHealthcare", "HyderabadRehab", "HospitalToHome", "PremiumRecoverySuites",
        "EliteRehabilitation", "EliteRecovery", "247NursingSupport", "PatientSuccessStories", "RoadToRecovery",
        "HealingJourney", "PatientCareFirst", "HolisticHealing", "QualityOfLife", "AssistedLiving",
        "RestorativeCare", "WellnessJourney"
    ]
    tags_str = ";".join(tags_list)

    # Encode as UTF-16 LE for Windows properties compatibility
    exif_dict["0th"][piexif.ImageIFD.XPTitle] = title.encode('utf-16le')
    exif_dict["0th"][piexif.ImageIFD.XPSubject] = subject.encode('utf-16le')
    exif_dict["0th"][piexif.ImageIFD.XPKeywords] = tags_str.encode('utf-16le')
    
    # 3. Add 5-Star Rating (XPRating: 0x9c9e, or Rating: 18246)
    # XPPercentRated is 0x9c9d (100% for 5 Stars)
    exif_dict["0th"][0x9c9d] = b"100\x00"

    # 4. Add GPS Coordinates (17.570323550461595 N, 78.49346350312031 E)
    lat = 17.570323550461595
    lon = 78.49346350312031
    
    exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef] = b"N"
    exif_dict["GPS"][piexif.GPSIFD.GPSLatitude] = degToDmsRational(lat)
    
    exif_dict["GPS"][piexif.GPSIFD.GPSLongitudeRef] = b"E"
    exif_dict["GPS"][piexif.GPSIFD.GPSLongitude] = degToDmsRational(lon)
    
    # 5. Save with new EXIF
    exif_bytes = piexif.dump(exif_dict)
    
    # Ensure it's saved as RGB JPEG to support EXIF metadata fully
    if im.mode != 'RGB':
        im = im.convert('RGB')
        
    im.save(output_path, "jpeg", exif=exif_bytes, quality=95)
    print(f"[OK] Successfully injected all Local SEO EXIF data into {output_path}!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python exif_injector.py <image_path> [output_path]")
        sys.exit(1)
    
    img = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    inject_metadata(img, out)
