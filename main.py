from edi_parser import EDIProcessor  # Import the processor class from edi_parser

def main():
    # Example EDI Document
    edi_document = """
    UNA:+.? '
    UNB+UNOC:3+123456789:14+987654321:14+230120:1234+00000000000111'
    UNH+1+ORDERS:D:96A:UN'
    BGM+220+PO123456+9'
    DTM+137:20230120:102'
    NAD+BY+123456789::16'
    UNT+6+1'
    UNZ+1+00000000000111'
    """

    # Define schema for validation
    schema = {
        "UNB": {"required": True},
        "UNH": {"required": True},
        "BGM": {"required": True},
        "UNT": {"required": True},
        "UNZ": {"required": True},
    }

    # Process the EDI document using EDIProcessor
    processor = EDIProcessor(edi_document, schema)
    parsed_data, is_valid = processor.process()

    # Print structured output
    print("Parsed EDI Document:")
    for segment, elements in parsed_data.items():
        print(f"\nSegment: {segment}")
        for i, element in enumerate(elements):
            print(f"  Element {i+1}: {element}")

    # Print validation result
    if is_valid:
        print("\nEDI document is valid.")
    else:
        print("\nEDI document is invalid.")

if __name__ == "__main__":
    main()

