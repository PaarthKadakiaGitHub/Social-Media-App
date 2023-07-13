from django.db import models
import uuid

id = models.UUIDField(primary_key=True, default=uuid.uuid4)

# Create your tests here.
id = print(str(uuid.uuid4()))