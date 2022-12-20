import random
import constants as C


class CONSTRUCTOR_VERB:
    """
    CONSTRUCTOR FOR A VERB.
    DO NOT USE IT DIRECTLY, IT IS DESIGNED TO BE USED WITH AN ALREADY PREDEFINED INSTANCE.
    """

    VERBS = C.VERBS

    @classmethod
    def __call__(cls):
        choice = random.choice(cls.VERBS)
        return choice.lower()

    def __repr__(self):
        print('Maybe you forgot the parentheses? use verb() instead of verb.')
        return '<randword.CONSTRUCTOR_VERB object>'


class CONSTRUCTOR_NOUN:
    """
    CONSTRUCTOR FOR A NOUN.
    DO NOT USE IT DIRECTLY, IT IS DESIGNED TO BE USED WITH AN ALREADY PREDEFINED INSTANCE.
    """

    NOUNS = C.NOUNS

    @classmethod
    def __call__(cls):
        choice = random.choice(cls.NOUNS)
        return choice.lower()

    def __repr__(self):
        print('Maybe you forgot the parentheses? use noun() instead of noun.')
        return '<randword.CONSTRUCTOR_NOUN object> '


class CONSTRUCTOR_CONJUNCTION:
    """
    CONSTRUCTOR FOR A CONJUNCTION.
    DO NOT USE IT DIRECTLY, IT IS DESIGNED TO BE USED WITH AN ALREADY PREDEFINED INSTANCE.
    """

    CONJUNCTIONS = C.CONJUNCTIONS

    @classmethod
    def __call__(cls):
        choice = random.choice(cls.CONJUNCTIONS)
        return choice.lower()

    def __repr__(self):
        print('Maybe you forgot the parentheses? use conjunction() instead of conjunction.')
        return '<randword.CONSTRUCTOR_CONJUNCTION object> '


class CONSTRUCTOR_PRONOUN:
    """
    CONSTRUCTOR FOR A PRONOUN.
    DO NOT USE IT DIRECTLY, IT IS DESIGNED TO BE USED WITH AN ALREADY PREDEFINED INSTANCE.
    """

    PRONOUNS = C.PRONOUNS

    @classmethod
    def __call__(cls):
        choice = random.choice(cls.PRONOUNS)
        return choice.lower()

    def __repr__(self):
        print('Maybe you forgot the parentheses? use pronoun() instead of pronoun.')
        return '<randword.CONSTRUCTOR_PRONOUN object> '


class CONSTRUCTOR_ADJECTIVE:
    """
    CONSTRUCTOR FOR A ADJECTIVE.
    DO NOT USE IT DIRECTLY, IT IS DESIGNED TO BE USED WITH AN ALREADY PREDEFINED INSTANCE.
    """

    ADJECTIVES = C.ADJECTIVES

    @classmethod
    def __call__(cls):
        choice = random.choice(cls.ADJECTIVES)
        return choice.lower()

    def __repr__(self):
        print('Maybe you forgot the parentheses? use adjective() instead of adjective.')
        return '<randword.CONSTRUCTOR_ADJECTIVE object> '


class CONSTRUCTOR_ADVERB:
    """
    CONSTRUCTOR FOR A ADVERB.
    DO NOT USE IT DIRECTLY, IT IS DESIGNED TO BE USED WITH AN ALREADY PREDEFINED INSTANCE.
    """

    ADVERBS = C.ADVERBS

    @classmethod
    def __call__(cls):
        choice = random.choice(cls.ADVERBS)
        return choice.lower()

    def __repr__(self):
        print('Maybe you forgot the parentheses? use adverb() instead of adverb.')
        return '<randword.CONSTRUCTOR_ADVERB object> '


class CONSTRUCTOR_PREPOSITIONS:
    """
    CONSTRUCTOR FOR A PREPOSITION.
    DO NOT USE IT DIRECTLY, IT IS DESIGNED TO BE USED WITH AN ALREADY PREDEFINED INSTANCE.
    """

    PREPOSITIONS = C.PREPOSITIONS

    @classmethod
    def __call__(cls):
        choice = random.choice(cls.PREPOSITIONS)
        return choice.lower()

    def __repr__(self):
        print('Maybe you forgot the parentheses? use preposition() instead of pronoun.')
        return '<randword.CONSTRUCTOR_PREPOSITION object> '


