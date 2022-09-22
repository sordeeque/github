from win32printing import Printer
import json
import requests

font = {
    "height": 12,
}
#with Printer(linegap=1) as printer:
 #   printer.text("Thank you Jesus for all you do am so glad", font_config=font)

SERVER_URL = 'http://127.0.0.1:5000'

ref_no = 'AR-115920220'


    
def print_receipt(recept):
    font = {
        "height": 15,
    }
    with Printer(linegap=1) as printer:
        printer.text("ARKSOFT TECHNOLOGIES", align='center', font_config=font)
        font[ 'height' ] = 8
        printer.text(f"Opposite Victory Baptist Church, Alogi, Obantoko, Abeokuta, Ogun State.\nTel: 08134829216, 08140359868", align='center', font_config=font)
        printer.text("____________________________________________________________________", font_config=font)
        font[ 'height' ] = 20
        printer.text("RECEIPT", align='center', font_config=font)
        font[ 'height' ] = 8
        printer.text("____________________________________________________________________\n", font_config=font)
        printer.text(f"DATE: {recept[ 'date' ]}", align='left', font_config=font)
        printer.text(f"STUDENT NAME: {recept[ 'name' ]}", align='left', font_config=font)
        printer.text(f"RECEPTIONIST: {recept[ 'rep' ]}", align='left', font_config=font)
        printer.text(f"PAYMENT MODE: {recept[ 't_type' ]}", align='left', font_config=font)
        printer.text(f"TRANSACTION REF: {recept[ 'ref' ]}\n", align='left', font_config=font)
        font[ 'height' ] = 10
        
        printer.text(f'DESCRIPTION: {recept["desc"]}\n',align='left', font_config=font)
        font[ 'height' ] = 15
        printer.text(f'AMOUNT: ₦{"{:,.2f}".format(recept["amount"])}',align='center', font_config=font)
            
        font[ 'height' ] = 8
        printer.text("____________________________________________________________________", font_config=font)
        printer.text("POWERED BY: Arksoft Technologies\nAbeokuta Ogun State\n08134829216", align='center',
                     font_config=font)

def get_ref():
    params = ref_no
    details = json.dumps(params)  # convert dictionary object to json file
    r = requests.post(f"{SERVER_URL}/api/receipt_by_ref", json=details)
    responce = r.json()
    responce = responce['receipt']
    print_receipt(responce)

get_ref()

#print_receipt(receipt)
