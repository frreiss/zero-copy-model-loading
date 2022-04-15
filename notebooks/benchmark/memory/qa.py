import transformers

QA_MODEL_NAME = 'deepset/roberta-base-squad2'
QA_INPUT = {
    'question': 'What is 1 + 1?',
    'context': 
        """Addition (usually signified by the plus symbol +) is one of the four basic operations of 
        arithmetic, the other three being subtraction, multiplication and division. The addition of two 
        whole numbers results in the total amount or sum of those values combined. The example in the
        adjacent image shows a combination of three apples and two apples, making a total of five apples. 
        This observation is equivalent to the mathematical expression "3 + 2 = 5" (that is, "3 plus 2 
        is equal to 5").
        """
}

qa_pipeline = transformers.pipeline('question-answering',
                                    model=QA_MODEL_NAME)
print(qa_pipeline(**QA_INPUT))


