from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel


class TextSummary(models.Model):
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    class PydanticMeta:
        exclude = ("created_at",)


SummarySchema = pydantic_model_creator(TextSummary)


