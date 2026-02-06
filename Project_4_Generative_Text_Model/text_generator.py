import random

class MarkovTextGenerator:
    def __init__(self, text):
        self.model = {}
        words = text.split()

        for i in range(len(words) - 1):
            key = words[i]
            if key not in self.model:
                self.model[key] = []
            self.model[key].append(words[i + 1])

    def generate(self, start_word, length=40):
        current = start_word
        result = [current]

        for _ in range(length):
            next_words = self.model.get(current)
            if not next_words:
                break
            current = random.choice(next_words)
            result.append(current)

        return " ".join(result)


if __name__ == "__main__":
    print("===== Generative Text Model (GPT-Style) =====\n")

    training_text = (
        "Machine learning is important because it enables systems to learn from data "
        "and improve performance without being explicitly programmed. "
        "Artificial intelligence is transforming industries by automating tasks "
        "and providing intelligent insights."
    )

    generator = MarkovTextGenerator(training_text)

    prompt = input(
        "Enter a starting word (select one word from: 'Machine, learning, intelligence'): "
    ).strip()

    if not prompt:
        prompt = "Machine"

    generated_text = generator.generate(prompt)

    print("\nGenerated Text:\n")
    print(generated_text)
