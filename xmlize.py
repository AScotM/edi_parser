import argparse
import xml.etree.ElementTree as ET
from xml.dom import minidom

def get_edi_documents():
    """Returns a dictionary of EDI standards and their document types."""
    return {
        "ANSI X12 (North American Standard)": {
            "204": "Motor Carrier Load Tender - A transportation order for shipping goods",
            "810": "Invoice - Used for sending billing information",
            "820": "Payment Order/Remittance Advice - Communicates payment details from buyer to seller",
            "834": "Benefit Enrollment and Maintenance - For exchanging enrollment information in health insurance plans",
            "837": "Healthcare Claim - Used for submitting healthcare claims electronically",
            "846": "Inventory Inquiry/Advice - Provides details about stock availability",
            "850": "Purchase Order (PO) - Used to request products or services",
            "855": "Purchase Order Acknowledgment - Confirms receipt and acceptance of a purchase order",
            "856": "Advance Shipping Notice (ASN) - Provides shipment details to the recipient before delivery",
            "867": "Product Transfer and Resale Report - Tracks resales of products through distribution channels",
            "997": "Functional Acknowledgment - Confirms receipt of an EDI transaction",
        },
        "EDIFACT (International Standard)": {
            "DESADV": "Dispatch Advice - Provides shipment details (like ASN in X12)",
            "IFCSUM": "International Forwarding and Consolidation Summary - Used in logistics for shipment consolidation",
            "INVOIC": "Invoice - Used for billing and invoicing globally",
            "ORDERS": "Purchase Order - Used to order goods or services internationally",
            "ORDRSP": "Order Response - Communicates acceptance or rejection of a purchase order",
            "PAYMUL": "Multiple Payment Order - Handles multiple payments in financial transactions",
            "PRICAT": "Price/Sales Catalog - Contains pricing and product information",
            "RECADV": "Receiving Advice - Notifies the sender of the goods that they were received",
        },
    }

def validate_standard(standard):
    """Validates if the provided standard exists in the EDI documents.
    
    Args:
        standard (str): The EDI standard to validate
        
    Raises:
        ValueError: If the standard is not found
    """
    valid_standards = get_edi_documents().keys()
    if standard and standard not in valid_standards:
        raise ValueError(f"Invalid standard. Must be one of: {', '.join(valid_standards)}")

def generate_xml(edi_documents):
    """Generates a formatted XML string from EDI documents dictionary.
    
    Args:
        edi_documents (dict): Dictionary containing EDI standards and documents
        
    Returns:
        str: Pretty-printed XML string
    """
    try:
        root = ET.Element("EDI_Documents")
        
        for standard, documents in edi_documents.items():
            standard_element = ET.SubElement(root, "Standard", name=standard)
            for code, description in documents.items():
                document_element = ET.SubElement(standard_element, "Document", code=code)
                document_element.text = description
        
        rough_string = ET.tostring(root, encoding="unicode")
        return minidom.parseString(rough_string).toprettyxml(indent="  ")
    except Exception as e:
        return f"<Error>Failed to generate XML: {str(e)}</Error>"

def list_edi_documents(filter_standard=None):
    """Lists EDI documents in XML format, optionally filtered by standard.
    
    Args:
        filter_standard (str, optional): Standard to filter by
    """
    try:
        edi_documents = get_edi_documents()
        validate_standard(filter_standard)
        
        if filter_standard and filter_standard in edi_documents:
            edi_documents = {filter_standard: edi_documents[filter_standard]}
        
        xml_output = generate_xml(edi_documents)
        print(xml_output)
    except ValueError as e:
        print(f"<Error>{str(e)}</Error>")

def search_edi_code(code):
    """Searches for a specific EDI code and returns its details in XML format.
    
    Args:
        code (str): EDI code to search for
    """
    try:
        code = code.upper()  # Case-insensitive search
        edi_documents = get_edi_documents()
        
        for standard, documents in edi_documents.items():
            if code in documents:
                root = ET.Element("Search_Result")
                document_element = ET.SubElement(root, "Document", code=code, standard=standard)
                document_element.text = documents[code]
                pretty_xml = minidom.parseString(ET.tostring(root, encoding="unicode")).toprettyxml(indent="  ")
                print(pretty_xml)
                return
        
        print(f"<Error>EDI code {code} not found.</Error>")
    except Exception as e:
        print(f"<Error>Search failed: {str(e)}</Error>")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="List and search EDI documents in XML format.",
        epilog="Examples:\n"
               "  List all: python script.py\n"
               "  Filter: python script.py --standard 'ANSI X12 (North American Standard)'\n"
               "  Search: python script.py --search '850'",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--standard", type=str, help="Filter by EDI standard (e.g., 'ANSI X12 (North American Standard)')")
    parser.add_argument("--search", type=str, help="Search for a specific EDI code (e.g., '850')")
    args = parser.parse_args()
    
    if args.search:
        search_edi_code(args.search)
    else:
        list_edi_documents(args.standard)
