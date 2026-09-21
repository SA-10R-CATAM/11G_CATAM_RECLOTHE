
from pyscript import display, document

# Define club information using dictionaries
thrift_info = {
            "1": {
                "name":"HMR Trading Haus Pioneer",
                "adress": "Pionees Corner, Reliance St.",
                "time": "9:00 AM - 8:00 PM",
                "location": "Pioneer corner, Reliance St, Mandaluyong City, 1554 Metro Manila",
               
            },
            "2": {
                "name": "FLEUR DE LIS UKAY-UKAY",
                "address": "409 EDSA, Mandaluyong",
                "time": "9:00 AM - 8:00 PM",
                "location": "409 Epifanio de los Santos Ave, Mandaluyong City, 1554 Metro Manila",
               
            },
            "3": {
                "name": "MRPM Ukay Ukay Store࣪",
                "address": "15-A Shaw Blvd.",
                "time": "8:30 AM - 7:00 PM",
                "location": "15 A, 15a Shaw Blvd, Mandaluyong City, 1552 Metro Manila",
              
            },
            "4": {
                "name": "Ukay ukay Kalentong",
                "address": "192 Gen. Kalentong",
                "time": "NO GIVEN TIME.",
                "location": "192 Gen Kalentong, Mandaluyong City, Metro Manila",
                
            },
            "5": {
                "name": "The FashionCafe by #RetailTherapy",
                "address": "713 D Boni Ave., Brgy. Malamig, Mandaluyong City",
                "time": "8:00 AM - 7:00 PM",
                "location": "Boni Ave, Brgy Malamig, Mandaluyong City, 1500 Metro Manila",
                
            },
            "6": {
                            "name": "Thrifty Haven PH",
                            "address": "Pinagtipunan, Mandaluyong",
                            "time": "OPEN 24 HOURS",
                            "location": "H2QM+69Q, Pinagtipunan, Mandaluyong City, 1550 Kalakhang Maynila",
                            
            },
            "7": {
                            "name": "Ukay Luxe Heaven",
                            "address": "Petsay St., Mandaluyong",
                            "time": "10:00 AM - 5:00 PM",
                            "location": "Petsay Street, 295 Block 38, Mandaluyong City, 1550 Metro Manila",
                           
            },
            "8": {
                            "name": "Segunda Mana - 500 Shaw",
                            "address": "Lica Mall, 500 Shaw Blvd.",
                            "time": "NO GIVEN TIME.",
                            "location": "Lica Mall, 500 Shaw Blvd, Zentrum, Mandaluyong City, 1550 Metro Manila",
                            
            },
            "9": {
                            "name": "Khaels Garment Store",
                            "address": "550 F. Martinez Ave.",
                            "time": "6:00 AM - 6:00 PM",
                            "location": "550 F. Martinez Ave, Mandaluyong City, 1550 Metro Manila",
                            
            },

            
            "": {
                "name": "",
                "address": "",
                "time": "",
                "location": "",
               
            }
        }
        
def show_thrift_info(event):
    selected_store = document.getElementById("store-select").value
    info = thrift_info.get(selected_store)

    if not info:
        display("Please select a store.", target="thrift-info")
        return

    output = f"""
{info['name']}
Address: {info.get('address', '')}
Time: {info.get('time', '')}
Location: {info.get('location', '')}
"""

    display(output, target="thrift-info")