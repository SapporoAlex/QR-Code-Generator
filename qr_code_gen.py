import qrcode
import sys

# I'd like to give a huge thanks to lincolnloop, maribedran and SmileyChris.
# Thank you for such a convenient and simple library.

run = True

while run:
    print("Welcome to Alex's QR Code Generator")
    print('1. Generate QR code')
    print('2. Exit program')
    choice = input('> ')

    if choice == '1':
        url = input('Paste URL here: ')
        file_name = input('Name file: ')
        if file_name == '':
            file_name = 'QR_code'
        img = qrcode.make(f'{url}')

        if file_name[-4:] != '.png':
            img.save(f'{file_name}.png')
        else:
            img.save(f'{file_name}')
        print(f"QR code saved as {file_name}.png")

    elif choice == '2':
        run = False
        print("Exiting the program. Goodbye!")

    else:
        print("Invalid choice. Please enter '1' or '2'.")

sys.exit()

