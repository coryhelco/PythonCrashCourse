class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.response = []
        #self.responses = set()

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.response.append(new_response)
        #self.responses.add(new_response) (If you want to use a set instead of a list)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.response:
            print(f"- {response}")