def distance(a: str, b: str) -> int:
    """
    :param a: first word
    :param b: second word
    :return: distance between word a and word b as an integer
    """
    similar = 0
    for l in a:
        if l in b:
            similar += 1
    return similar


common = [
    "to",
    "the",
    "a",
    "how",
    "what",
    "when",
    "where",
    "why",
    "an",
    "there",
    "me",
    "about",
    "all",
    "also",
    "and",
    "as",
    "at",
    "be",
    "because",
    "but",
    "by",
    "can",
    "come",
    "could",
    "day",
    "do",
    "even",
    "find",
    "first",
    "for",
    "from",
    "get",
    "give",
    "go",
    "have",
    "he",
    "here",
    "him",
    "his",
    "how",
    "i",
    "if",
    "in",
    "into",
    "it",
    "its",
    "just",
    "know",
    "like",
    "look",
    "make",
    "man",
    "many",
    "me",
    "more",
    "my",
    "new",
    "no",
    "not",
    "now",
    "of",
    "on",
    "one",
    "only",
    "or",
    "other",
    "our",
    "out",
    "people",
    "say",
    "see",
    "she",
    "so",
    "some",
    "take",
    "tell",
    "than",
    "that",
    "the",
    "their",
    "them",
    "then",
    "there",
    "these",
    "they",
    "thing",
    "think",
    "this",
    "those",
    "time",
    "to",
    "two",
    "up",
    "use",
    "very",
    "want",
    "way",
    "we",
    "well",
    "what",
    "when",
    "which",
    "who",
    "will",
    "with",
    "would",
    "year",
    "you",
    "your",
    "is"
]

responses = {
    ("hello", "hi", "who"): "Hello, this is a chatbot.",
    ("delivery", "shipping", "postage"): "Shipping information can be found on the FAQ.",
    ("materials", ): "Material information can be found in the description of each product.",
}

def find_response(question):
    words = question.split(" ")
    filtered = []
    for w in words:
        if w.lower() not in common:
            filtered.append(w.lower())

    print(filtered)
    closest = (0, "I didn't understand.")
    for word in words:
        for kws, response in responses.items():
            for kw in kws:
                dist = distance(word, kw)
                if dist > len(kw) / 2:
                    if closest[0] == 0:
                        closest = (distance(word, kw), responses[kws])
                    if distance(word, kw) > closest[0]:
                        closest = (distance(word, kw), responses[kws])
    return closest[1]
