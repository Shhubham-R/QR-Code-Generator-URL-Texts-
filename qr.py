import qrcode

def main():
    data = input("enter the text or URL for converting into QR: ")
    output = input("enter the output file name 'example.png' or press enter for 'qrcode.png':") or "qrcode.png"
    box_size = int(input("enter the box size or (press enter for default 10 ):") or 10)
    border = int(input("enter the border thinkness (press enter for default 4):") or 4) 
    fill = input("enter the color (press enter for default 'black'):") or "black"
    back = input("enter the background color (press enter for 'white'):") or "white"
    
    #setting up the Qr code object
    qr = qrcode.QRCode(box_size = box_size ,border=border)
    
    #adding data 
    qr.add_data(data)
    
    #building qr
    qr.make(fit = True)

    #createing image
    img = qr.make_image(fill_color=fill, back_color = back)
    img.save(output)

    print(f"the QR code generated and saved to {output}")

if __name__ == "__main__":
    main()