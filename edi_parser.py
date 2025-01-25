import re
from typing import List, Dict, Any


class EDIParser:
    """Parser for EDI/EDIFACT documents."""
    
    def __init__(self, edi_document: str):
        self.edi_document = edi_document
        self.segment_terminator = "'"
        self.data_element_separator = "+"
        self.component_separator = ":"
        self.parsed_data = {}

        # Check and apply custom delimiters from the UNA header
        self._extract_delimiters()

    def _extract_delimiters(self):
        """Extract delimiters from UNA header if present."""
        if self.edi_document.startswith("UNA"):
            self.data_element_separator = self.edi_document[3]
            self.component_separator = self.edi_document[4]
            self.segment_terminator = self.edi_document[8]
            # Remove the UNA segment
            self.edi_document = self.edi_document[9:].strip()

    def parse(self) -> Dict[str, List[Any]]:
        """Parse the EDI/EDIFACT document into a structured dictionary."""
        # Split into segments
        segments = self.edi_document.split(self.segment_terminator)
        for segment in segments:
            segment = segment.strip()
            if not segment:
                continue  # Skip empty lines or segments

            # Split the segment into elements
            elements = segment.split(self.data_element_separator)
            segment_type = elements.pop(0)  # First element is the segment type

            # Parse components within each element
            for i, element in enumerate(elements):
                elements[i] = element.split(self.component_separator)

            # Store the parsed segment
            if segment_type not in self.parsed_data:
                self.parsed_data[segment_type] = []
            self.parsed_data[segment_type].append(elements)

        return self.parsed_data


class EDIValidator:
    """Validator for EDI/EDIFACT documents."""
    
    def __init__(self, schema: Dict[str, Dict[str, Any]]):
        """
        Initialize the validator with a schema.
        :param schema: A dictionary defining segment rules.
                       Example: {'UNB': {'required': True}, 'BGM': {'required': True}}
        """
        self.schema = schema

    def validate(self, parsed_data: Dict[str, List[Any]]) -> bool:
        """Validate parsed EDI data against the schema."""
        is_valid = True
        for segment_type, rules in self.schema.items():
            if rules.get("required", False) and segment_type not in parsed_data:
                print(f"Missing required segment: {segment_type}")
                is_valid = False
            else:
                # Optionally, validate individual fields in each segment
                for segment in parsed_data.get(segment_type, []):
                    # Add field-specific validation here
                    pass

        return is_valid


class EDIProcessor:
    """Main processor to parse, validate, and output EDI/EDIFACT documents."""
    
    def __init__(self, edi_document: str, schema: Dict[str, Dict[str, Any]]):
        self.edi_document = edi_document
        self.schema = schema

    def process(self):
        """Process the EDI document."""
        # Step 1: Parse the document
        parser = EDIParser(self.edi_document)
        parsed_data = parser.parse()
        print("\nParsed EDI Document:")
        for segment, elements in parsed_data.items():
            print(f"{segment}: {elements}")

        # Step 2: Validate the document
        validator = EDIValidator(self.schema)
        is_valid = validator.validate(parsed_data)
        if is_valid:
            print("\nEDI document is valid.")
        else:
            print("\nEDI document is invalid.")

        return parsed_data, is_valid


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

# Process the EDI document
processor = EDIProcessor(edi_document, schema)
parsed_data, is_valid = processor.process()

