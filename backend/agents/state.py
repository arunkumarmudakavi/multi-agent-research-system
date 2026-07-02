from pydantic import BaseModel, Field


class Task(BaseModel):
    topic: str
    description: str


class Source(BaseModel):
    topic: str
    title: str
    url: str
    content: str
    score: float | None = None


class Finding(BaseModel):
    topic: str
    content: str


class VerifiedFinding(BaseModel):
    topic: str
    content: str
    confidence_score: float = Field(ge=0.0, le=1.0)  # Confidence score between 0 and 1


class ResearchState(BaseModel):
    query: str
    tasks: list[Task] = Field(default_factory=list)
    sources: list[Source] = Field(default_factory=list)
    findings: dict[str, Finding] = Field(default_factory=dict)
    verified_findings: dict[str, VerifiedFinding] = Field(default_factory=dict)
    report: str = ""
    status: str = "PENDING"
    errors: list[str] = Field(default_factory=list)
