import os
import sys
from typing import Dict, Any, List, Optional
from deepeval.test_case import LLMTestCase

try:
    from deepeval.test_case import SingleTurnParams as MetricParams
except ImportError:
    from deepeval.test_case import LLMTestCaseParams as MetricParams

from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    ContextualRelevancyMetric,
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    HallucinationMetric,
    ToxicityMetric,
    BiasMetric,
    GEval
)

try:
    from eval.eval_gemini import GeminiLLM
except ImportError:
    from eval_gemini import GeminiLLM


def get_eval_judge(model_name: str = "gemini-3.1-flash-lite") -> GeminiLLM:
    """Returns an instance of GeminiLLM to act as the evaluation judge."""
    return GeminiLLM(model_name=model_name)


def create_all_metrics(judge: Optional[GeminiLLM] = None) -> List[Any]:
    """
    Creates and returns all 9 evaluation metrics requested:
    1. Answer Relevancy
    2. Faithfulness
    3. Contextual Relevancy
    4. Contextual Precision
    5. Contextual Recall
    6. Correctness (GEval)
    7. Hallucination
    8. Toxicity
    9. Bias
    """
    judge = judge or get_eval_judge()

    correctness_metric = GEval(
        name="Correctness",
        criteria="Evaluate if the actual output is factually correct, accurate, and completely addresses the prompt.",
        evaluation_params=[MetricParams.INPUT, MetricParams.ACTUAL_OUTPUT],
        threshold=0.7,
        model=judge
    )

    return [
        AnswerRelevancyMetric(threshold=0.6, model=judge),
        FaithfulnessMetric(threshold=0.6, model=judge),
        ContextualRelevancyMetric(threshold=0.6, model=judge),
        ContextualPrecisionMetric(threshold=0.6, model=judge),
        ContextualRecallMetric(threshold=0.6, model=judge),
        correctness_metric,
        HallucinationMetric(threshold=0.6, model=judge),
        ToxicityMetric(threshold=0.7, model=judge),
        BiasMetric(threshold=0.7, model=judge)
    ]


def evaluate_single_response(
    user_input: str,
    actual_output: str,
    expected_output: Optional[str] = None,
    context: Optional[List[str]] = None,
    judge_model_name: str = "gemini-3.1-flash-lite"
) -> Dict[str, Any]:
    """
    Evaluates a single chatbot user_input and actual_output across all 9 DeepEval metrics.
    Returns a structured dictionary of results for table rendering.
    """
    judge = get_eval_judge(model_name=judge_model_name)

    # Supply fallback context if none provided so context-dependent metrics can evaluate
    retrieval_ctx = context or [f"User query topic: {user_input}. Response: {actual_output}"]
    exp_output = expected_output or actual_output

    test_case = LLMTestCase(
        input=user_input,
        actual_output=actual_output,
        expected_output=exp_output,
        retrieval_context=retrieval_ctx,
        context=retrieval_ctx
    )

    metrics = create_all_metrics(judge=judge)
    results = {}

    for metric in metrics:
        metric.measure(test_case)
        
        # Format display name
        if hasattr(metric, "__name__"):
            raw_name = metric.__name__
        else:
            raw_name = metric.__class__.__name__

        if raw_name == "GEval":
            display_name = getattr(metric, "name", "Correctness")
        else:
            # e.g., AnswerRelevancyMetric -> Answer Relevancy
            display_name = raw_name.replace("Metric", "")
            display_name = "".join([f" {c}" if c.isupper() and i > 0 else c for i, c in enumerate(display_name)]).strip()

        score = round(getattr(metric, "score", 0.0) or 0.0, 3)
        passed = metric.is_successful() if hasattr(metric, "is_successful") else score >= getattr(metric, "threshold", 0.6)
        reason = getattr(metric, "reason", "Evaluated successfully.") or "Evaluated successfully."

        results[display_name] = {
            "score": score,
            "passed": passed,
            "reason": reason
        }

    return results
