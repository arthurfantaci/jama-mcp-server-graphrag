"""Evaluation module for GraphRAG quality assessment.

Provides RAGAS-based evaluation metrics with LangSmith integration
for measuring retrieval and generation quality.

Usage:
    from jama_mcp_server_graphrag.evaluation import (
        evaluate_rag_pipeline,
        create_evaluation_dataset,
        RAGEvaluator,
    )

    # Create evaluator
    evaluator = RAGEvaluator(config)

    # Run evaluation
    results = await evaluator.evaluate(dataset)
"""

from jama_mcp_server_graphrag.evaluation.datasets import (
    EvaluationSample,
    create_evaluation_dataset,
    get_sample_evaluation_data,
)
from jama_mcp_server_graphrag.evaluation.metrics import (
    RAGMetrics,
    compute_all_metrics,
    compute_answer_relevancy,
    compute_context_precision,
    compute_context_recall,
    compute_faithfulness,
)
from jama_mcp_server_graphrag.evaluation.runner import (
    EvaluationReport,
    EvaluationResult,
    RAGEvaluator,
    evaluate_rag_pipeline,
)

__all__ = [
    "EvaluationReport",
    "EvaluationResult",
    "EvaluationSample",
    "RAGEvaluator",
    "RAGMetrics",
    "compute_all_metrics",
    "compute_answer_relevancy",
    "compute_context_precision",
    "compute_context_recall",
    "compute_faithfulness",
    "create_evaluation_dataset",
    "evaluate_rag_pipeline",
    "get_sample_evaluation_data",
]
