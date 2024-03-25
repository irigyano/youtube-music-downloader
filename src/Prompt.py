import inquirer

class Prompt:
    def prompt_input_type(self):
        questions = [
        inquirer.List('type',
                        message="What's the target type?",
                        choices=['Video', 'Playlist'],
                    ),
        ]
        return inquirer.prompt(questions)['type']
    
    def prompt_url(self):
        print('Target url:')
        return input()
    
    def prompt(self):
        return self.prompt_input_type() , self.prompt_url()
