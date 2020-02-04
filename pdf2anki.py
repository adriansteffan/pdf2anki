from pdf2image import convert_from_path
import os
import sys


if len(sys.argv) < 3:
    print('Invalid number of arguments. Refer to the readme for usage instructions.')
    exit()

pdf_file = sys.argv[1]
deck_name = sys.argv[2]


out_folder = 'pdf2anki_images_%s' % deck_name
pages = convert_from_path(pdf_file, 500)

if not os.path.exists(out_folder):
    os.makedirs(out_folder)

for i in range(0, len(pages)):
    pages[i].save('%s/Image_%s_%05d.jpg' % (out_folder, deck_name, i), 'JPEG')


with open('pdf2anki_%s.csv' % deck_name, 'a') as f:

    f.write("\n".join(['%s_%05d;<img src="Image_%s_%05d.jpg"/>;<img src="Image_%s_%05d.jpg"/>\n' %
                 (deck_name, image_number, deck_name, image_number*2, deck_name, image_number * 2 + 1)
     for image_number in range(0, int(len(pages)/2))]))


