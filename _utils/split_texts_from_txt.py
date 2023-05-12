import os
from ukrainian_countables import ukrainian_countables

path = '../text_txt_raw/'

with open('txt_filenames', 'r') as file:
    filenames = file.read().splitlines()


for filename in filenames:
    # Psalm book is different format, so I'll handle it manually
    if 'ps' in filename.lower():
        continue

    with open(path + filename) as file:
        # Each txt file contains hole Bible book with short
        # retelling at the beginning, which I remove by the following
        intro, content = file.read().split('Кінець короткого змісту')

    # Each chapter should be saved as a separate .txt file
    # so I split by the following word
    split_word = 'Розділ'
    chapters = content.replace('\n', ' ').split(split_word)[1:]

    # There are 4 books in the dataset, which consist of single chapter
    # So I process them with special care
    if len(chapters) == 0:
        cut = content.replace('\n', ' ')
        with_name = intro.split('\n')[0].title() + '. ' + cut
        filtered = ''.join(list(filter(lambda ch: not ch.isdigit(), with_name)))
        final_str = " ".join(filtered.split())

        # print(final_str[:150])

        filename_to_write = '../text_txt_clean/' + filename[:-4] + '/' + filename[:-4] + f'_01' + '.txt'
        print(filename_to_write)

        with open(filename_to_write, 'w') as file:
            file.write(final_str)

    else:
        # In the following loop, prepare each chapter str to write to file
        for idx, chapter in enumerate(chapters):

            # Cut the number of character
            cut = chapter[len(str(idx + 1)) + 1:]

            # Remove all digits (which mark the number of poems)
            filtered = ''.join(list(filter(lambda ch: not ch.isdigit(), cut)))

            # Add chapter word and chapter number in ukrainian
            # Chapter number is originally an int, so I replace it with str
            almost_ready = split_word + ' ' + ukrainian_countables[idx] + '.' + filtered

            # Get rid of extra (double) spaces
            final_str = " ".join(almost_ready.split())

            # print(final_str[:150])



            filename_to_write = '../text_txt_clean/' + filename[:-4] + '/' + filename[:-4] + f'_{idx + 1:02d}' + '.txt'
            print(filename_to_write)
            print()

            with open(filename_to_write, 'w') as file:
                file.write(final_str)


    print()
