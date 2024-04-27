class Evaluator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def zip_evaluate(coefs :list[float], words :list[str]) -> float:
        if len(coefs) != len(words):
            return -1
        
        num_letters :list[int] = [len(word) for word in words]
        print(list(zip(coefs, words)))
        return sum([coef * num_letters for coef, num_letters in zip(coefs, num_letters)])

    @staticmethod
    def enumerate_evaluate(coefs :list[float], words :list[str]) -> float:
        if len(coefs) != len(words):
            return -1
        
        num_letters :list[int] = [len(word) for word in words]
        print(list(enumerate(coefs)))
        return sum([coef * num_letters[i] for i, coef in enumerate(coefs)])

if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))

    words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.enumerate_evaluate(coefs, words))