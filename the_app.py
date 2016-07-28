
class AppReader:
    '''
    This app opens two text files as lists, then combines them together into a dictionary. The first file is a list of car makes, and the second file is a list of car models. the resulting dictionary has the car makes as keys, and the car models as items in the car make value list.

    methods: open_makes, open_models, make_dictionary, print_dictionary.
    '''

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
        '''
        loops through the list of makes in the makes.txt file and creates a dictionary with each make.txt item as a key and an empty list as a value.
        loops through the list of models in the models.txt file and adds matching models as list items for the corresponting make.
        Arguments: None.
        '''
        makes = self.open_makes()
        models = self.open_models()

        for make in makes:
            # create a dictionary entry with an empty list for a value, for each make.
            self.dictionary[make] = []
            # then loop through the models list and add any models of the correct make to the list.
            for model in models:
                if model[0] == make[0]:
                    # note here I'm taking off the '(first letter)=' from the model list items.
                    self.dictionary[make].append(model[2:])

    def print_dictionary(self):
        '''
        prints the final dictionary in format. Run only after make_dictionary.
        arguments: none
        '''
        for (key, value) in self.dictionary.items():
            print(key.upper() + ": " + ", ".join(value))

if __name__ == '__main__':
    app = AppReader()
    app.make_dictionary()
    app.print_dictionary()
