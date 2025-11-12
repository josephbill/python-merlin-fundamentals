import cloudinary
import cloudinary.api
import requests
import time

# ---- Cloudinary Configuration ----
cloudinary.config(
    cloud_name="dddrbbrjk",
    api_key="363728576685873",
    api_secret="8VhOkrGadVBEzhcFM3csN6BFlvY"
)

# ---- OCR.Space Configuration ----
OCR_SPACE_API_KEY = "K85196021888957"  # Get from https://ocr.space/ocrapi
# ---- Fetch all Cloudinary images with pagination ----
def get_all_uploaded_images():
    print("[DEBUG] Fetching all uploaded images from Cloudinary...")
    all_images = []
    next_cursor = None

    while True:
        result = cloudinary.api.resources(
            type="upload",
            max_results=100,
            next_cursor=next_cursor
        )
        all_images.extend(res["secure_url"] for res in result["resources"])
        print(f"[DEBUG] Fetched {len(result['resources'])} images, total so far: {len(all_images)}")

        next_cursor = result.get("next_cursor")
        if not next_cursor:
            break

    print(f"[DEBUG] Total images fetched: {len(all_images)}")
    return all_images

# ---- Extract text from image using OCR.Space ----
def extract_text_from_image(url):
    print(f"[DEBUG] Sending image to OCR.Space: {url}")
    api_url = "https://api.ocr.space/parse/image"
    payload = {
        'apikey': OCR_SPACE_API_KEY,
        'url': url,
        'language': 'eng'
    }
    try:
        response = requests.post(api_url, data=payload, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] OCR.Space request failed: {e}")
        return ""

    result = response.json()
    if result.get("IsErroredOnProcessing"):
        print(f"[ERROR] OCR.Space failed: {result.get('ErrorMessage')}")
        return ""

    text = result["ParsedResults"][0]["ParsedText"]
    return text

# ---- Parse ticket details from extracted text ----
def parse_ticket_details(text):
    details = {}
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    for line in lines:
        lower = line.lower()
        # Match "Seats : E30" or "Seats: E30" pattern
        if "seats" in lower and ":" in line:
            parts = line.split(":", 1)
            if len(parts) == 2:
                details["seat"] = parts[1].strip()
        # Match "Order Number: 2004" pattern
        elif "order number" in lower and ":" in line:
            parts = line.split(":", 1)
            if len(parts) == 2:
                details["order_number"] = parts[1].strip()

    return details

# ---- Check if all order numbers have been found ----
def all_orders_found(order_map):
    for order_num, seat in order_map.items():
        if seat is None:
            return False
    return True

# ---- Collect tickets for multiple orders with early exit ----
def collect_tickets_for_orders(order_numbers, delay=1):
    print(f"[DEBUG] Collecting tickets for {len(order_numbers)} orders...")
    
    # Initialize order map with None values
    order_map = {str(num): None for num in order_numbers}
    
    urls = get_all_uploaded_images()
    total_images = len(urls)
    
    for idx, url in enumerate(urls, 1):
        # Check if all orders have been found
        if all_orders_found(order_map):
            print(f"\n[SUCCESS] ✅ All {len(order_numbers)} orders found! Stopping scan.")
            print(f"[INFO] Processed {idx - 1} out of {total_images} images")
            break
        
        print(f"\n[DEBUG] Processing image {idx}/{total_images}")
        text = extract_text_from_image(url)
        
        if not text:
            print(f"[DEBUG] ⚠️ No text extracted from image")
            time.sleep(delay)
            continue
        
        details = parse_ticket_details(text)
        order_number = details.get("order_number")
        seat = details.get("seat")

        if order_number and order_number in order_map:
            # Only update if this order hasn't been found yet
            if order_map[order_number] is None:
                order_map[order_number] = seat
                found_count = sum(1 for v in order_map.values() if v is not None)
                print(f"[DEBUG] ✅ Match found! Order {order_number}: {seat}")
                print(f"[PROGRESS] Found {found_count}/{len(order_numbers)} orders")
            else:
                print(f"[DEBUG] ℹ️ Order {order_number} already found, skipping duplicate")
        else:
            print(f"[DEBUG] ❌ No match - Order: {order_number}, Seat: {seat}")

        time.sleep(delay)  # avoid hitting OCR.Space rate limit
    else:
        # Loop completed without break (all images processed)
        found_count = sum(1 for v in order_map.values() if v is not None)
        print(f"\n[INFO] Finished scanning all {total_images} images")
        print(f"[INFO] Found {found_count}/{len(order_numbers)} orders")

    return order_map

# ---- Run the Script ----
if __name__ == "__main__":
    ORDER_NUMBERS = [
        1936, 1937, 1938, 1939, 1941, 1942, 1943, 1945, 1951, 1955,
        1957, 1958, 1964, 1975, 1980, 1981, 1983, 1984, 1985, 1986,
        1987, 1988, 1991, 1994, 1995, 1996, 2010, 2011, 2012, 2024,
        2025, 2026, 2027, 2030, 2031, 2032, 2042, 2046, 2057, 2058,
        2060, 2061, 2062, 2063, 2080, 2081, 2082
    ]
    
    print("=" * 60)
    print("TICKET SCANNER - Starting Process")
    print("=" * 60)
    
    result = collect_tickets_for_orders(ORDER_NUMBERS, delay=1)

    print("\n" + "=" * 60)
    print("FINAL RESULTS - ORDER TO SEAT MAPPING")
    print("=" * 60)
    
    # Separate found and not found orders
    found_orders = {k: v for k, v in result.items() if v is not None}
    missing_orders = {k: v for k, v in result.items() if v is None}
    
    if found_orders:
        print(f"\n✅ FOUND ({len(found_orders)} orders):")
        for order, seat in sorted(found_orders.items(), key=lambda x: int(x[0])):
            print(f"  Order {order}: {seat}")
    
    if missing_orders:
        print(f"\n❌ NOT FOUND ({len(missing_orders)} orders):")
        for order in sorted(missing_orders.keys(), key=lambda x: int(x)):
            print(f"  Order {order}: No ticket found")
    
    print("\n" + "=" * 60)