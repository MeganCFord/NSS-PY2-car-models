
class AppReader:

    def __init__(self):
        self.dictionary = {}

    def open_makes(self):
        '''
        opens the 'models.txt' file and prints each line. currently without the model initial and equals sign and without the newline, but that's likely to change.
        Arguments: none
        '''
        makes_list = []
        with open("makes.txt", "r") as makes:
            for make in makes:
                makes_list.append(make[:-1])
        return makes_list

    def open_models(self):
        '''
        opens the 'models.txt' file and prints each line. currently without the model initial and equals sign and without the newline, but that's likely to change.
        Arguments: none
        '''
        models_list = []
        with open("models.txt", "r") as models:
            for model in models:
                models_list.append(model[:-1])
        return models_list

    def make_dictionary(self):
        makes = self.open_makes()
        models = self.open_models()

        for make in makes:
            self.dictionary[make] = []
            for model in models:
                if model[0] == make[0]:
                    self.dictionary[make].append(model[2:])

        print(self.dictionary)

if __name__ == '__main__':
    app = AppReader()
    app.make_dictionary()
    # app.open_makes()
    # app.open_models()
