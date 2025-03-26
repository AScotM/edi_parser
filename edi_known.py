import argparse
from typing import Dict, Optional

# Constants
ANSI_X12 = "ANSI X12 (North American Standard)"
EDIFACT = "EDIFACT (International Standard)"
TRADACOMS = "TRADACOMS (UK Retail Standard)"
VDA = "VDA (German Automotive Standard)"
ROSETTANET = "RosettaNet (Technology Industry Standard)"

def get_edi_documents() -> Dict[str, Dict[str, str]]:
    return {
        ANSI_X12: {
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
        EDIFACT: {
            "DESADV": "Dispatch Advice - Provides shipment details (like ASN in X12)",
            "IFCSUM": "International Forwarding and Consolidation Summary - Used in logistics for shipment consolidation",
            "INVOIC": "Invoice - Used for billing and invoicing globally",
            "ORDERS": "Purchase Order - Used to order goods or services internationally",
            "ORDRSP": "Order Response - Communicates acceptance or rejection of a purchase order",
            "PAYMUL": "Multiple Payment Order - Handles multiple payments in financial transactions",
            "PRICAT": "Price/Sales Catalog - Contains pricing and product information",
            "RECADV": "Receiving Advice - Notifies the sender of the goods that they were received",
        },
        TRADACOMS: {
            "DELHDR": "Delivery Header - Provides delivery instructions for an order",
            "INVFIL": "Invoice File - Used for billing in the UK retail sector",
            "ORDHDR": "Order Header - The header of a purchase order document",
        },
        VDA: {
            "4905": "Delivery Schedule - Communicates delivery schedules in automotive manufacturing",
            "4913": "Invoice - Used for billing in the automotive industry",
        },
        ROSETTANET: {
            "3A4": "Purchase Order - Used for ordering goods in the high-tech industry",
            "4B2": "Advance Shipment Notification - Communicates shipment details in the tech supply chain",
        },
    }

def list_edi_documents(filter_standard: Optional[str] = None) -> None:
    edi_documents = get_edi_documents()
    if filter_standard and filter_standard in edi_documents:
        edi_documents = {filter_standard: edi_documents[filter_standard]}
    
    print("\nKnown EDI Documents and Their Uses:\n")
    for standard, documents in edi_documents.items():
        print(f"{standard}:")
        for code in sorted(documents.keys(), key=lambda x: (int(x) if x.isdigit() else float('inf'), x)):
            print(f"  {code}: {documents[code]}")
        print()

def search_edi_code(code: str) -> None:
    edi_documents = get_edi_documents()
    for standard, documents in edi_documents.items():
        if code in documents:
            print(f"{code}: {documents[code]} (Found in {standard})")
            return
    print(f"EDI code {code} not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--standard", type=str, help=f"Filter by EDI standard (e.g., '{ANSI_X12}')")
    parser.add_argument("--search", type=str, help="Search for a specific EDI code (e.g., '850')")
    args = parser.parse_args()
    
    if args.search:
        search_edi_code(args.search)
    else:
        list_edi_documents(args.standard)
