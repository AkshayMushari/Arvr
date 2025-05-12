from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, RecognizerResult, EntityRecognizer
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
from transformers import pipeline


class TransformersRecognizer(EntityRecognizer):
    def __init__(self, model_name="dslim/bert-base-NER", supported_entities=None):
        super().__init__(supported_entities=supported_entities or ["PERSON", "ORG", "LOC"], name="TransformersRecognizer")
        self.model_name = model_name
        self.pipeline = pipeline("ner", model=model_name, tokenizer=model_name, aggregation_strategy="simple")

    def load(self):
        pass  

    def analyze(self, text, entities, nlp_artifacts=None):
        results = []
        ner_results = self.pipeline(text)

        for r in ner_results:
            entity = r.get("entity_group")
            if entity in entities:
                result = RecognizerResult(
                    entity_type=entity,
                    start=r["start"],
                    end=r["end"],
                    score=r["score"],
                    analysis_explanation=None  # Removed `recognizer_name`
                )
                results.append(result)

        return results


analyzer = AnalyzerEngine()
transformers_recognizer = TransformersRecognizer()
analyzer.registry.add_recognizer(transformers_recognizer)

text = "My name is John Doe. I work at Microsoft and live in New York."

results = analyzer.analyze(text=text, language="en")
print("\n[+] Entities Detected:")
for res in results:
    print(f"{res.entity_type} ({res.start}, {res.end}): {text[res.start:res.end]} | Score: {res.score:.2f}")

anonymizer = AnonymizerEngine()
operators = {
    "PERSON": OperatorConfig("replace", {"new_value": "ANONYMIZED"}),
    "ORG": OperatorConfig("replace", {"new_value": "ANONYMIZED"}),
    "LOC": OperatorConfig("replace", {"new_value": "ANONYMIZED"})
}
operators = {
    "PERSON": OperatorConfig("replace", {"new_value": "<Redacted_Person>"}),
    "ORG": OperatorConfig("replace", {"new_value": "<Redacted_Org>"}),
    "LOC": OperatorConfig("replace", {"new_value": "<Redacted_Location>"}),
}

anonymized_result = anonymizer.anonymize(text=text, analyzer_results=results, operators=operators)

print("\n[+] Anonymized Text:")
print(anonymized_result.text)