class CONSTRUCTOR_SENTENCE:
    """
    CONSTRUCTOR FOR AN SENTENCE.
    DO NOT USE IT DIRECTLY, IT IS DESIGNED TO BE USED WITH AN ALREADY PREDEFINED INSTANCE.
    """

    @classmethod
    def __call__(cls):
        format_ = 0
        return f'{pronoun().capitalize()} {adjective()} {noun()} {adverb()} {verb()} {noun()} {conjunction()}' \
               f'{preposition()} {noun()}.'

    def __repr__(self):
        print('Maybe you forgot the parentheses? use sentence() instead of sentence.')
        return '<randword.CONSTRUCTOR_SENTENCE object>'


class CONSTRUCTOR_NAMES_MEN:
    """
    CONSTRUCTOR FOR A MAN NAME.
    DO NOT USE IT DIRECTLY, IT IS DESIGNED TO BE USED WITH AN ALREADY PREDEFINED INSTANCE.
    """

    NAMES_MEN = C.NAMES_MEN

    @classmethod
    def __call__(cls):
        choice = random.choice(cls.NAMES_MEN)
        return choice.capitalize()

    def __repr__(self):
        print('Maybe you forgot the parentheses? use name_men() instead of name_men.')
        return '<randword.CONSTRUCTOR_NAME_MEN object>'


class CONSTRUCTOR_NAMES_WOMEN:
    """
    CONSTRUCTOR FOR A WOMAN NAME.
    DO NOT USE IT DIRECTLY, IT IS DESIGNED TO BE USED WITH AN ALREADY PREDEFINED INSTANCE.
    """

    NAMES_WOMEN = C.NAMES_WOMEN

    @classmethod
    def __call__(cls):
        choice = random.choice(cls.NAMES_WOMEN)
        return choice.capitalize()

    def __repr__(self):
        print('Maybe you forgot the parentheses? use name_women() instead of name_women.')
        return '<randword.CONSTRUCTOR_NAME_WOMEN object>'


class CONSTRUCTOR_LAST_NAME:
    """
    CONSTRUCTOR FOR A LAST NAME.
    DO NOT USE IT DIRECTLY, IT IS DESIGNED TO BE USED WITH AN ALREADY PREDEFINED INSTANCE.
    """

    LAST_NAMES = C.LAST_NAMES

    @classmethod
    def __call__(cls):
        choice = random.choice(cls.LAST_NAMES)
        return choice.capitalize()

    def __repr__(self):
        print('Maybe you forgot the parentheses? use last_name() instead of last_name.')
        return '<randword.CONSTRUCTOR_LAST_NAME object>'


class CONSTRUCTOR_FULL_NAME:
    """
    CONSTRUCTOR FOR A FULL NAME.
    DO NOT USE IT DIRECTLY, IT IS DESIGNED TO BE USED WITH AN ALREADY PREDEFINED INSTANCE.
    """

    @classmethod
    def __call__(cls):
        options = [
            f'{name_woman()} {name_woman()} {lastname()}',
            f'{name_woman()} {lastname()}',
            f'{name_man()} {name_man()} {lastname()}',
            f'{name_man()} {lastname()}',
        ]
        return random.choice(options)

    def __repr__(self):
        print('Maybe you forgot the parentheses? use full_name() instead of full_name.')
        return '<randword.CONSTRUCTOR_FULL_NAMES object>'


#   Initializing the instances to be called.
verb = CONSTRUCTOR_VERB()
noun = CONSTRUCTOR_NOUN()
pronoun = CONSTRUCTOR_PRONOUN()
conjunction = CONSTRUCTOR_CONJUNCTION()
adjective = CONSTRUCTOR_ADJECTIVE()
adverb = CONSTRUCTOR_ADVERB()
preposition = CONSTRUCTOR_PREPOSITIONS()
sentence = CONSTRUCTOR_SENTENCE()
name_man = CONSTRUCTOR_NAMES_MEN()
name_woman = CONSTRUCTOR_NAMES_WOMEN()
lastname = CONSTRUCTOR_LAST_NAME()
fullname = CONSTRUCTOR_FULL_NAME()
