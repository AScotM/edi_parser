# Known EDI Documents and Their Uses

def list_edi_documents():
    edi_documents = {
        "ANSI X12 (North American Standard)": [
            {"810": "Invoice - Used for sending billing information"},
            {"850": "Purchase Order (PO) - Used to request products or services"},
            {"855": "Purchase Order Acknowledgment - Confirms receipt and acceptance of a purchase order"},
            {"856": "Advance Shipping Notice (ASN) - Provides shipment details to the recipient before delivery"},
            {"820": "Payment Order/Remittance Advice - Communicates payment details from buyer to seller"},
            {"997": "Functional Acknowledgment - Confirms receipt of an EDI transaction"},
            {"846": "Inventory Inquiry/Advice - Provides details about stock availability"},
            {"837": "Healthcare Claim - Used for submitting healthcare claims electronically"},
            {"834": "Benefit Enrollment and Maintenance - For exchanging enrollment information in health insurance plans"},
            {"204": "Motor Carrier Load Tender - A transportation order for shipping goods"},
        ],
        "EDIFACT (International Standard)": [
            {"INVOIC": "Invoice - Used for billing and invoicing globally"},
            {"ORDERS": "Purchase Order - Used to order goods or services internationally"},
            {"ORDRSP": "Order Response - Communicates acceptance or rejection of a purchase order"},
            {"DESADV": "Dispatch Advice - Provides shipment details (like ASN in X12)"},
            {"IFCSUM": "International Forwarding and Consolidation Summary - Used in logistics for shipment consolidation"},
            {"PRICAT": "Price/Sales Catalog - Contains pricing and product information"},
            {"PAYMUL": "Multiple Payment Order - Handles multiple payments in financial transactions"},
            {"RECADV": "Receiving Advice - Notifies the sender of the goods that they were received"},
        ],
        "TRADACOMS (UK Retail Standard)": [
            {"INVFIL": "Invoice File - Used for billing in the UK retail sector"},
            {"ORDHDR": "Order Header - The header of a purchase order document"},
            {"DELHDR": "Delivery Header - Provides delivery instructions for an order"},
        ],
        "VDA (German Automotive Standard)": [
            {"4905": "Delivery Schedule - Communicates delivery schedules in automotive manufacturing"},
            {"4913": "Invoice - Used for billing in the automotive industry"},
        ],
        "RosettaNet (Technology Industry Standard)": [
            {"3A4": "Purchase Order - Used for ordering goods in the high-tech industry"},
            {"4B2": "Advance Shipment Notification - Communicates shipment details in the tech supply chain"},
        ],
        "Industry-Specific EDI Documents": {
            "Retail": [
                {"852": "Product Activity Data - Provides information about inventory movement and sales"},
                {"867": "Product Transfer and Resale Report - Tracks resales of products through distribution channels"},
            ],
            "Transportation & Logistics": [
                {"214": "Transportation Carrier Shipment Status Message - Provides shipment updates in real-time"},
                {"210": "Motor Carrier Freight Details and Invoice - Used for billing in the transportation industry"},
            ],
            "Healthcare": [
                {"270": "Healthcare Eligibility Inquiry - Verifies patient insurance coverage"},
                {"271": "Healthcare Eligibility Response - Responds to the eligibility inquiry"},
            ],
            "Financial Services": [
                {"821": "Financial Information Reporting - For reporting bank account summaries and balances"},
                {"823": "Lockbox - Reports payments received through a lockbox service"},
            ],
        },
    }

    print("Known EDI Documents and Their Uses:\n")
    for standard, documents in edi_documents.items():
        print(f"{standard}:")
        if isinstance(documents, list):
            for doc in documents:
                for code, description in doc.items():
                    print(f"  {code}: {description}")
        elif isinstance(documents, dict):
            for industry, industry_docs in documents.items():
                print(f"  {industry}:")
                for doc in industry_docs:
                    for code, description in doc.items():
                        print(f"    {code}: {description}")
        print()


if __name__ == "__main__":
    list_edi_documents()

