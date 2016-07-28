
class AppReader:

    def open_makes(self):
        '''
        opens the 'models.txt' file and prints each line. currently without the model initial and equals sign and without the newline, but that's likely to change.
        Arguments: none
        '''

        with open("makes.txt", "r") as makes:
            for make in makes:
                print(make[:-1])


    def open_models(self):
        '''
        opens the 'models.txt' file and prints each line. currently without the model initial and equals sign and without the newline, but that's likely to change.
        Arguments: none
        '''
        with open("models.txt", "r") as models:
            for model in models:
                print(model[2:][:-1])


if __name__ == '__main__':
    app = AppReader()
    # app.open_makes()
    # app.open_models()
