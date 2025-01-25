from edi_parser import EDIProcessor


BATMAN_COLOR_PALETTE = {
    "background": "#1E1E1E",  # Dark gray
    "highlight": "#B68D40",   # Bronze
    "accent": "#363636",      # Charcoal gray
    "error": "#FF3131",       # Red
}

def print_with_palette(data, palette):
    """Prints data using the Batman 2022 color palette."""
    from rich.console import Console
    from rich.text import Text

    console = Console()

    for segment, elements in data.items():
        title = Text(f"{segment}:", style=f"bold {palette['highlight']}")
        console.print(title)
        for element in elements:
            element_text = Text(f"  {element}", style=f"color({palette['accent']})")
            console.print(element_text)

def main():
    # Sample EDI Document
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

    # Schema for validation
    schema = {
        "UNB": {"required": True},
        "UNH": {"required": True},
        "BGM": {"required": True},
        "UNT": {"required": True},
        "UNZ": {"required": True},
    }

    # Process the EDI document
    processor = EDIProcessor(edi_document, schema)
    parsed_data, is_valid = processor.process()

    # Display parsed data using the Batman 2022 color palette
    print("\nParsed EDI Data (Styled):\n")
    print_with_palette(parsed_data, BATMAN_COLOR_PALETTE)

if __name__ == "__main__":
    main()

