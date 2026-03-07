import re
import json

def read_receipt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def extract_prices(text):
    pattern = r"\d[\d\s]*,\d{2}"
    prices = re.findall(pattern, text)
    return prices


def extract_products(text):
    pattern = r"\d+\.\s*\n(.+)"
    products = re.findall(pattern, text)
    return [p.strip() for p in products]


def extract_total(text):
    pattern = r"ИТОГО:\s*\n([\d\s]+,\d{2})"
    match = re.search(pattern, text)
    return match.group(1) if match else None


def extract_datetime(text):
    pattern = r"Время:\s*([\d\.]+\s[\d:]+)"
    match = re.search(pattern, text)
    return match.group(1) if match else None


def extract_payment_method(text):
    pattern = r"(Банковская карта|Наличные)"
    match = re.search(pattern, text)
    return match.group(1) if match else None


def parse_receipt(text):
    data = {
        "products": extract_products(text),
        "prices": extract_prices(text),
        "total_amount": extract_total(text),
        "datetime": extract_datetime(text),
        "payment_method": extract_payment_method(text),
    }
    return data


def main():
    text = read_receipt("raw.txt")

    parsed = parse_receipt(text)

    print("\nParsed Receipt Data\n")
    print(json.dumps(parsed, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()