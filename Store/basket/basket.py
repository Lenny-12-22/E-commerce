class Basket():
    def __init__(self, request):
        self.session = request.session

        # Get the basket from session or initialize an empty basket
        self.basket = self.session.get('basket', {})

        # Save the basket back to session if it doesn't exist
        if 'basket' not in self.session:
            self.session['basket'] = self.basket
