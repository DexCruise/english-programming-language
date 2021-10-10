# THE ENGLISH PROGRAMMING LANGUAGE

TABLE OF CONTENTS:  
1: PARTS OF SPEECH  
2: PUNCTUATION  
3: GRAMMAR

## 1: PARTS OF SPEECH

Parts of Speech are the core of the english language. Every word is a part of speech.  
The following parts of speech are defined in this specification:

A. NOUNS            // variables in functional languages or objects and classes in object-oriented languages  
B. PRONOUNS         // pointers and references to previous variables  
C. VERBS            // functions, methods, and declarations  
D. ADJECTIVES       // fields  
R. ADVERBS          // TODO: think about adverbs  
F. PREPOSITIONS     // control flow  
G. CONJUNCTIONS     // some builtin keywords  
H. INTERJECTIONS    // preprocessor/interpreter instructions, like decorators in python and directives in c/c++

### **A: NOUNS**

Nouns store data, or form patterns to store data and execute verbs. 
There are eight types of nouns, and every noun is in four different types:

i.    Common //classes  
ii.   Proper //objects  
iii.  Concrete  
iv.   Abstract  
v.    Regular  
vi.   Irregular  
vii.  Countable  
iix.  Uncountable

#### *i: COMMON NOUNS*

These nouns are patterns - like "classes" in Java - that dictate how proper nouns that are instances of them behave, and what properties they can have.  
New common nouns are designated with a plural suffix (like `s` and `es`), like so:

`Rocks exist` makes a *concrete common* noun called `rock`.

or:

`Potatoes can be interesting, and can be Brown, Purple, Yellow, or Green.` makes a *concrete common* noun called `potato` if `potato` doesn't exist.  
If `potato` already exists, it updates `potato` to add or update the adjectives.

Said `potato` has gets an adjective `interesting`. They can either be
- `interesting` or
- `not interesting`.

Said `potato` gets a `colour`, which is a standard adjective of all concrete nouns.  
Valid `colours` for a `potato` would be:
- `Brown`
- `Purple`
- `Yellow`
- `Green`

`Rocks can be interesting.` would add an adjective to Rocks. This can be queried with a question, like `Is Janet interesting?`

If `Janet` (a proper noun that can be interesting, for instance a rock as defined above) is interesting, it will return `Yes`.  
If `Janet` is not interesting, it will return `No`.

#### *ii: PROPER NOUNS*

These nouns are instances of common nouns - like "objects" in java.

#### *iii: CONCRETE NOUNS*

These nouns are defined using the verb "to be" and are modified or referenced by verbs.  
A concrete noun can be common or proper, for instance:

`Janet is a rock.` would instantiate a new `rock` - a common noun - called `Janet` - a proper noun.

#### *iv: ABSTRACT NOUNS*

TODO: think of something for abstract nouns





### **G: CONJUNCTIONS**

Conjunctions are built-in keywords that can perform actions on nouns, pronouns, verbs, adjectives, and adverbs.  
There are three types of conjunction:

- i. Coordinating
- ii. Subordinating
- iii. Correlative

#### *i: COORDINATING CONJUNCTIONS*

These conjunctions link two equal parts of a sentence, for instance:

`Are Janet and Mark rocks?`

`and` takes `Janet` and `Mark`, and looks for something to do with them. 

In this case, it checks whether they are both rocks, and returns `Yes` if they are and `No` if they are not.

#### *ii: SUBORDINATING CONJUNCTIONS*

Connects an *independent* clause to a *dependent* clause, like so:

`If Janet is interesting, Mark is not interesting.`

`if` looks for the primary adjective in the clause, being `is`.

#### *iii: CORRELATIVE CONJUNCTIONS*

Correlative conjunctions come in pairs.

## ***2: PUNCTUATION***

